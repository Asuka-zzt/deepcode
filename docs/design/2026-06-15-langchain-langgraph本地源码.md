# LangChain / LangGraph 本地源码接入

## 目标

将 LangChain 和 LangGraph 的完整上游仓库纳入本地开发环境，让 DeepCode
直接加载可编辑源码，为后续修改框架内部实现、调试和跟踪上游更新做准备。

## 决策

采用 Git submodule 管理两个上游仓库，并通过 uv 的本地 editable source
接入运行环境：

| 子模块 | 固定版本 | 本地包 |
| --- | --- | --- |
| `vendor/langchain` | commit `51578289b` | `langchain 1.3.9`、`langchain-core 1.4.7` |
| `vendor/langgraph` | tag `1.2.5` / commit `7ab79f9f3` | `langgraph`、`checkpoint`、`prebuilt`、`sdk` |

LangChain 固定到 `langchain-core==1.4.7` 标签对应的提交，而不是稍早的
`langchain==1.3.9` 标签提交，因为 LangGraph 1.2.5 要求
`langchain-core>=1.4.7`。该提交中的 LangChain 主包版本仍为 1.3.9。

## 依赖路径

根项目的 `pyproject.toml` 使用 `[tool.uv.sources]` 将以下包映射到源码：

- `langchain`
- `langchain-core`
- `langgraph`
- `langgraph-checkpoint`
- `langgraph-prebuilt`
- `langgraph-sdk`

这些包以 editable 模式安装，修改对应源码后无需重新构建 wheel。

## 开发流程

1. 初始化环境：`git submodule update --init --recursive && uv sync`
2. 在需要修改的子模块内配置个人 fork，并创建开发分支。
3. 在子模块仓库内提交框架改动。
4. 在 DeepCode 主仓库提交新的 submodule commit 指针。
5. 分别运行 DeepCode 测试和受影响的上游包测试。

## 权衡和风险

- 主仓库只记录子模块提交指针，克隆时必须初始化子模块。
- 官方仓库通常没有直接推送权限，开始二次开发前需要切换到个人或团队 fork。
- 同时修改跨仓库接口时，要保持 LangChain、LangGraph 与 DeepCode 三方提交的兼容关系。
- 根项目 lint 排除 `vendor/`；上游源码应使用各自仓库的 lint 和测试配置验证。
