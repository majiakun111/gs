import openai
import os

class LLM:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    //用LLM对Markdown提炼
    def generate_report(self, issues_prs_summary):
        """生成基于 issues 和 PRs 的正式报告"""
        prompt = f"Please generate a formal project report based on the following issues and pull requests:\n\n{issues_prs_summary}"

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