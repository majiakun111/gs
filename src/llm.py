from openai import OpenAI
import os

class LLM:
    def __init__(self, api_key):
        self.client = OpenAI(
            api_key = api_key, 
            base_url = "https://aigc.sankuai.com/v1/openai/native"
        )  

        # 从TXT文件加载提示信息
        with open("prompts/report_prompt.txt", "r", encoding='utf-8') as file:
            self.system_prompt = file.read()

    #用LLM对Markdown提炼
    def generate_report(self, markdown_content):
        try:
            response = self.client.chat.completions.create(
                model="gpt-4.1",
                messages= [
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": markdown_content},
                ],
                stream=False,
                extra_headers={
                    "M-TraceId": "e6Cx1wCdLGzKw2WmaGg0Pdmq8Z26oMQf3wlOkbT1Iv0"
                }
            )
            
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating report: {e}")
            return ""