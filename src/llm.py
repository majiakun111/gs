from openai import OpenAI
import os

class LLM:
    def __init__(self):
        self.client = OpenAI(
            api_key = "21912878364344545321", #模型工厂AppID
            base_url = "https://aigc.sankuai.com/v1/openai/native"
        )  

    #用LLM对Markdown提炼
    def generate_report(self, markdown_content):
        prompt = f"以下是项目的最新进展,根据功能合并同类项,形成一份简报,至少包含: 1)新增功能; 2)主要改进; 3)修复问题; :\n\n{markdown_content}-------------------- \n\n并以中文输出"

        try:
            response = self.client.chat.completions.create(
                model="gpt-4.1",
                messages= [
                    {"role": "system", "content": "You are a helpful assistant that generates formal project reports."},
                    {"role": "user", "content": prompt},
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