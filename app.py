from flask import Flask, send_file
import os

app = Flask(__name__)

# 获取当前文件所在的目录绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    # 确切指向当前目录下的 index.html
    file_path = os.path.join(BASE_DIR, 'index.html')
    return send_file(file_path)

if __name__ == '__main__':
    # 在 5000 端口运行，开启调试模式方便开发
    app.run(host='0.0.0.0', port=5000, debug=True)
