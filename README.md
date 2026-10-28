# SpecTrial Problems

使用 AI 工具，在真实开源仓库里练习理解问题、修改代码与工程交付。

本仓库公开题目、固定版本、环境定义、完整评测测试及独立复现工具，不依赖 SpecTrial 的私有业务后端。

## 首批题目

| 题目 | 仓库 | 练习重点 |
| --- | --- | --- |
| `pallets__flask-5014` | Flask | Blueprint 初始化与输入校验 |
| `psf__requests-6028` | Requests | 代理 URL 与认证信息解析 |
| `pytest-dev__pytest-10051` | Pytest | 日志捕获、可变对象与状态一致性 |

来源为 [SWE-bench Verified](https://huggingface.co/datasets/SWE-bench/SWE-bench_Verified)，数据 revision 固定为 `78f471bf655a3137b2e8a75af1501690ec009ec3`。每个任务记录原仓库、完整 `base_commit`、容器镜像 digest、来源 ID 与资产摘要。

题目均须通过干净基线和参考补丁验证后才在平台发布。原始基准中依赖外部网络、与隔离环境不兼容的实例不属于本批题目；保留完整权威测试，不通过删除失败用例来凑分。

## 开始练习

1. 打开 `tasks/TASK_ID/task.json`，按 `guide.setup` 克隆并检出题目基线。
2. 阅读 `problem.md`、中文入门说明及 `guide.entry_points`，在本地使用熟悉的 IDE 与 AI 工具开发。
3. 仅修改 `allowed_paths` 中的源代码。新增源文件先执行 `git add`。
4. 使用导出脚本生成 UTF-8 Git 补丁：

```bash
python tools/export_patch.py --task pallets__flask-5014 --repo /path/to/flask --output solution.patch
```

该命令包含相对指定基线的已暂存和未暂存修改，检查未跟踪的新源文件，并避免 PowerShell 重定向导致的 UTF-16 编码问题。它不会替你修改 Git index。

安装 Docker 后可在干净环境中运行固定测试：

```bash
python tools/reproduce.py --task pallets__flask-5014 --patch solution.patch
```

镜像先拉取，再断网执行；不需要平台账号。工具恢复到准确代码基线，应用补丁，执行题包内 `eval.sh`，使用固定 F2P/P2P 列表判断结果。全部指定测试通过时退出码为 0。

Windows 推荐使用 WSL2 或 Docker Desktop。Apple Silicon 使用 `linux/amd64` 模拟执行，首次拉取镜像需要时间和磁盘空间。开发环境可联网使用 AI；平台评测不提供网络与模型凭据。

## TaskPackage v1

```text
schema/task-v1.schema.json
tasks/TASK_ID/
  task.json             # 版本、来源、允许修改目录、镜像及测试列表
  problem.md            # 原始英文问题报告
  test.patch            # 权威测试补丁
  eval.sh               # 原始评测脚本
  repo-license.txt      # 对应仓库版本的许可证
tools/                  # 校验、补丁导出与独立复现工具
```

同一 `task_id@task_version` 不可变。修改题面、环境、测试或元数据时增加版本。Release 提供源码归档与 SHA-256 清单，平台消费固定发布版本，不跟踪运行中的主分支。

目前支持三个题目使用的 pytest 解析器变体，判分要求所有 `FAIL_TO_PASS` 和 `PASS_TO_PASS` 用例均通过。复现解析器来源和许可见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。公开的参考解答在原始数据集中可查，因此这些题目用于自主练习。

## 贡献题目

```bash
python -m pip install jsonschema==4.26.0
python tools/validate.py
```

通过 PR 提交新题包或版本。包括来源、许可证、可复现环境、入门说明、完整测试与内容校验。PR CI 只校验公开包，不接触私有平台凭据；维护者在可信环境完成基线和参考补丁验收后决定发布。

## 许可

新增脚本、协议及元数据使用 MIT。SWE-bench 资产保留其来源与署名；原仓库代码和测试沿用对应 `repo-license.txt`，本仓库不对其统一重新许可。题库不包含学生提交、平台凭据或私有业务后端。
