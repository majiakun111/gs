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
