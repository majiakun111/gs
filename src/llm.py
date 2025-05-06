from openai import OpenAI
from logger import LOG  # 导入日志模块
import requests
import json

class LLM:
    def __init__(self, config):
        self.config = config;

        if self.config["model_type"] == "openai" : 
            self.client = OpenAI(
                api_key = self.config["openai_api_key"], 
                base_url = self.config["api_url"]
            )  

        # 从TXT文件加载提示信息
        with open("prompts/report_prompt.txt", "r", encoding='utf-8') as file:
            self.system_prompt = file.read()

    #用LLM对Markdown提炼
    def generate_report(self, markdown_content):
        messages=[
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": markdown_content},
        ]

        model_type=self.config['model_type']
        print(model_type)

        if model_type=="openai":
            return self.generate_report_openai(messages)
        elif model_type=="ollama": 
            return self.generate_report_ollama(messages)
        else:
            raise ValueError(f"Unsupported model type: {model_type}")

    def generate_report_openai(self, messages):
        LOG.info("使用 OpenAI GPT 模型开始生成报告。")
        try:
            response = self.client.chat.completions.create(
                model=self.config["model_name"],
                messages=messages,
                stream=False,
                extra_headers={
                    "M-TraceId": "e6Cx1wCdLGzKw2WmaGg0Pdmq8Z26oMQf3wlOkbT1Iv0"
                }
            )
            
            LOG.debug("GPT response: {}", response)
            return response.choices[0].message.content
        except Exception as e:
            LOG.error(f"生成报告时发生错误：{e}")
            raise

    def generate_report_ollama(self, messages):
        LOG.info("使用 Ollama 托管模型服务开始生成报告。")
        try:
            # payload = {
            #     "model": self.config["model_name"], 
            #     "messages": messages,
            #     "stream": False
            # }
            payload = {
                        "model": "llama3.1:latest",
                        "messages": [{"role": "user", "content": "What is the capital of France?"}]
            }
            
            response = requests.post(self.config["api_url"], json=payload)
            LOG.debug("Ollama response: {}", response)

            response_data = response.json()

            # 调试输出查看完整的响应结构
            LOG.debug("Ollama response_data: {}", response_data)
            
            # 直接从响应数据中获取 content
            message_content = response_data.get("message", {}).get("content", None)
            if message_content:
                return message_content  # 返回生成的报告内容
            else:
                LOG.error("无法从响应中提取报告内容。")
                raise ValueError("Invalid response structure from Ollama API")
        except Exception as e:
            LOG.error(f"生成报告时发生错误：{e}")
            raise

if __name__ == '__main__':
    from config import Config  # 导入配置管理类
    config = Config()
    llm = LLM(config.llm)

    markdown_content="""
# Progress for langchain-ai/langchain (2024-08-20 to 2024-08-21)


## Issues Closed in the Last 1 Days
- partners/chroma: release 0.1.3 #25599
- docs: few-shot conceptual guide #25596
- docs: update examples in api ref #25589
"""

    report = llm.generate_report(markdown_content)
    LOG.info(report)