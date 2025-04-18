import json
import os

class SubscriptionManager:
    def __init__(self):
        # 使用项目根目录下的 data 目录存储订阅数据
        current_script_path = os.path.abspath(__file__)
        # 2. 获取脚本所在的目录 (e.g., .../your_project_root/src/subscriptions/)
        script_dir = os.path.dirname(current_script_path)
        # 3. 获取父目录 (即 src 目录) (e.g., .../your_project_root/src/)
        parent_dir = os.path.dirname(script_dir)
        # 4. 构建到父目录下 JSON 文件的完整路径
        self.file_path = os.path.join(parent_dir, 'subscriptions.json')       
        self.subscriptions = self.load_subscriptions()
    
    def load_subscriptions(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                return json.load(file)
                
        # 如果文件不存在，创建一个空的订阅列表并保存
        self.subscriptions = []
        self.save_subscriptions()
        return self.subscriptions
    
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
