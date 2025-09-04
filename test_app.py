# 最小化测试版本 - 用于Vercel部署测试
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'message': 'ACM Lab API is working!',
        'status': 'success',
        'version': '1.0.0'
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': '2024-01-01T00:00:00Z'
    })

if __name__ == '__main__':
    app.run(debug=True)
