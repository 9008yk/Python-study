# 第三周：Web 后端 FastAPI

从这周开始，你写的东西不再只是命令行程序，而是可以通过浏览器和网络访问的服务。

## 每日任务

- [x] Day 15：FastAPI 入门，GET / POST 接口
- [x] Day 16：路径参数、查询参数和请求体
- [x] Day 17：SQLite 数据库
- [x] Day 18（后端版）：response_model、状态码和 tags
- [x] Day 19：用户注册、登录和 JWT 认证
- [ ] Day 20~21：综合项目：待办绑定用户

## 完成标准

- 能启动 FastAPI 服务，并理解接口、请求和响应
- 能用浏览器打开 `/docs` 调试接口
- 能用 pytest 测试接口
- 能把数据存进 SQLite 而不是内存列表

## 部署

本地生产模式启动：

```powershell
.venv\Scripts\Activate.ps1
python -m uvicorn week03.main:app --host 0.0.0.0 --port 8000
```

通过环境变量配置密钥和数据库位置，参考 `.env.example`。

Docker 启动：

```powershell
docker compose up --build
```

启动后访问 http://localhost:8000/docs。
