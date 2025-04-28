import os
import sys
import threading
import time
import schedule
from subscription_manager import SubscriptionManager
from config import Config
from github_client import GitHubClient
from report_generator import ReportGenerator
from llm import LLM
from command_handler import CommandHandler

from notifier import Notifier

class GitHubSentinel:
    def __init__(self):
        config = Config();
        github_client = GitHubClient(token=config.github_token)
        llm = LLM(config.openai_api_key)
        report_generator = ReportGenerator(llm)
        subscription_manager = SubscriptionManager(config.subscriptions_file)
        self.command_handler = CommandHandler(subscription_manager, github_client, report_generator)

    def interactive_command(self):
        self.command_handler.show_help();
        while True:
            command = input("Enter a command: ").strip().lower()
            if not self.command_handler.handle_command(command):
                break

def main():
    try:
        sentinel = GitHubSentinel()
        
        # 启动交互式命令行工具
        sentinel.interactive_command()
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()

    
