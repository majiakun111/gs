import requests 
import os
from datetime import datetime, date, timedelta  # 导入日期处理模块
class GitHubClient:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://api.github.com"
        self.headers = {"Authorization": f"token {self.token}"}

    def get_issues(self, owner, repo, since=None, until=None):
        url = f"{self.base_url}/repos/{owner}/{repo}/issues"
        params = {
            'state': 'closed',  # 仅获取已关闭的问题
            'since': since,
            'until': until
        }
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_pull_requests(self, owner, repo, since=None, until=None):
        url = f"{self.base_url}/repos/{owner}/{repo}/pulls"
        params = {
            'state': 'closed',  # 仅获取已合并的拉取请求
            'since': since,
            'until': until
        }
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_commits(self, owner, repo, since=None, until=None):
        url = f"{self.base_url}/repos/{owner}/{repo}/commits"
        params = {
            'since': since,
            'until': until
        }
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()


    def export_progress(self, owner, repo):
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
        markdown_file_path = f"{directory}.md"

        # 写入 Markdown 文件
        with open(markdown_file_path, 'w') as file:
            file.write(f"# {repo} Daily Progress.\n")
            
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

    def export_progress_by_date_range(self, owner, repo, days):
        today = date.today()  # 获取当前日期
        since = today - timedelta(days=days)  # 计算开始日期

        """从 GitHub 获取 issues, prs, commits 并保存为每日进度的 Markdown 文件"""
        # 获取数据
        issues = self.get_issues(owner, repo, since=since.isoformat(), until=today.isoformat())
        prs = self.get_pull_requests(owner, repo, since=since.isoformat(), until=today.isoformat())
        commits = self.get_commits(owner, repo, since=since.isoformat(), until=today.isoformat())

        # 格式化文件路径
        repo_dir = f"daily_progress/{owner}_{repo}"
        # 确保目录存在
        os.makedirs(repo_dir, exist_ok=True)
        date_str = f"{since}_to_{today}"
        markdown_file_path = os.path.join(repo_dir, f'{date_str}.md')  # 构建文件路径

        # 写入 Markdown 文件
        with open(markdown_file_path, 'w') as file:
            file.write(f"# {repo} Daily Progress - {since} to {today}\n\n")
            
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

        print(f"Exported time-range progress to {markdown_file_path}")
        return markdown_file_path