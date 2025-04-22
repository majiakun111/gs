import gradio as gr  # 导入gradio库用于创建GUI
from config import Config
from github_client import GitHubClient  # 导入用于GitHub API操作的客户端
from report_generator import ReportGenerator  # 导入报告生成器模块
from llm import LLM  # 导入可能用于处理语言模型的LLM类
from subscription_manager import SubscriptionManager  # 导入订阅管理器
import os


# 创建各个组件的实例
config = Config()
github_client = GitHubClient(config.github_token)
llm = LLM(config.openai_api_key)
report_generator = ReportGenerator(llm)
subscription_manager = SubscriptionManager(config.subscriptions_file)

def export_progress_by_date_range(repo, days):
    # 定义一个函数，用于导出和生成指定时间范围内项目的进展报告
    owner, repo_name = repo.split('/')
    raw_file_path = github_client.export_progress_by_date_range(owner, repo_name, days)  # 导出原始数据文件路径
    report, report_file_path = report_generator.generate_report(raw_file_path)  # 生成并获取报告内容及文件路径
    # 转换为绝对路径
    report_file_path = os.path.abspath(report_file_path)
    
    return report_file_path  #返回报告内容和报告文件路径

demo = gr.Interface(
    fn=export_progress_by_date_range, 
    title="GitHubSentinel",  #设置界面标题
    inputs=[
        gr.Dropdown(
            subscription_manager.list_subscriptions(), label="订阅列表", info="已订阅GitHub项目"
        ),  # 下拉菜单选择订阅的GitHub项目
        gr.Slider(value=2, minimum=1, maximum=7, step=1, label="报告周期", info="生成项目过去一段时间进展，单位：天")
        # 滑动条选择报告的时间范围
    ],
    outputs=[gr.Markdown(), gr.File(label="下载报告")]  # 输出格式：Markdown文本和文件下载
)

if __name__ == "__main__":
    #export_progress_by_date_range("axios/axios", days=5);
    demo.launch(share=True, server_name="0.0.0.0", server_port=10086, debug=True)
    # 可选带有用户认证的启动方式
    # demo.launch(share=True, server_name="0.0.0.0", auth=("django", "1234"))
