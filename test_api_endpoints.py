#!/usr/bin/env python3
"""
API端点测试脚本
用于测试修复后的API端点是否正常工作
"""

import requests
import json
import sys
import os

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(__file__))

def test_api_endpoint(url, method='GET', data=None, headers=None):
    """测试API端点"""
    try:
        if method == 'GET':
            response = requests.get(url, headers=headers, timeout=10)
        elif method == 'POST':
            response = requests.post(url, json=data, headers=headers, timeout=10)
        elif method == 'PUT':
            response = requests.put(url, json=data, headers=headers, timeout=10)
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers, timeout=10)
        
        print(f"🔍 {method} {url}")
        print(f"   状态码: {response.status_code}")
        
        if response.status_code == 200:
            print(f"   ✅ 成功")
            try:
                result = response.json()
                if isinstance(result, list):
                    print(f"   返回数据: {len(result)} 条记录")
                elif isinstance(result, dict):
                    print(f"   返回数据: {list(result.keys())}")
                else:
                    print(f"   返回数据: {type(result)}")
            except:
                print(f"   返回数据: 非JSON格式")
        elif response.status_code == 500:
            print(f"   ❌ 服务器错误")
            try:
                error = response.json()
                print(f"   错误信息: {error.get('error', '未知错误')}")
            except:
                print(f"   错误信息: {response.text[:100]}")
        else:
            print(f"   ⚠️ 其他状态码")
            try:
                result = response.json()
                print(f"   响应: {result}")
            except:
                print(f"   响应: {response.text[:100]}")
        
        print()
        return response.status_code == 200
        
    except requests.exceptions.RequestException as e:
        print(f"🔍 {method} {url}")
        print(f"   ❌ 请求失败: {e}")
        print()
        return False

def main():
    """主测试函数"""
    print("🚀 开始测试API端点...")
    print("=" * 50)
    
    # 基础URL - 假设应用运行在本地5000端口
    base_url = "http://localhost:5000"
    
    # 测试的API端点列表
    test_endpoints = [
        # 前端API端点
        ("/api/frontend/algorithms", "GET"),
        ("/api/frontend/algorithm-awards", "GET"),
        ("/api/frontend/project-overview", "GET"),
        ("/api/innovation-projects", "GET"),
        ("/api/advisors", "GET"),
        ("/api/frontend/advisors", "GET"),
        
        # 管理员API端点（需要认证）
        ("/api/admin/algorithms", "GET"),
        ("/api/admin/algorithm-awards", "GET"),
        ("/api/admin/project-overview", "GET"),
        ("/api/innovation-projects/admin", "GET"),
        
        # 年级管理API
        ("/api/grades", "GET"),
        
        # 团队成员API
        ("/api/team", "GET"),
        
        # 研究领域API
        ("/api/research-areas", "GET"),
    ]
    
    success_count = 0
    total_count = len(test_endpoints)
    
    for endpoint, method in test_endpoints:
        url = base_url + endpoint
        if test_api_endpoint(url, method):
            success_count += 1
    
    print("=" * 50)
    print(f"📊 测试结果: {success_count}/{total_count} 个端点正常")
    
    if success_count == total_count:
        print("🎉 所有API端点测试通过！")
        return 0
    else:
        print(f"⚠️ 有 {total_count - success_count} 个端点存在问题")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
