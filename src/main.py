import os
import sys
import threading
import time
import schedule
from subscription_manager import SubscriptionManager
from github_client import GitHubClient
from report_generator import ReportGenerator
from llm import LLM
from cli import CLI

from notifier import Notifier

class GitHubSentinel:
    def __init__(self):
        subscription_manager = SubscriptionManager()

        github_token = os.getenv('GITHUB_TOKEN')
        if not github_token:
            raise ValueError("GITHUB_TOKEN environment variable is not set")
        github_client = GitHubClient(token=github_token)

        llm = LLM()
        report_generator = ReportGenerator(llm)

        self.cli = CLI(subscription_manager, github_client, report_generator)
       
        self.notifier = Notifier(
            email_host="smtp.gmail.com",
            email_port=465,
            sender_email="your_email@gmail.com",
            sender_password="your_email_password"
        )

    def scheduler_task(self):
        """定时任务在后台运行"""
        schedule.every().day.at("09:00").do(self.cli.daily_progress_and_report)
        while True:
            try:
                # 检查并运行所有到期的任务
                schedule.run_pending()
            except Exception as e:
                # 捕获并打印任务执行中的异常，防止调度器线程退出
                print(f"Error during scheduled task execution: {str(e)}")
                # 可以选择添加更详细的日志记录
                # logger.exception("Error during scheduled task execution")
            
            # 短暂休眠，避免 CPU 占用过高
            # 这是 schedule 库推荐的标准模式
            time.sleep(1)

    def interactive_cli(self):
        self.cli.show_help();
        while True:
            command = input("Enter a command: ").strip().lower()
            if not self.cli.handle_command(command):
                break

def main():
    try:
        sentinel = GitHubSentinel()
        
        # 启动调度器任务线程
        scheduler_thread = threading.Thread(
            target=sentinel.scheduler_task,
            daemon=True
        )
        scheduler_thread.start()
        
        # 启动交互式命令行工具
        sentinel.interactive_cli()
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()

    
