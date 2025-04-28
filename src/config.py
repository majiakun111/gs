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


import json
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

        self.load_config()

    
    def load_config(self):
        # 尝试从环境变量获取配置或使用 config.json 文件中的配置作为回退
        with open('config.json', 'r') as f:
            config = json.load(f)
            
            # 初始化电子邮件设置
            self.email = config.get('email', {})
            # 使用环境变量中的授权码
            self.email['password'] = os.getenv('SINA_EMAIL_AUTH_PASSWORD') 

            self.subscriptions_file = config.get('subscriptions_file')
            # 默认每天执行
            self.freq_days = config.get('github_progress_frequency_days', 1)
            # 默认早上8点更新 (操作系统默认时区是 UTC +0，08点刚好对应北京时间凌晨12点)
            self.exec_time = config.get('github_progress_execution_time', "08:00") 