import os

class Config:
    def __init__(self):
        # 从环境变量获取GitHub Token
        self.github_token = os.getenv('GITHUB_TOKEN')
        if not self.github_token:
            raise ValueError("GITHUB_TOKEN environment variable is not set")

        self.openai_api_key = os.getenv("OPENAI_API_KEY") #模型工厂AppID
        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")

        self.subscriptions_file = "subscriptions.json";
        self.update_interval = 24 * 60 * 60;  # 默认24小时