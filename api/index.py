# Vercel API入口点
from app import app

# 导出Flask应用实例
application = app

# Vercel函数处理器
def handler(request):
    """Vercel无服务器函数处理器"""
    return app(request.environ, lambda status, headers: None)