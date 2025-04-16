import argparse
import threading
import time
from api.github_api import GitHubAPI
from subscriptions.subscription_manager import SubscriptionManager
from notifications.notifier import Notifier
from reports.report_generator import ReportGenerator
import schedule

class GitHubSentinel:
    def __init__(self):
        self.github_api = GitHubAPI(token="your_github_api_token")
        self.subscription_manager = SubscriptionManager()
        self.notifier = Notifier(email_host="smtp.gmail.com", email_port=465, sender_email="your_email@gmail.com", sender_password="your_email_password")
        self.report_generator = ReportGenerator()

    def fetch_and_generate_report(self, repo_url=None):
        """获取更新并生成报告"""
        repo_url = repo_url or self.subscription_manager.get_subscriptions()
        updates_by_repo = {}

        for repo_url in repo_url:
            owner, repo = repo_url.split('/')[-2], repo_url.split('/')[-1]
            updates = self.github_api.get_repo_updates(owner, repo)
            updates_by_repo[repo] = updates

        # 生成报告
        report = self.report_generator.generate_daily_report(updates_by_repo)
        print("Generated Report:")
        for item in report:
            print(f"Repo: {item['repo_name']}")
            print(f"Date: {item['date']}")
            print(f"Updates: {item['updates']}")

        # 发送通知
        self.notifier.send_email_notification("recipient@example.com", "GitHub Updates Report", str(updates_by_repo))

    def scheduler_task(self):
        """定时任务在后台运行"""
        schedule.every().day.at("09:00").do(self.fetch_and_generate_report)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def add_subscription(self, repo_url):
        """增加订阅"""
        self.subscription_manager.add_subscription(repo_url)
        print(f"Added subscription: {repo_url}")

    def remove_subscription(self, repo_url):
        """删除订阅"""
        self.subscription_manager.remove_subscription(repo_url)
        print(f"Removed subscription: {repo_url}")

    def show_subscriptions(self):
        """显示当前订阅的仓库"""
        subscriptions = self.subscription_manager.get_subscriptions()
        print("Current subscriptions:")
        for repo in subscriptions:
            print(repo)

    def run(self):
        """启动调度任务并进入命令行工具"""
        scheduler_thread = threading.Thread(target=self.scheduler_task, daemon=True)
        scheduler_thread.start()

        # 进入命令行工具
        while True:
            command = input("\nGitHub Sentinel Command > ").strip().split()

            if len(command) == 0:
                continue

            cmd = command[0]

            if cmd == "status":
                self.show_subscriptions()

            elif cmd == "add":
                if len(command) != 2:
                    print("Usage: add <repo_url>")
                else:
                    self.add_subscription(command[1])

            elif cmd == "remove":
                if len(command) != 2:
                    print("Usage: remove <repo_url>")
                else:
                    self.remove_subscription(command[1])

            elif cmd == "fetch":
                self.fetch_and_generate_report()

            elif cmd == "exit":
                print("Exiting...")
                break

            else:
                print(f"Unknown command: {cmd}. Type 'help' for usage.")

if __name__ == "__main__":
    sentinel = GitHubSentinel()
    sentinel.run()
