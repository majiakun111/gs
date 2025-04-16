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
    manager.add_subscription("https://github.com/langchain-ai/langchain")
    print(manager.get_subscriptions())
