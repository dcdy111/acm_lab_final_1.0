# WSGI入口文件 - 用于Vercel部署
import os
import sys

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(__file__))

# 导入Flask应用
from app import app

# Vercel需要这个变量
handler = app

# 如果直接运行此文件，启动开发服务器
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
