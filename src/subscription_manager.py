import json
import os

class SubscriptionManager:
    def __init__(self, subscriptions_file):        
        self.subscriptions_file = subscriptions_file;
        self.subscriptions = self.load_subscriptions()
    
    def load_subscriptions(self):
        if os.path.exists(self.subscriptions_file):
            with open(self.subscriptions_file, "r") as file:
                return json.load(file)
                
        # 如果文件不存在，创建一个空的订阅列表并保存
        self.subscriptions = []
        self.save_subscriptions()
        return self.subscriptions
    
    def save_subscriptions(self):
        with open(self.subscriptions_file, "w") as file:
            json.dump(self.subscriptions, file, indent=4)
    
    def add_subscription(self, repo_url):
        if repo_url not in self.subscriptions:
            self.subscriptions.append(repo_url)
            self.save_subscriptions()
    
    def remove_subscription(self, repo_url):
        if repo_url in self.subscriptions:
            self.subscriptions.remove(repo_url)
            self.save_subscriptions()
    
    def list_subscriptions(self):
        return self.subscriptions
