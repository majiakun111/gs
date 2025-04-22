# GitHub Sentinel

GitHub Sentinel 是一款开源工具类 AI Agent，专为开发者和项目管理人员设计，能够定期（每日/每周）自动获取并汇总订阅的 GitHub 仓库最新动态。

## 功能
- 订阅管理
- 获取仓库更新
- 发送通知
- 生成更新报告

## 安装
使用以下命令安装所需依赖：
```bash
pip install -r requirements.txt
```

## 配置
编辑 `config.py` 配置文件，填入 GitHub API Token 和OpenAI Key设置。

## 使用
运行以下命令启动：
```bash
python src/main.py
```
