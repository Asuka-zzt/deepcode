# deepcode

这是一个参考claude和codex打造的coding agent,编程语言使用python,主要使用langchain和langgraph作为开发框架,并在langchain,langgraph上进行二次开发.

## 本地开发

项目通过 Git submodule 引入 LangChain 和 LangGraph 源码，并由 uv 以 editable
模式安装。首次克隆时执行：

```bash
git clone --recurse-submodules <repository-url>
cd deepcode
uv sync
```

已有仓库更新后执行：

```bash
git submodule update --init --recursive
uv sync
```

源码目录：

- `vendor/langchain`：固定到包含 `langchain 1.3.9` 和 `langchain-core 1.4.7` 的提交。
- `vendor/langgraph`：固定到 `langgraph 1.2.5`。

二次开发前应在对应子模块中创建分支并配置自己的 fork。子模块内的源码提交与
DeepCode 主仓库对子模块版本指针的提交需要分别完成。
