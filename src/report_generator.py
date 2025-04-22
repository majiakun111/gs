from datetime import datetime

class ReportGenerator:
    def __init__(self, llm):
        self.llm = llm
    
    def generate_report(self, markdown_file_path):
        """从 Markdown 文件生成项目报告"""
        try:
            with open(markdown_file_path, 'r') as file:
                content = file.read()

            # 生成报告
            report = self.llm.generate_report(content)

            # 保存报告为 Markdown 文件
            report_file_path = markdown_file_path.replace(".md", "_report.md")
            with open(report_file_path, 'w') as report_file:
                report_file.write(f"# Project Daily Report\n\n{report}")
            
            return report, report_file_path

        except Exception as e:
            print(f"Error generating daily report: {e}")

         