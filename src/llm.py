import openai
import os

class LLM:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    #用LLM对Markdown提炼
    def generate_report(self, issues_prs_summary):
        """生成基于 issues 和 PRs 的正式报告"""
        prompt = f"以下是项目的最新进展,根据功能合并同类项,形成一份简报,至少包含: 1)新增功能; 2)主要改进; 3)修复问题; :\n\n{markdown_content}, 并以中文输出"

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that generates formal project reports."},
                    {"role": "user", "content": prompt},
                ]
            )
            report = response['choices'][0]['message']['content']
            return report
        except Exception as e:
            print(f"Error generating report: {e}")
            return ""