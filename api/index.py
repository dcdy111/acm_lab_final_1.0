# Vercel API入口文件
from flask import Flask
import os
import sys

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 导入主应用
from app import app

# Vercel处理函数
def handler(request):
    """Vercel无服务器函数处理器"""
    return app(request.environ, lambda status, headers: None)

# 导出应用实例供Vercel使用
application = app

if __name__ == "__main__":
    app.run()
