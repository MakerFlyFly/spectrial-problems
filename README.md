# SpecTrial Problems

使用 AI 工具，在真实开源仓库里练习理解问题、修改代码与工程交付。

本仓库公开题目、固定版本、环境定义、完整评测测试及独立复现工具，不依赖 SpecTrial 的私有业务后端。

## 题库

当前 Release 包含 **43 道**已通过基线与两次参考补丁验证的题目。

| 题目 | 仓库 | 难度 | 固定测试 |
| --- | --- | --- | --- |
| [在正确数据库上重命名内容类型](tasks/django__django-11066/problem.md) | django/django | 入门 | 4 |
| [让模板字符串渲染遵循自动转义设置](tasks/django__django-11119/problem.md) | django/django | 入门 | 8 |
| [为 dbshell 支持 PostgreSQL 客户端证书](tasks/django__django-11239/problem.md) | django/django | 入门 | 6 |
| [避免重复构造 URL 解析器](tasks/django__django-11333/problem.md) | django/django | 进阶 | 3 |
| [修复视图文档字符串的渲染错误](tasks/django__django-12155/problem.md) | django/django | 进阶 | 7 |
| [让消息级别标签随配置覆盖更新](tasks/django__django-15127/problem.md) | django/django | 入门 | 2 |
| [修正 PostgreSQL dbshell 的参数顺序](tasks/django__django-15851/problem.md) | django/django | 入门 | 9 |
| [让另存为新对象遵循新增权限](tasks/django__django-16527/problem.md) | django/django | 进阶 | 7 |
| [修复多条件异或查询的奇偶语义](tasks/django__django-16901/problem.md) | django/django | 进阶 | 7 |
| [让后台内联表单使用 UUID 默认值](tasks/django__django-16950/problem.md) | django/django | 进阶 | 4 |
| [为 Blueprint 增加空名称校验](tasks/pallets__flask-5014/problem.md) | pallets/flask | 入门 | 60 |
| [修复请求中不恰当的 Content-Length](tasks/psf__requests-1142/problem.md) | psf/requests | 入门 | 6 |
| [修复代理地址中的认证信息解析](tasks/psf__requests-6028/problem.md) | psf/requests | 进阶 | 187 |
| [让零相似行数阈值关闭重复代码检查](tasks/pylint-dev__pylint-4970/problem.md) | pylint-dev/pylint | 入门 | 18 |
| [规范短格式详细输出选项的参数](tasks/pylint-dev__pylint-6386/problem.md) | pylint-dev/pylint | 进阶 | 8 |
| [修复容器中自动选择工作进程数失败](tasks/pylint-dev__pylint-6903/problem.md) | pylint-dev/pylint | 入门 | 9 |
| [让递归扫描遵循忽略路径配置](tasks/pylint-dev__pylint-7080/problem.md) | pylint-dev/pylint | 进阶 | 121 |
| [修复日志清空后的状态不一致](tasks/pytest-dev__pytest-10051/problem.md) | pytest-dev/pytest | 进阶 | 16 |
| [修复跳过 unittest 类时的调试清理流程](tasks/pytest-dev__pytest-10081/problem.md) | pytest-dev/pytest | 入门 | 64 |
| [修复替换数组对象时的测试收集异常](tasks/pytest-dev__pytest-5631/problem.md) | pytest-dev/pytest | 进阶 | 16 |
| [修复 pastebin 功能的语法高亮类型](tasks/pytest-dev__pytest-5809/problem.md) | pytest-dev/pytest | 入门 | 4 |
| [修复 Windows 路径大小写导致的配置导入失败](tasks/pytest-dev__pytest-5840/problem.md) | pytest-dev/pytest | 进阶 | 53 |
| [保留测试报告标题中的参数表示](tasks/pytest-dev__pytest-6202/problem.md) | pytest-dev/pytest | 入门 | 73 |
| [修复展示字节参数时的 BytesWarning](tasks/pytest-dev__pytest-7205/problem.md) | pytest-dev/pytest | 入门 | 26 |
| [修复调试模式下跳过测试的清理流程](tasks/pytest-dev__pytest-7236/problem.md) | pytest-dev/pytest | 进阶 | 52 |
| [修复调试版 Python 下的标记表达式崩溃](tasks/pytest-dev__pytest-7324/problem.md) | pytest-dev/pytest | 进阶 | 61 |
| [修复 runxfail 下跳过测试的位置报告](tasks/pytest-dev__pytest-7432/problem.md) | pytest-dev/pytest | 入门 | 78 |
| [在测试结束后恢复 caplog 日志级别](tasks/pytest-dev__pytest-7571/problem.md) | pytest-dev/pytest | 进阶 | 15 |
| [恢复符号链接目录中的测试收集](tasks/pytest-dev__pytest-7982/problem.md) | pytest-dev/pytest | 入门 | 79 |
| [保持 unittest 类级 fixture 的私有性](tasks/pytest-dev__pytest-8399/problem.md) | pytest-dev/pytest | 进阶 | 60 |
| [去除国际化消息的重复源位置](tasks/sphinx-doc__sphinx-10466/problem.md) | sphinx-doc/sphinx | 进阶 | 7 |
| [修复继承关系图 SVG 中的链接](tasks/sphinx-doc__sphinx-10614/problem.md) | sphinx-doc/sphinx | 进阶 | 6 |
| [修复 rst_prolog 导致顶层标题丢失](tasks/sphinx-doc__sphinx-11445/problem.md) | sphinx-doc/sphinx | 进阶 | 10 |
| [让 source-read 事件修改包含文件内容](tasks/sphinx-doc__sphinx-11510/problem.md) | sphinx-doc/sphinx | 挑战 | 9 |
| [修复泛型类在自动文档模拟环境中的异常](tasks/sphinx-doc__sphinx-7889/problem.md) | sphinx-doc/sphinx | 入门 | 6 |
| [支持为自动文档指定私有成员名单](tasks/sphinx-doc__sphinx-8035/problem.md) | sphinx-doc/sphinx | 进阶 | 3 |
| [补全继承属性的自动文档](tasks/sphinx-doc__sphinx-8548/problem.md) | sphinx-doc/sphinx | 挑战 | 6 |
| [修复变量的公开成员元数据识别](tasks/sphinx-doc__sphinx-8593/problem.md) | sphinx-doc/sphinx | 进阶 | 3 |
| [禁用 EPUB 时不再生成源码查看页](tasks/sphinx-doc__sphinx-8721/problem.md) | sphinx-doc/sphinx | 入门 | 4 |
| [修复快速建站遇到已有配置时无法退出](tasks/sphinx-doc__sphinx-9320/problem.md) | sphinx-doc/sphinx | 入门 | 10 |
| [支持向量与零的加法](tasks/sympy__sympy-14711/problem.md) | sympy/sympy | 入门 | 3 |
| [修复希腊字母下标的 Unicode 排版](tasks/sympy__sympy-20916/problem.md) | sympy/sympy | 入门 | 2 |
| [修复置换群同态检查](tasks/sympy__sympy-24443/problem.md) | sympy/sympy | 进阶 | 2 |

来源为 [SWE-bench Verified](https://huggingface.co/datasets/SWE-bench/SWE-bench_Verified)，数据 revision 固定为 `78f471bf655a3137b2e8a75af1501690ec009ec3`。每个任务记录原仓库、完整 `base_commit`、容器镜像 digest、来源 ID 与资产摘要。

题目均须通过干净基线和参考补丁验证后才在平台发布。原始基准中依赖外部网络、与隔离环境不兼容的实例不属于本批题目；保留完整权威测试，不通过删除失败用例来凑分。

## 开始练习

本地工具需要 Python 3.10+、Git 和 Docker。题目的历史依赖由固定镜像提供，不要求本地 Python 与旧仓库使用相同版本。

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

保留 v1 解析器兼容历史题目，v2 支持 Django、Sphinx、Pylint 等 Python 仓库。判分要求所有 `FAIL_TO_PASS` 和 `PASS_TO_PASS` 用例均通过。复现解析器来源和许可见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。公开的参考解答在原始数据集中可查，因此这些题目用于自主练习。

## 贡献题目

```bash
python -m pip install jsonschema==4.26.0
python tools/validate.py
```

通过 PR 提交新题包或版本。包括来源、许可证、可复现环境、入门说明、完整测试与内容校验。PR CI 只校验公开包，不接触私有平台凭据；维护者在可信环境完成基线和参考补丁验收后决定发布。

## 许可

新增脚本、协议及元数据使用 MIT。SWE-bench 资产保留其来源与署名；原仓库代码和测试沿用对应 `repo-license.txt`，本仓库不对其统一重新许可。题库不包含学生提交、平台凭据或私有业务后端。

Sphinx 题包中的 `upstream-eval.sh` 保存原始脚本，`eval.sh` 仅增加 `-rA` 完整结果报告选项，不改变测试选集或断言。基线和两次参考补丁的验收摘要见 `validation-summary.json`。
