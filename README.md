# 文件网盘系统

一个基于 Flask 的私有云文件存储系统，支持用户注册登录、文件上传、下载、列表展示和删除功能。每个用户拥有独立的存储空间。

## 功能特性

### 用户管理
- 🔐 **用户注册** - 支持新用户注册，密码加密存储
- 🔑 **用户登录** - 安全的登录认证系统
- 🚪 **用户登出** - 一键安全登出

### 文件管理
- 📤 **文件上传** - 支持拖拽上传和点击选择，支持批量上传
- 📥 **文件下载** - 一键下载存储的文件
- 📋 **文件列表** - 清晰展示所有文件，显示文件大小和修改时间
- 🗑️ **文件删除** - 安全删除不需要的文件
- 📁 **用户隔离** - 每个用户拥有独立的存储空间，互不干扰

### 系统特性
- 💾 **持久化存储** - 文件存储在服务器本地磁盘
- 🎨 **现代界面** - 采用玻璃态设计，视觉效果出色
- 📱 **响应式设计** - 支持各种屏幕尺寸
- 🔒 **安全认证** - 基于 Flask-Login 的用户认证系统
- 📊 **文件统计** - 实时显示文件数量和存储信息

## 技术栈

- **后端框架**: Flask 3.0.0
- **用户认证**: Flask-Login 0.6.3
- **跨域支持**: Flask-CORS 4.0.0
- **密码加密**: Werkzeug 3.0.1
- **前端**: HTML5, CSS3, JavaScript (ES6+)
- **设计风格**: 玻璃态设计

## 快速开始

### 环境要求

- Python 3.7+
- pip 包管理器

### 安装步骤

1. **克隆项目**
```bash
git clone https://github.com/LiMin1314520/file-server.git
cd file-server
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **启动服务器**
```bash
python app.py
```

4. **访问应用**

打开浏览器访问: `http://localhost:5000`

### 默认账户

系统会自动创建默认管理员账户：
- 用户名: `admin`
- 密码: `admin123`

**⚠️ 生产环境请务必修改默认密码！**

## 目录结构

```
file-server/
├── app.py              # Flask 应用主程序
├── requirements.txt    # Python 依赖
├── users.json          # 用户数据存储
├── uploads/            # 文件上传目录
│   └── {username}/     # 用户独立存储空间
├── templates/          # HTML 模板
│   ├── index.html      # 主页面
│   ├── login.html      # 登录页面
│   └── register.html   # 注册页面
├── static/             # 静态资源
│   ├── css/
│   │   └── style.css   # 样式文件
│   └── js/
│       └── app.js      # 前端逻辑
├── README.md           # 项目说明
└── LICENSE             # 许可证
```

## API 接口

### 用户认证

| 接口 | 方法 | 说明 |
|------|------|------|
| `/api/register` | POST | 用户注册 |
| `/api/login` | POST | 用户登录 |
| `/api/logout` | POST | 用户登出 |
| `/api/check-login` | GET | 检查登录状态 |

### 文件管理

| 接口 | 方法 | 说明 |
|------|------|------|
| `/api/files` | GET | 获取文件列表 |
| `/api/upload` | POST | 上传文件 |
| `/api/download/<filename>` | GET | 下载文件 |
| `/api/delete/<filename>` | DELETE | 删除文件 |
| `/api/file-info/<filename>` | GET | 获取文件详情 |

## 配置说明

在 `app.py` 中可以修改以下配置：

```python
app.secret_key = 'your-secret-key-change-this-in-production'  # 会话密钥
app.config['UPLOAD_FOLDER'] = 'uploads'                      # 上传目录
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024         # 最大文件大小 (100MB)
```

## 安全建议

1. **修改密钥**: 生产环境请修改 `app.secret_key`
2. **修改默认密码**: 首次登录后立即修改管理员密码
3. **HTTPS**: 生产环境建议使用 HTTPS
4. **文件验证**: 建议添加文件类型验证和病毒扫描
5. **备份**: 定期备份 `users.json` 和 `uploads/` 目录

## 注意事项

### 存储限制

- 单文件最大上传: 100MB (可在配置中修改)
- 存储空间: 受服务器磁盘空间限制

### 浏览器兼容性

支持所有现代浏览器：
- Chrome 60+
- Firefox 60+
- Safari 12+
- Edge 79+

### 数据安全

- 删除文件操作不可恢复，请谨慎操作
- 建议定期备份重要文件
- 用户数据存储在 `users.json` 中

## 常见问题

### Q: 文件存储在哪里？
A: 文件存储在服务器本地的 `uploads/{username}/` 目录中。

### Q: 能在不同设备间同步文件吗？
A: 需要配置服务器公网访问或内网穿透，设备间通过服务器访问同一账户即可。

### Q: 如何备份文件？
A: 定期备份 `uploads/` 目录和 `users.json` 文件。

### Q: 忘记密码怎么办？
A: 管理员可以编辑 `users.json` 文件重置用户密码哈希值。

### Q: 如何修改上传文件大小限制？
A: 修改 `app.py` 中的 `MAX_CONTENT_LENGTH` 配置。

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

## 更新日志

- 2026-03-01: 添加用户注册登录功能，实现用户隔离存储