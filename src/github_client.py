import requests 
import os
from datetime import datetime

class GitHubClient:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://api.github.com"
        self.headers = {"Authorization": f"token {self.token}"}

    def get_issues(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/issues"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching issues for {repo}: {response.status_code} {response.text}")

    def get_pull_requests(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/pulls"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching pull requests for {repo}: {response.status_code} {response.text}")

    def get_commits(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/commits"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching commits for {repo}: {response.status_code} {response.text}")

    def export_daily_progress(self, owner, repo, since_day=None, until_day=None):
        """从 GitHub 获取 issues, prs, commits 并保存为每日进度的 Markdown 文件"""
        # 获取数据
        issues = self.get_issues(owner, repo)
        prs = self.get_pull_requests(owner, repo)
        commits = self.get_commits(owner, repo)

        # 格式化文件路径
        date_str = datetime.now().strftime('%Y-%m-%d')
        directory = f"daily_progress/{owner}_{repo}"

        # 确保目录存在
        os.makedirs(directory, exist_ok=True)

        # 使用 since_day 和 until_day 来命名文件
        markdown_file_path = f"{directory}/{since_day}_{until_day}.md"

        # 写入 Markdown 文件
        with open(markdown_file_path, 'w') as file:
            file.write(f"# {repo} Daily Progress - {since_day} to {until_day}\n\n")
            
            # 导出 Issues
            file.write("## Issues\n")
            if not issues:
                file.write("No new issues today.\n")
            else:
                for issue in issues:
                    file.write(f"- {issue['title']} ({issue['state']})\n")

            # 导出 Pull Requests
            file.write("\n## Pull Requests\n")
            if not prs:
                file.write("No new pull requests today.\n")
            else:
                for pr in prs:
                    file.write(f"- {pr['title']} ({pr['state']})\n")

            # 导出 Commits
            file.write("\n## Commits\n")
            if not commits:
                file.write("No new commits today.\n")
            else:
                for commit in commits:
                    file.write(f"- {commit['commit']['message']} by {commit['commit']['author']['name']}\n")

        print(f"Daily progress exported to {markdown_file_path}")
        return markdown_file_path