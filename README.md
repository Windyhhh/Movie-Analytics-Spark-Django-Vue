# 🎬 电影大数据分析平台 | Movie Analytics Platform

> **Spark 大数据处理 + Django 后端 + Vue 前端的全栈电影分析平台——从数据清洗到可视化看板，一站式电影洞察。**
>
> *Full-stack movie analytics platform with Spark big data processing + Django backend + Vue frontend — from data cleaning to visualization dashboard, one-stop movie insights.*

---

## ⭐ 核心卖点 | Why Star This

| 卖点 | Feature | 一句话 |
|------|---------|--------|
| 🔥 **全栈架构** | Full-Stack | Spark + Django + Vue 三层架构，工业级完整项目 |
| 📊 **大数据处理** | Big Data | Spark 处理百万级电影评分数据，高效 ETL |
| 🎨 **可视化看板** | Dashboard | Vue + ECharts 交互式数据可视化 |
| 🧮 **推荐算法** | Recommendation | 协同过滤电影推荐引擎 |
| 📈 **多维度分析** | Multi-Dimension | 评分、类型、年份、导演、演员多维度分析 |

---

## 🏆 技术栈 | Tech Stack

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Apache Spark](https://img.shields.io/badge/Spark-3.0+-red?logo=apachespark)
![Django](https://img.shields.io/badge/Django-3.2+-green?logo=django)
![Vue.js](https://img.shields.io/badge/Vue-3.0+-brightgreen?logo=vuedotjs)
![ECharts](https://img.shields.io/badge/ECharts-5.0+-orange?logo=apacheecharts)

---

## 📊 架构分层 | Architecture Layers

| 层级 | 技术 | 职责 |
|------|------|------|
| 数据层 | Spark + HDFS | 大规模数据存储与处理 |
| 后端层 | Django REST Framework | API 服务、业务逻辑 |
| 前端层 | Vue 3 + ECharts | 交互式可视化看板 |
| 算法层 | Spark MLlib | 推荐算法、聚类分析 |

---

## 🚀 快速开始 | Quick Start

```bash
git clone https://github.com/Windyhhh/Movie-Analytics-Spark-Django-Vue.git
cd Movie-Analytics-Spark-Django-Vue

# 1. Spark 数据处理
cd spark
spark-submit etl.py --input data/movies.csv --output hdfs:///movies/etl

# 2. Django 后端
cd ../backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# 3. Vue 前端
cd ../frontend
npm install
npm run serve
```

访问 `http://localhost:8080`

---

## 📂 项目结构 | Project Structure

```
Movie-Analytics-Spark-Django-Vue/
├── spark/                     # Spark 大数据处理
│   ├── etl.py                 # 数据清洗 ETL
│   ├── analysis.py            # 数据分析
│   └── recommendation.py      # 推荐算法
├── backend/                   # Django 后端
│   ├── manage.py
│   ├── movies/                # 电影 APP
│   │   ├── models.py          # 数据模型
│   │   ├── views.py           # API 视图
│   │   └── serializers.py     # 序列化器
│   └── requirements.txt
├── frontend/                  # Vue 前端
│   ├── src/
│   │   ├── views/             # 页面组件
│   │   ├── components/        # 通用组件
│   │   └── api/               # API 调用
│   └── package.json
├── data/                      # 示例数据
└── README.md
```

---

## 🔬 核心功能 | Core Features

### 数据分析维度 | Analysis Dimensions

| 维度 | 分析内容 |
|------|---------|
| ⭐ 评分分布 | 电影评分直方图、平均分趋势 |
| 🎭 类型分析 | 各类型电影数量、评分对比 |
| 📅 年份趋势 | 电影产量、评分随时间变化 |
| 🎬 导演/演员 | 高产导演、高评分演员排名 |
| 🌍 地区分布 | 各国电影产量、评分对比 |

### 推荐算法 | Recommendation Algorithm

```
基于用户的协同过滤 (User-based CF):
  1. 计算用户间相似度 (余弦相似度)
  2. 找到 Top-K 相似用户
  3. 加权预测目标用户对未看电影的评分
  4. 推荐 Top-N 高分电影

基于物品的协同过滤 (Item-based CF):
  1. 计算电影间相似度
  2. 根据用户已看电影推荐相似电影
```

---

## 🎯 应用场景 | Use Cases

- 🎬 **电影平台**：为流媒体平台提供数据分析和推荐功能
- 📊 **数据科学教学**：大数据全栈项目的学习案例
- 🏢 **企业内训**：Spark + Django + Vue 技术栈培训
- 🎓 **毕业设计**：计算机相关专业的完整毕设项目

---

## 📚 数据集 | Dataset

- MovieLens 20M：2000 万条评分记录
- TMDB：电影元数据（类型、导演、演员等）

---

## 📄 License

MIT License — 自由使用、修改和分发。

---

> 💡 **Spark + Django + Vue 全栈大数据项目，Star ⭐ 支持开源！**
