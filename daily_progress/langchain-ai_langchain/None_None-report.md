# Project Daily Report

项目简报

本期简报结合近期issue、PR及commit情况，按功能模块归纳整理如下：

1. 新增功能
- 支持OpenAI reasoning summary流式（streaming）输出，提升大模型推理总结实时返回能力。
- 推出独立的langchain-opensearch软件包，便于Opensearch相关能力的独立部署和维护。
- 新增对Perplexity sonar系列模型的provider自动推断，简化模型初始化流程。
- ChatAnthropic现支持URL输入，扩展输入数据形式。
- 集成Compass Labs工具集。
- 标准测试及openai新版支持标准音频输入。
- 集成Galaxia和ChatLLM7，丰富模型生态。
- Feature: 支持波斯语文本处理。

2. 主要改进
- 修复和优化私有成员访问方式，增强代码规范性与兼容性。
- 多处API已添加弃用（deprecated）声明，对HanaDB/HanaTranslator等老旧实现进行废弃并提供新用法。
- 针对OpenAI 4.1、o4、gpt-4.5-preview等新版本模型，完善计费/名称处理等细节。
- 对AzureAISearchRetriever、langchain-singlestore等集成进行细致兼容及说明文档优化。
- text-splitters及相关代码启用更严格的mypy类型检查，提升代码质量。
- 支持多模态（multimodal）内容块的可选字段，提升内容表达与扩展灵活性。
- “split_list_of_docs”函数性能提升。
- 移除重复的OpenAI embedding相关代码。
- 优化了输出结构，提升OpenAI工具消息自定义回退内容的支持。

3. 修复问题
- 修复OpenAI callback在新模型上的计费信息缺失问题。
- 解决llm.ainvoke与llm.invoke追踪不一致（tracing问题）。
- 修复异步索引（async indexing）异常问题。
- 修复openapi接口_resize用例异常。
- 统一、规范了部分代码的类型忽略与类型标注，消除额外类型警告和错误。
- 修复SitemapLoader和URL处理相关Bug，Strip URLs功能到位。
- 修复ChatTongyi结构化输出相关问题。
- 解决OpenAICallbackHandler不支持4.1及o4模型cost信息问题。
- 修正partners: check_imports.py的退出码。
- 解决模块命名空间冲突（如output_parsers中的list命名冲突）。
- 处理Anthropic与GoogleVertex库混用导致的scope error。
- 修复远程恶意邮件注入导致安全风险问题。
- 解决OpenSearch/AWS OSS Filter无法正常工作的问题。

备注：以上内容基于langchain项目最新issue、PR及commit梳理归纳，部分功能变更仍处于合并审批中，实际上线请关注项目发布公告。