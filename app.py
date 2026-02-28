from flask import Flask, render_template, request, send_file, jsonify
from flask_cors import CORS
import os
import datetime
import mimetypes

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# 配置上传文件夹
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 限制上传文件最大100MB


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/files', methods=['GET'])
def list_files():
    """获取文件列表"""
    try:
        files = []
        for filename in os.listdir(app.config['UPLOAD_FOLDER']):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            if os.path.isfile(filepath):
                stat = os.stat(filepath)
                file_info = {
                    'name': filename,
                    'size': stat.st_size,
                    'modified': datetime.datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                    'type': mimetypes.guess_type(filename)[0] or 'application/octet-stream'
                }
                files.append(file_info)
        
        # 按修改时间降序排序
        files.sort(key=lambda x: x['modified'], reverse=True)
        return jsonify({'success': True, 'files': files})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/upload', methods=['POST'])
def upload_file():
    """上传文件"""
    try:
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': '没有文件'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'success': False, 'error': '文件名为空'}), 400
        
        # 保存文件
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # 如果文件已存在，添加时间戳
        if os.path.exists(filepath):
            name, ext = os.path.splitext(filename)
            filename = f"{name}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}{ext}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        file.save(filepath)
        
        return jsonify({
            'success': True,
            'message': '文件上传成功',
            'filename': filename
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/download/<filename>', methods=['GET'])
def download_file(filename):
    """下载文件"""
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if not os.path.exists(filepath):
            return jsonify({'success': False, 'error': '文件不存在'}), 404
        
        return send_file(filepath, as_attachment=True, download_name=filename)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    """删除文件"""
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if not os.path.exists(filepath):
            return jsonify({'success': False, 'error': '文件不存在'}), 404
        
        os.remove(filepath)
        return jsonify({'success': True, 'message': '文件删除成功'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/file-info/<filename>', methods=['GET'])
def file_info(filename):
    """获取文件详细信息"""
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if not os.path.exists(filepath):
            return jsonify({'success': False, 'error': '文件不存在'}), 404
        
        stat = os.stat(filepath)
        file_info = {
            'name': filename,
            'size': stat.st_size,
            'size_human': format_size(stat.st_size),
            'modified': datetime.datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
            'type': mimetypes.guess_type(filename)[0] or 'application/octet-stream'
        }
        return jsonify({'success': True, 'file': file_info})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


def format_size(size):
    """格式化文件大小"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} TB"


if __name__ == '__main__':
    print("=" * 50)
    print("文件网盘服务器已启动")
    print("=" * 50)
    print(f"访问地址: http://localhost:5000")
    print(f"上传目录: {os.path.abspath(UPLOAD_FOLDER)}")
    print("=" * 50)
    app.run(host='0.0.0.0', port=5000, debug=True)