# 🚀 ACM实验室管理系统 - Vercel部署指南

## 📋 部署概述

本指南将帮助您将ACM实验室管理系统部署到Vercel平台，实现：
- ✅ GitHub代码同步到Vercel自动部署
- ✅ Flask后端API在Vercel无服务器环境运行
- ✅ 前端页面加载后端SQLite数据库数据
- ✅ 只读数据库访问（符合您的需求）
- ✅ 完整的上线网站前端展示

## 🛠️ 部署前准备

### 1. 检查项目结构
确保以下文件已创建：
- ✅ `vercel.json` - Vercel配置文件
- ✅ `runtime.txt` - Python版本指定
- ✅ `requirements.txt` - 依赖包列表（已优化）
- ✅ `.vercelignore` - 忽略文件配置
- ✅ `api/index.py` - Vercel API入口
- ✅ `api/frontend.py` - 前端数据API
- ✅ `api/hello.py` - API测试端点

### 2. 数据库准备
- ✅ SQLite数据库已配置为只读模式
- ✅ 数据库文件 `acm_lab.db` 将作为静态资源部署
- ✅ 支持前端数据读取，无增删改查功能

## 🚀 部署步骤

### 第一步：准备GitHub仓库

1. **将代码推送到GitHub**
```bash
git add .
git commit -m "优化项目结构，支持Vercel部署"
git push origin main
```

### 第二步：连接Vercel

1. **访问 [Vercel官网](https://vercel.com)**
2. **使用GitHub账号登录**
3. **点击"New Project"**
4. **选择您的GitHub仓库**

### 第三步：配置部署设置

在Vercel项目设置中：

1. **Framework Preset**: 选择 "Other"
2. **Root Directory**: 保持默认 "./"
3. **Build Command**: 留空（无需构建）
4. **Output Directory**: 留空
5. **Install Command**: `pip install -r requirements.txt`

### 第四步：环境变量设置

在Vercel项目设置的Environment Variables中添加：

```
VERCEL=true
FLASK_ENV=production
```

### 第五步：部署

点击"Deploy"按钮开始部署。

## 🌐 访问地址

部署成功后，您将获得：

- **前台网站**: `https://your-project.vercel.app`
- **后台管理**: `https://your-project.vercel.app/admin`
- **API测试**: `https://your-project.vercel.app/api/hello`

## 📊 功能验证

### 前端功能测试：
- ✅ 首页展示（团队成员、论文成果、活动动态）
- ✅ 团队成员页面
- ✅ 论文成果页面
- ✅ 科创成果页面
- ✅ 实验室介绍页面

### API功能测试：
- ✅ `/api/frontend/papers` - 论文数据
- ✅ `/api/frontend/team` - 团队成员数据
- ✅ `/api/frontend/activities` - 活动动态数据
- ✅ `/api/frontend/innovation-projects` - 科创项目数据

## 🔧 技术说明

### Vercel适配优化：
1. **无服务器架构**: Flask应用转换为Vercel Functions
2. **只读数据库**: SQLite配置为只读模式，符合无服务器环境
3. **静态资源**: CSS/JS/图片文件通过Vercel CDN加速
4. **API路由**: 前端API调用自动适配Vercel域名

### 移除的功能：
- ❌ WebSocket实时通信（Vercel不支持）
- ❌ 文件上传功能（改为只读展示）
- ❌ 后台管理写操作（保留读取功能）
- ❌ 系统监控和统计（无服务器环境不适用）

## 🔄 自动部署

配置完成后，每次向GitHub仓库推送代码时，Vercel会自动：
1. 检测代码变更
2. 重新构建项目
3. 部署到生产环境
4. 更新网站内容

## 🐛 常见问题

### 问题1：数据库连接失败
**解决方案**: 确保 `acm_lab.db` 文件在项目根目录，且已提交到Git仓库

### 问题2：API调用失败
**解决方案**: 检查 `vercel.json` 配置中的路由规则是否正确

### 问题3：静态文件404
**解决方案**: 确保静态文件路径以 `/static/` 开头

### 问题4：中文字符显示异常
**解决方案**: 确保所有文件使用UTF-8编码保存

## 📞 技术支持

如果遇到部署问题：
1. 检查Vercel部署日志
2. 验证数据库文件是否正确上传
3. 测试API端点是否正常响应
4. 确认静态资源路径配置

## ✨ 部署成功标志

当您看到以下内容时，说明部署成功：
- 前端页面正常显示
- 团队成员数据正常加载
- 论文成果正常展示
- 科创项目数据正常显示
- API端点正常响应

---

**🎉 恭喜！您的ACM实验室管理系统已成功部署到Vercel！**
