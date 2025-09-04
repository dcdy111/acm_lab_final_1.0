# Vercel WSGI 入口文件
# 这个文件专门用于Vercel部署，避免兼容性问题

import os
import sys

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(__file__))

# 导入Flask应用
from app import app

# Vercel WSGI处理器
def handler(request):
    """Vercel WSGI处理器"""
    return app(request.environ, request.start_response)

# 直接导出app作为WSGI应用
application = app

# 为了兼容性，也导出handler
__all__ = ['application', 'handler']