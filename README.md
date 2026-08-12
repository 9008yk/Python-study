# Python 学习项目

这是你的 Python 学习仓库，所有练习和小项目都会放在这里。

## 目录结构

```text
Python-study/
├── hello.py          # 环境验证脚本
├── README.md         # 仓库说明
└── week01/           # 第一周练习
    ├── README.md     # 本周任务清单
    └── exercises.py  # 练习入口文件
```

之后每周建一个新的目录，例如 `week02/`、`week03/`，小项目可以放在 `projects/` 下。

## 如何运行

先在项目目录激活虚拟环境：

```powershell
cd D:\vue3-program\Python-study
.venv\Scripts\Activate.ps1
```

然后运行脚本：

```powershell
python hello.py
```

## 学习路线概览

1. 基础语法：变量、字符串、条件、循环、列表、字典、函数（第 1~3 周）
2. 进阶语法：类、异常、文件读写、模块、pip、Git（第 4~6 周）
3. 小项目：CLI 工具、数据处理、爬虫或 Web 后端（第 7~12 周）
4. 选定方向深入：数据分析 / AI、Web 开发、自动化

## 推送到 GitHub

1. 在 GitHub 网页上新建一个仓库，名字建议用 `python-study`，不要勾选自动生成 README
2. 复制仓库地址（形如 `https://github.com/<你的用户名>/python-study.git`）
3. 在本目录执行：

```powershell
git remote add origin <仓库地址>
git push -u origin main
```

之后每次完成练习都可以提交：

```powershell
git add .
git commit -m "描述这次改了什么"
git push
```
