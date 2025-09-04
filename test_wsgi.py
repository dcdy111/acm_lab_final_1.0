# 测试用WSGI入口文件
import os
import sys

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(__file__))

# 导入测试应用
from test_app import app

# Vercel需要这个特定的导出
application = app

# 为了确保兼容性，也导出app
__all__ = ['application', 'app']
