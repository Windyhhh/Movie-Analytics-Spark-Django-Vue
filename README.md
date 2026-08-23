# 🎬 Movie Analytics Platform | 电影数据分析可视化平台

> **Full-stack big data movie analytics platform: Apache Spark data processing + Django REST API backend + Vue3/ECharts interactive visualization. 8 chart types, genre/rating/year analysis, real-time dashboard.**
>
> 全栈大数据电影分析平台：Apache Spark 数据处理 + Django REST API 后端 + Vue3/ECharts 交互式可视化。8 种图表类型，类型/评分/年份分析，实时仪表盘。

---

## 🌟 Why This Project? | 项目亮点

Movie datasets contain rich insights about trends in genre popularity, rating distributions, and temporal patterns. This project implements a **complete full-stack big data analytics platform** combining **Apache Spark** for scalable data processing, **Django REST Framework** for API backend, and **Vue3 + ECharts** for interactive visualization. The platform features **8 chart types** (bar, line, pie, scatter, radar, gauge, capsule, water level, scroll board), real-time data fetching, and a responsive dashboard layout.

电影数据集包含关于类型流行度、评分分布和时间模式的丰富洞察。本项目实现了一个**完整的全栈大数据分析平台**，结合 **Apache Spark** 进行可扩展数据处理，**Django REST Framework** 作为 API 后端，**Vue3 + ECharts** 实现交互式可视化。平台支持 **8 种图表类型**（柱状图、折线图、饼图、散点图、雷达图、仪表盘、胶囊图、水球图、滚动看板），实时数据获取和响应式仪表盘布局。

| Feature | Details |
|---------|---------|
| **Data Processing** | Apache Spark (PySpark) for scalable movie data analysis |
| **Backend** | Django 4 + Django REST Framework (REST API) |
| **Frontend** | Vue3 + Vite + ECharts 5 (interactive visualization) |
| **Chart Types** | Bar, Line, Pie, Scatter, Radar, Gauge, Capsule, Water Level, Scroll Board |
| **Analysis Dimensions** | Genre distribution, rating analysis, year trends, movie metadata |
| **State Management** | Pinia (Vue3 state management) |
| **Routing** | Vue Router 4 |
| **Build Tool** | Vite (frontend) + Django (backend) |
| **Data Format** | CSV (raw) + JSON (processed) |

---

## 🏗️ Architecture | 架构设计

```
┌─────────────────────────────────────────────────────────────┐
│                   Raw Movie Data (CSV)                        │
│              movies.csv (title, genre, rating, year, ...)     │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│              Apache Spark Data Processing Layer                │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │  spark_analysis.py                                       │  │
│  │  • Load CSV into Spark DataFrame                         │  │
│  │  • Genre analysis: count per genre                       │  │
│  │  • Rating analysis: distribution statistics               │  │
│  │  • Year analysis: trends over time                       │  │
│  │  • Output: processed JSON files                           │  │
│  └─────────────────────────────────────────────────────────┘  │
│         Output: data/processed/*.json                          │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│              Django REST API Backend                           │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │  Project: movie_api (Django 4)                           │  │
│  │  App: analytics                                           │  │
│  │  • models.py: Movie, Genre, Rating models                │  │
│  │  • views.py: REST API views (list, detail, analytics)   │  │
│  │  • urls.py: API routing                                   │  │
│  │  • settings.py: Django configuration                      │  │
│  └─────────────────────────────────────────────────────────┘  │
│         REST Endpoints:                                         │
│         GET /api/movies/        — Movie list                   │
│         GET /api/movies/{id}/   — Movie detail                 │
│         GET /api/analytics/genre/ — Genre analysis             │
│         GET /api/analytics/rating/ — Rating analysis           │
│         GET /api/analytics/year/ — Year trends                 │
└──────────────────────────────┬──────────────────────────────┘
                               │ HTTP/REST + JSON
                               ▼
┌─────────────────────────────────────────────────────────────┐
│              Vue3 + ECharts Frontend                           │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │  Framework: Vue3 + Vite + Pinia + Vue Router 4          │  │
│  │                                                          │  │
│  │  Views:                                                   │  │
│  │  • home.vue (12KB) — Main dashboard with all charts     │  │
│  │  • moduleFirst.vue — First analysis module               │  │
│  │  • moduleSecond.vue — Second analysis module             │  │
│  │  • moduleTitle.vue — Module title component              │  │
│  │                                                          │  │
│  │  Chart Components (views/chart/):                        │  │
│  │  • barchart.vue — Bar chart (genre distribution)         │  │
│  │  • linechart.vue — Line chart (year trends)              │  │
│  │  • piechart.vue — Pie chart (rating distribution)        │  │
│  │  • scatterchart.vue — Scatter plot (rating vs year)      │  │
│  │  • radarchart.vue — Radar chart (multi-dimension)        │  │
│  │  • gaugechart.vue — Gauge chart (average rating)         │  │
│  │  • capsulechart.vue — Capsule progress chart             │  │
│  │  • water.vue — Water level chart (completion rate)       │  │
│  │  • scrollboard.vue (10KB) — Scrolling data board         │  │
│  └─────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure | 项目结构

```
Movie-Analytics-Spark-Django-Vue/
├── 电影数据分析可视化平台博客.md    # Technical blog
├── datav/                           # Alternative Vue3 visualization frontend
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── src/
│   └── vue/
└── movie_analytics/                 # Main full-stack project
    ├── README.md
    ├── backend/                     # Django REST API backend
    │   ├── manage.py
    │   ├── requirements.txt
    │   ├── analytics/               # Django app
    │   │   ├── models.py            # Movie, Genre, Rating models
    │   │   ├── views.py             # REST API views
    │   │   ├── urls.py              # API routing
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   └── migrations/
    │   └── movie_api/               # Django project config
    │       ├── settings.py
    │       ├── urls.py
    │       ├── asgi.py
    │       └── wsgi.py
    ├── config/                      # Configuration files
    ├── data/                        # Movie dataset
    │   ├── movies.csv               # Raw movie data
    │   └── processed/               # Spark-processed JSON
    │       ├── movies.json
    │       ├── genre_analysis.json
    │       ├── rating_analysis.json
    │       └── year_analysis.json
    ├── data_processing/             # Spark data processing
    │   └── spark_analysis.py        # PySpark analysis script
    └── frontend/                    # Vue3 + ECharts frontend
        ├── index.html
        ├── package.json
        ├── vite.config.js
        ├── public/
        └── src/
            ├── App.vue
            ├── main.js
            ├── style.css
            ├── router/index.js       # Vue Router 4
            ├── stores/data.js        # Pinia state management
            ├── views/
            │   ├── home.vue          # Main dashboard (12KB)
            │   ├── moduleFirst.vue
            │   ├── moduleSecond.vue
            │   ├── moduleTitle.vue
            │   └── chart/
            │       ├── barchart.vue
            │       ├── linechart.vue
            │       ├── piechart.vue
            │       ├── scatterchart.vue
            │       ├── radarchart.vue
            │       ├── gaugechart.vue
            │       ├── capsulechart.vue
            │       ├── water.vue
            │       └── scrollboard.vue
            ├── assets/
            │   ├── css/
            │   └── font/
            └── type/
```

---

## 🚀 Quick Start | 快速开始

### 1. Spark Data Processing | Spark 数据处理

```bash
cd movie_analytics/data_processing

# Ensure PySpark is installed
pip install pyspark

# Run Spark analysis
python spark_analysis.py
```

This processes `data/movies.csv` and outputs JSON files to `data/processed/`.

### 2. Django Backend | Django 后端

```bash
cd movie_analytics/backend

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# (Optional) Load movie data
python manage.py loaddata ../data/processed/movies.json

# Start development server
python manage.py runserver 0.0.0.0:8000
```

API available at `http://localhost:8000/api/`

### 3. Vue3 Frontend | Vue3 前端

```bash
cd movie_analytics/frontend

# Install dependencies
npm install
# or: yarn install

# Start development server
npm run dev
# or: yarn dev
```

Frontend available at `http://localhost:5173/`

---

## 📊 Chart Components | 图表组件

| Component | File | Description | Use Case |
|-----------|------|-------------|----------|
| **Bar Chart** | `barchart.vue` | Vertical/horizontal bar chart | Genre distribution, count comparison |
| **Line Chart** | `linechart.vue` | Time series line chart | Year trends, rating over time |
| **Pie Chart** | `piechart.vue` | Proportion pie/donut chart | Rating distribution, genre share |
| **Scatter Chart** | `scatterchart.vue` | 2D scatter plot | Rating vs year, budget vs revenue |
| **Radar Chart** | `radarchart.vue` | Multi-dimension radar | Movie multi-attribute comparison |
| **Gauge Chart** | `gaugechart.vue` | Dashboard gauge | Average rating, completion rate |
| **Capsule Chart** | `capsulechart.vue` | Capsule progress bar | Genre coverage, data completeness |
| **Water Level** | `water.vue` | Animated water level | Achievement rate, target progress |
| **Scroll Board** | `scrollboard.vue` | Auto-scrolling data board | Top movies, real-time rankings |

---

## 🔧 API Endpoints | API 接口

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/movies/` | List all movies (paginated) |
| GET | `/api/movies/{id}/` | Get movie detail by ID |
| GET | `/api/analytics/genre/` | Genre distribution analysis |
| GET | `/api/analytics/rating/` | Rating distribution statistics |
| GET | `/api/analytics/year/` | Year-by-year trends |
| GET | `/api/analytics/top/?n=10` | Top N movies by rating |

---

## 📚 References | 参考文献

1. **Apache Spark.** (2024). *Spark Programming Guide.*
2. **Django Software Foundation.** (2024). *Django Documentation.*
3. **Vue.js.** (2024). *Vue 3 Documentation.*
4. **Apache ECharts.** (2024). *ECharts 5 Documentation.*
5. **Meng, X., et al.** (2016). *MLlib: Machine learning in Apache Spark.* JMLR.

---

## 📄 License | 许可证

MIT License — free to use, modify, and distribute.

---

<div align="center">

**Built with 🎬 for big data visualization**

[Report Bug](https://github.com/Windyhhh/Movie-Analytics-Spark-Django-Vue/issues) · [Request Feature](https://github.com/Windyhhh/Movie-Analytics-Spark-Django-Vue/issues)

</div>
