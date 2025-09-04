# Vercel WSGI 入口文件
# 这个文件专门用于Vercel部署，避免兼容性问题

import os
import sys

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(__file__))

# 设置环境变量
os.environ['VERCEL'] = 'true'

# 导入Flask应用
try:
    from app import app
    application = app
    print("✅ Flask应用导入成功")
except Exception as e:
    print(f"❌ Flask应用导入失败: {e}")
    # 创建一个简单的Flask应用作为后备
    from flask import Flask
    application = Flask(__name__)
    
    @application.route('/')
    def index():
        return "ACM Lab - 应用正在启动中..."

# Vercel需要这个特定的导出
__all__ = ['application']