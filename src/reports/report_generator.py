from datetime import datetime

class ReportGenerator:
    def __init__(self):
        self.reports = []
    
    def generate_report(self, repo_name, updates):
        report = {
            "repo_name": repo_name,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updates": updates
        }
        self.reports.append(report)
    
    def generate_daily_report(self, updates_by_repo):
        for repo_name, updates in updates_by_repo.items():
            self.generate_report(repo_name, updates)
        return self.reports
    
    def generate_weekly_report(self, updates_by_repo):
        for repo_name, updates in updates_by_repo.items():
            self.generate_report(repo_name, updates)
        return self.reports

# 示例用法
if __name__ == "__main__":
    report_generator = ReportGenerator()
    daily_updates = {
        "Hello-World": ["Commit 1", "PR #2 merged"],
        "GitHub-Sentinel": ["Issue #3 opened", "Commit 4"]
    }
    report = report_generator.generate_daily_report(daily_updates)
    print(report)
