from datetime import datetime

class ReportGenerator:
    def __init__(self, llm):
        self.llm = llm
    
    def generate_daily_report(self, markdown_file_path):
        """从 Markdown 文件生成项目报告"""
        try:
            with open(markdown_file_path, 'r') as file:
                content = file.read()

            # 生成报告
            report = self.llm.generate_report(content)

            # 保存报告为 Markdown 文件
            report_file_path = markdown_file_path.replace(".md", "-report.md")
            with open(report_file_path, 'w') as report_file:
                report_file.write(f"# Project Daily Report\n\n{report}")
            
            print(f"Report saved as: {report_file_path}")
        except Exception as e:
            print(f"Error generating daily report: {e}")

# 示例用法
if __name__ == "__main__":
    report_generator = ReportGenerator()
    daily_updates = {
        "Hello-World": ["Commit 1", "PR #2 merged"],
        "GitHub-Sentinel": ["Issue #3 opened", "Commit 4"]
    }
    report = report_generator.generate_daily_report(daily_updates)
    print(report)
