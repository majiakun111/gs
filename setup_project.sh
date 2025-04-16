#!/bin/bash

# 设置项目根目录
PROJECT_DIR="GitHubSentinel"

# 创建目录结构
mkdir -p $PROJECT_DIR/{src/{api,notifications,reports,subscriptions,utils},config,tests}

# 创建核心文件

# 1. 创建 GitHub API 集成代码
cat > $PROJECT_DIR/src/api/github_api.py <<EOF
import requests

class GitHubAPI:
    def __init__(self, token):
        self.base_url = "https://api.github.com"
        self.token = token
        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
    
    def get_repo_updates(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/events"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_subscription_repos(self, user):
        url = f"{self.base_url}/users/{user}/subscriptions"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

# 示例用法
if __name__ == "__main__":
    github_api = GitHubAPI(token="your_github_api_token")
    updates = github_api.get_repo_updates(owner="octocat", repo="Hello-World")
    print(updates)
EOF

# 2. 创建 订阅管理代码
cat > $PROJECT_DIR/src/subscriptions/subscription_manager.py <<EOF
import json
import os

class SubscriptionManager:
    def __init__(self, file_path="subscriptions.json"):
        self.file_path = file_path
        self.subscriptions = self.load_subscriptions()
    
    def load_subscriptions(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                return json.load(file)
        return []
    
    def save_subscriptions(self):
        with open(self.file_path, "w") as file:
            json.dump(self.subscriptions, file, indent=4)
    
    def add_subscription(self, repo_url):
        if repo_url not in self.subscriptions:
            self.subscriptions.append(repo_url)
            self.save_subscriptions()
    
    def remove_subscription(self, repo_url):
        if repo_url in self.subscriptions:
            self.subscriptions.remove(repo_url)
            self.save_subscriptions()
    
    def get_subscriptions(self):
        return self.subscriptions

# 示例用法
if __name__ == "__main__":
    manager = SubscriptionManager()
    manager.add_subscription("https://github.com/octocat/Hello-World")
    print(manager.get_subscriptions())
EOF

# 3. 创建 通知系统代码
cat > $PROJECT_DIR/src/notifications/notifier.py <<EOF
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Notifier:
    def __init__(self, email_host, email_port, sender_email, sender_password):
        self.email_host = email_host
        self.email_port = email_port
        self.sender_email = sender_email
        self.sender_password = sender_password
    
    def send_email_notification(self, recipient_email, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        try:
            with smtplib.SMTP_SSL(self.email_host, self.email_port) as server:
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_email, msg.as_string())
            print("Email sent successfully")
        except Exception as e:
            print(f"Failed to send email: {e}")
    
    def send_slack_notification(self, slack_webhook_url, message):
        import requests
        payload = {"text": message}
        response = requests.post(slack_webhook_url, json=payload)
        if response.status_code == 200:
            print("Slack notification sent successfully")
        else:
            print(f"Failed to send Slack notification: {response.status_code}")

# 示例用法
if __name__ == "__main__":
    notifier = Notifier(
        email_host="smtp.gmail.com", 
        email_port=465, 
        sender_email="your_email@gmail.com", 
        sender_password="your_email_password"
    )
    notifier.send_email_notification("recipient@example.com", "Test Subject", "This is a test email.")
EOF

# 4. 创建 报告生成代码
cat > $PROJECT_DIR/src/reports/report_generator.py <<EOF
from datetime import datetime

class ReportGenerator:
    def __init__(self):
        self.reports = []
    
    def generate_report(self, repo_name, updates):
        report = {
            "repo_name": repo_name,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updates": updates
        }
        self.reports.append(report)
    
    def generate_daily_report(self, updates_by_repo):
        for repo_name, updates in updates_by_repo.items():
            self.generate_report(repo_name, updates)
        return self.reports
    
    def generate_weekly_report(self, updates_by_repo):
        for repo_name, updates in updates_by_repo.items():
            self.generate_report(repo_name, updates)
        return self.reports

# 示例用法
if __name__ == "__main__":
    report_generator = ReportGenerator()
    daily_updates = {
        "Hello-World": ["Commit 1", "PR #2 merged"],
        "GitHub-Sentinel": ["Issue #3 opened", "Commit 4"]
    }
    report = report_generator.generate_daily_report(daily_updates)
    print(report)
EOF

# 5. 创建 主程序文件
cat > $PROJECT_DIR/src/main.py <<EOF
import schedule
import time
from src.api.github_api import GitHubAPI
from src.subscriptions.subscription_manager import SubscriptionManager
from src.notifications.notifier import Notifier
from src.reports.report_generator import ReportGenerator

def fetch_and_notify():
    github_api = GitHubAPI(token="your_github_api_token")
    subscription_manager = SubscriptionManager()
    notifier = Notifier(email_host="smtp.gmail.com", email_port=465, sender_email="your_email@gmail.com", sender_password="your_email_password")
    report_generator = ReportGenerator()

    # 获取订阅的仓库
    for repo_url in subscription_manager.get_subscriptions():
        owner, repo = repo_url.split('/')[-2], repo_url.split('/')[-1]
        updates = github_api.get_repo_updates(owner, repo)
        
        # 生成报告
        report_generator.generate_daily_report({repo: updates})
        
        # 发送通知
        notifier.send_email_notification("recipient@example.com", f"Updates for {repo}", str(updates))

# 定时任务
schedule.every().day.at("09:00").do(fetch_and_notify)

while True:
    schedule.run_pending()
    time.sleep(1)
EOF

# 6. 创建配置文件
cat > $PROJECT_DIR/config/settings.py <<EOF
GITHUB_API_TOKEN = "your_github_api_token"
NOTIFICATION_CHANNELS = ["email", "slack"]
REPORT_SCHEDULE = "weekly"  # daily or weekly
EOF

# 7. 创建 requirements.txt
cat > $PROJECT_DIR/requirements.txt <<EOF
requests
schedule
smtplib
slack_sdk
apscheduler
EOF

# 8. 创建 .gitignore 文件
cat > $PROJECT_DIR/.gitignore <<EOF
*.pyc
__pycache__/
subscriptions.json
EOF

# 9. 创建 README.md 文件
cat > $PROJECT_DIR/README.md <<EOF
# GitHub Sentinel

GitHub Sentinel 是一款开源工具类 AI Agent，专为开发者和项目管理人员设计，能够定期（每日/每周）自动获取并汇总订阅的 GitHub 仓库最新动态。

## 功能
- 订阅管理
- 获取仓库更新
- 发送通知
- 生成更新报告

## 安装
使用以下命令安装所需依赖：
\`\`\`bash
pip install -r requirements.txt
\`\`\`

## 配置
编辑 \`config/settings.py\` 配置文件，填入 GitHub API Token 和通知设置。

## 使用
运行以下命令启动：
\`\`\`bash
python src/main.py
\`\`\`
EOF

echo "GitHub Sentinel 项目目录结构已创建完成！"

