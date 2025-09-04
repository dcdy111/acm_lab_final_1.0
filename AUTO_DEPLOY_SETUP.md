# 🚀 自动部署设置指南

## ✅ 自动部署功能已实现

您的项目已经配置了完整的自动部署功能：

### 📋 已配置的文件：

1. **✅ vercel.json** - Vercel部署配置
2. **✅ .github/workflows/vercel-deploy.yml** - GitHub Actions自动部署工作流
3. **✅ requirements.txt** - Python依赖
4. **✅ runtime.txt** - Python版本指定

## 🔧 设置步骤

### 第一步：在Vercel创建项目

1. 访问 [vercel.com](https://vercel.com)
2. 用GitHub账号登录
3. 点击 "New Project"
4. 选择您的GitHub仓库
5. 点击 "Deploy" 完成初始部署

### 第二步：获取Vercel配置信息

部署完成后，在Vercel项目设置中找到：
- **Project ID**: 项目ID
- **Org ID**: 组织ID

### 第三步：在GitHub设置Secrets

在您的GitHub仓库中：
1. 进入 **Settings** → **Secrets and variables** → **Actions**
2. 点击 **New repository secret**
3. 添加以下三个secrets：

```
VERCEL_TOKEN = your_vercel_token
ORG_ID = your_org_id  
PROJECT_ID = your_project_id
```

**如何获取Vercel Token：**
1. 在Vercel控制台点击头像 → **Settings**
2. 进入 **Tokens** 页面
3. 点击 **Create Token**
4. 复制生成的token

## 🎯 自动部署流程

配置完成后，每次您：

1. **本地修改代码**
2. **推送到GitHub**：
   ```bash
   git add .
   git commit -m "更新内容"
   git push origin main
   ```
3. **GitHub Actions自动触发**
4. **Vercel自动重新部署**
5. **网站自动更新**

## 📊 部署状态监控

您可以在以下位置监控部署状态：

- **GitHub Actions**: 仓库 → Actions 标签页
- **Vercel Dashboard**: vercel.com → 您的项目 → Deployments

## 🔍 验证自动部署

测试自动部署功能：

1. 修改任意文件（如README.md）
2. 提交并推送：
   ```bash
   git add .
   git commit -m "测试自动部署"
   git push origin main
   ```
3. 观察GitHub Actions运行状态
4. 检查Vercel部署日志
5. 访问网站确认更新

## ⚠️ 常见问题

### 问题1：GitHub Actions失败
**解决方案**：
- 检查Secrets是否正确设置
- 确认Vercel Token权限
- 查看Actions日志错误信息

### 问题2：Vercel部署失败
**解决方案**：
- 检查vercel.json配置
- 确认requirements.txt依赖
- 查看Vercel部署日志

### 问题3：网站没有更新
**解决方案**：
- 清除浏览器缓存
- 检查Vercel部署状态
- 确认代码已正确推送

## 🎉 完成！

设置完成后，您就拥有了：
- ✅ 本地修改 → GitHub推送 → 自动部署的完整流程
- ✅ 无需手动操作，代码更新自动同步到线上
- ✅ 部署状态实时监控
- ✅ 回滚和版本管理功能

**现在您可以专注于内容更新，部署完全自动化！**
