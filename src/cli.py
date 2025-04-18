# cli.py

class CLI:
    def __init__(self, subscription_manager, github_client, report_generator):
        self.subscription_manager = subscription_manager;
        self.github_client = github_client;
        self.report_generator = report_generator;

    def add_subscription(self, repo):
        """添加订阅仓库"""
        self.subscription_manager.add_subscription(repo)
        print(f"Added subscription for {repo}")
    
    def remove_subscription(self, repo):
        """移除订阅仓库"""
        self.subscription_manager.remove_subscription(repo)
        print(f"Removed subscription for {repo}")

    def list_subscriptions(self):
        """列出所有订阅的仓库"""
        subscriptions = self.subscription_manager.get_subscriptions()
        if not subscriptions:
            print("No subscriptions yet.")
        else:
            print("Subscribed repositories:")
            for repo in subscriptions:
                print(f"- {repo}")   

    def process_repositories(self, action_callback):
        """遍历所有订阅仓库并执行指定操作（如只导出或导出+生成报告）"""
        subscriptions = self.subscription_manager.get_subscriptions()
        if not subscriptions:
            print("No repositories subscribed yet.")
            return

        for repo in subscriptions:
            try:
                owner, repo_name = repo.split('/')
                print(f"Fetching updates for {repo_name}...")
                action_callback(owner, repo_name)
                print(f"Report generated for {repo_name}")
            except ValueError:
                print(f"Invalid repository format: {repo}. Expected format: owner/repo")
            except Exception as e:
                print(f"Error processing repository {repo}: {str(e)}")


    def export_daily_progress(self):
        """从所有订阅仓库获取更新"""
        self.process_repositories(
            lambda owner, repo: self.github_client.export_daily_progress(owner, repo)
        )

    def daily_progress_and_report(self):
        """从所有订阅仓库获取更新并生成报告"""
        def process(owner, repo):
            markdown_file = self.github_client.export_daily_progress(owner, repo)
            self.report_generator.generate_daily_report(markdown_file)

        self.process_repositories(process)
        
    def show_help(self):
        print("Commands:")
        print("  add <repo>       - Add a subscription for the repo")
        print("  remove <repo>    - Remove a subscription for the repo")
        print("  list             - List all subscriptions")
        print("  export           - Fetch updates and generate daily report for all subscribed repositories")
        print("  generate         - Fetch updates and generate daily report for all subscribed repositories")
        print("  exit/quit        - Exit the tool")

    def handle_command(self, command):
        command = command.strip().lower()

        if command == "exit" or command == "quit":
            print("Exiting...")
            return False
        
        elif command.startswith("add "):
            repo = command.split(" ")[1]
            self.add_subscription(repo)
        
        elif command.startswith("remove "):
            repo = command.split(" ")[1]
            self.remove_subscription(repo)
        
        elif command == "list":
            self.list_subscriptions()

        elif command == "generate":
            self.daily_progress_and_report()
        
        elif command == "export":
            self.export_daily_progress()
        
        elif command == "help":
            self.show_help()
        
        else:
            print("Unknown command. Type 'help' for available commands.")
        
        return True
