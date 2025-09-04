# Vercel API - 前端数据接口
from flask import Flask, jsonify
import sys
import os
import sqlite3
import json
from datetime import datetime

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__)

def get_db_connection():
    """获取数据库连接"""
    db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'acm_lab.db')
    conn = sqlite3.connect(f'file:{db_path}?mode=ro', uri=True)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/frontend/papers')
def get_frontend_papers():
    """获取前端论文数据"""
    try:
        conn = get_db_connection()
        cursor = conn.execute("SELECT * FROM papers ORDER BY order_index ASC, updated_at DESC LIMIT 3")
        papers = cursor.fetchall()
        
        papers_data = []
        for paper in papers:
            paper_dict = dict(paper)
            
            # 处理authors字段
            authors = paper_dict.get('authors', '[]')
            if isinstance(authors, str):
                try:
                    authors = json.loads(authors)
                except:
                    authors = [authors] if authors else []
            
            if not isinstance(authors, list):
                authors = [authors] if authors else []
            
            paper_dict['authors'] = authors
            
            # 处理categories字段
            categories = paper_dict.get('category_ids', '[]')
            if isinstance(categories, str):
                try:
                    categories = json.loads(categories)
                except:
                    categories = []
            
            if not isinstance(categories, list):
                categories = []
            
            paper_dict['categories'] = categories
            
            # 获取类别名称
            category_names = []
            category_map = {
                16: 'CCF-A', 17: 'CCF-B', 18: 'CCF-C',
                19: '中科院一区', 20: '中科院二区', 21: '中科院三区', 22: '中科院四区',
                23: 'JCR一区', 24: 'JCR二区', 25: 'JCR三区', 26: 'JCR四区',
                27: 'EI源刊', 28: 'EI会议', 29: '南核', 30: 'CSCD', 31: '北核', 32: '普刊'
            }
            
            for cat_id in categories:
                if cat_id in category_map:
                    category_names.append(category_map[cat_id])
            
            paper_dict['category_names'] = category_names
            papers_data.append(paper_dict)
        
        conn.close()
        return jsonify(papers_data)
    except Exception as e:
        print(f"Error fetching frontend papers: {e}")
        return jsonify([])

@app.route('/api/frontend/team')
def get_frontend_team():
    """获取前端团队数据"""
    try:
        conn = get_db_connection()
        cursor = conn.execute('SELECT * FROM team_members ORDER BY order_index ASC, created_at DESC')
        members = cursor.fetchall()
        
        members_data = []
        for member in members:
            member_dict = dict(member)
            members_data.append(member_dict)
        
        conn.close()
        return jsonify(members_data)
    except Exception as e:
        print(f"Error fetching frontend team: {e}")
        return jsonify([])

@app.route('/api/frontend/activities')
def get_frontend_activities():
    """获取前端活动数据"""
    try:
        conn = get_db_connection()
        cursor = conn.execute('''
            SELECT id, title, excerpt, category, author, publish_date, reading_time, tags
            FROM notifications 
            WHERE status = 'published'
            ORDER BY order_index ASC, publish_date DESC
            LIMIT 3
        ''')
        activities = []
        for row in cursor.fetchall():
            activity = dict(row)
            # 格式化日期
            if activity['publish_date']:
                try:
                    date_obj = datetime.strptime(activity['publish_date'], '%Y-%m-%d %H:%M:%S')
                    activity['formatted_date'] = date_obj.strftime('%Y.%m.%d')
                except:
                    activity['formatted_date'] = activity['publish_date']
            else:
                activity['formatted_date'] = '未知日期'
            activities.append(activity)
        
        conn.close()
        return jsonify(activities)
    except Exception as e:
        print(f"Error fetching frontend activities: {e}")
        return jsonify([])

@app.route('/api/frontend/innovation-projects')
def get_frontend_innovation_projects():
    """获取前端科创项目数据"""
    try:
        conn = get_db_connection()
        cursor = conn.execute("SELECT * FROM innovation_projects WHERE status = 'active' ORDER BY sort_order")
        projects = cursor.fetchall()
        
        projects_data = []
        for project in projects:
            project_dict = dict(project)
            projects_data.append(project_dict)
        
        conn.close()
        return jsonify(projects_data)
    except Exception as e:
        print(f"Error fetching frontend innovation projects: {e}")
        return jsonify([])

# Vercel处理函数
def handler(request):
    return app.test_client().open(request.path, method=request.method, data=request.data)

if __name__ == "__main__":
    app.run(debug=True)
