# Project Daily Report

# Axios 项目进展简报

## 1. 新增功能

- 支持通过配置项忽略绝对 URL，提高请求 URL 管理灵活性（allowAbsoluteUrls）。
- `AxiosHeaders` 新增 `getSetCookie` 方法，可用于获取 set-cookie 响应头。
- 类型定义增强：允许对 Params 属性进行类型化，提升 TypeScript 开发体验。
- 支持 zstd 解压缩功能用于 http 适配器。
- 可为同一个 Axios 实例配置多个 baseURL。
- 支持 Cloudflare Worker 环境。
- 支持自定义响应头返回。
- 优化移除拦截器时使用 Map 替代 Array，增强性能。
- 响应头类型统一为小写，提升兼容性。

## 2. 主要改进

- `fetchOptions` 类型增强，改善自动补全与类型安全，并提升 Next.js 兼容性。
- Axios 构造器实现调整，配置项 config 现可选，提升调用灵活性。
- 内部类型定义及 JSDoc 文档完善，便于二次开发与使用。
- 请求配置（AxiosRequestConfig）类型处理优化，支持 URL 对象，实现更强类型约束。
- 优化 baseURL 与请求 url 的合并与生成逻辑。
- 优化 Safari 浏览器下的网络错误映射。
- 迭代器对象可以作为 set 方法的数据源，用于设置 header。
- 优化工具 utils，在客户端构建中避免导入 crypto 模块，提升构建性能。
- 优化授权头合并逻辑，优先使用请求级别的 Authorization。
- 简化 multipart 请求末尾边界处理，减少冗余数据。
- 代码打包流程调整，确保许可证声明文件不会被 minify 删除。

## 3. 修复问题

- 修复了 Axios 构造方法参数可选相关实现。
- 修复 Set-Cookie 响应头获取存在的问题。
- 修复 allowAbsoluteUrls 类型缺失、传递不完整等相关问题。
- 修复 fetch、xhr、http 适配器未正确传递 allowAbsoluteUrls 配置的问题。
- 修复因 TypeScript 类型定义导致的适配器参数无法自动补全问题。
- 修复 Node >= 20.13.0 时使用 FormData 携带文件无法收到响应的问题。
- 修复请求配置对象 baseURL 未定义情况下路径计算出错的问题。
- 修复 `CanceledError` 在 JSON.stringify 时导致栈溢出的问题。
- 修复 Safari 浏览器请求返回 ERR_NETWORK 状态码映射不准确的问题。
- 修复某些包构建及依赖安全等细节性问题。
- 修复 React Native 包导出及某些环境下 window.location 相关报错。
- 修复多 Headers 处理、响应头归一化等相关问题。

---

如需详细了解各项功能、优化细节或问题处理记录，可参考对应 PR 和 Commit 信息。