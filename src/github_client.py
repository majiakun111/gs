# github_client.py
import requests
from datetime import datetime

class GitHubClient:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://api.github.com"

    def _make_request(self, url):
        headers = {'Authorization': f'token {self.token}'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_issues(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/issues"
        return self._make_request(url)

    def get_pull_requests(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/pulls"
        return self._make_request(url)

    def get_commits(self, owner, repo):
        """获取 commits"""
        url = f"{self.base_url}/repos/{owner}/{repo}/commits"
        return self._make_request(url)

    def export_daily_progress(self, owner, repo):
        """从 GitHub 获取 issues, prs, commits 并保存为每日进度的 Markdown 文件"""
        # 获取数据
        issues = self.get_issues(owner, repo)
        prs = self.get_pull_requests(owner, repo)
        commits = self.get_commits(owner, repo)

        # 格式化日期
        date_str = datetime.now().strftime('%Y-%m-%d')
        markdown_file_path = f"{repo}-{date_str}-daily-progress.md"

        # 写入 Markdown 文件
        with open(markdown_file_path, 'w') as file:
            file.write(f"# {repo} Daily Progress - {date_str}\n\n")
            
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
