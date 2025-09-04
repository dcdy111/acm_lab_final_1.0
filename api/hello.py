# Vercel API测试端点
from flask import Flask, jsonify
import sys
import os

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    """测试API端点"""
    return jsonify({
        "message": "Hello from Vercel API!",
        "status": "success",
        "service": "ACM Lab Management System"
    })

# Vercel处理函数
def handler(request):
    return app.test_client().open(request.path, method=request.method, data=request.data)

if __name__ == "__main__":
    app.run(debug=True)
