# 文件网盘系统

一个现代化的本地文件网盘系统，支持文件上传、下载、列表展示和删除功能。

## 功能特性

- 📤 **文件上传** - 支持拖拽上传和点击选择，支持批量上传
- 📥 **文件下载** - 一键下载服务器上的文件
- 📋 **文件列表** - 清晰展示所有文件，显示文件大小和修改时间
- 🗑️ **文件删除** - 安全删除不需要的文件
- 🎨 **现代界面** - 采用玻璃态设计，视觉效果出色
- 📱 **响应式设计** - 支持各种屏幕尺寸

## 技术栈

- **后端**: Python Flask
- **前端**: HTML5, CSS3, JavaScript
- **设计**: 玻璃态设计风格

## 安装步骤

### 1. 安装依赖

```bash
git clone https://github.com/LiMin1314520/file-server.git
cd file-server
pip install -r requirements.txt
```

### 2. 启动服务器

```bash
python app.py
```

### 3. 访问应用

在浏览器中打开: `http://localhost:5000`

## 目录结构

```
file-server/
├── app.py              # Flask后端服务器
├── requirements.txt    # Python依赖
├── uploads/            # 文件存储目录（自动创建）
├── templates/          # HTML模板
│   └── index.html
└── static/             # 静态资源
    ├── css/
    │   └── style.css
    └── js/
        └── app.js
```

## API接口

### 获取文件列表
```
GET /api/files
```

### 上传文件
```
POST /api/upload
Content-Type: multipart/form-data
```

### 下载文件
```
GET /api/download/<filename>
```

### 删除文件
```
DELETE /api/delete/<filename>
```

## 配置说明

在 `app.py` 中可以修改以下配置：

- `UPLOAD_FOLDER`: 文件上传目录（默认: 'uploads'）
- `MAX_CONTENT_LENGTH`: 最大上传文件大小（默认: 100MB）
- `host`: 服务器监听地址（默认: '0.0.0.0'）
- `port`: 服务器端口（默认: 5000）

## 注意事项

- 文件上传大小限制为100MB，可在配置中修改
- 上传的文件存储在 `uploads` 目录中
- 删除文件操作不可恢复，请谨慎操作
- 服务器默认监听所有网络接口，请注意安全

## 安全建议

- 在生产环境中，建议添加用户认证
- 设置适当的文件类型白名单
- 限制上传文件的执行权限
- 使用HTTPS协议保护数据传输

## 许可证

MIT License
