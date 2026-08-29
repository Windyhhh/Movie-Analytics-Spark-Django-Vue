<div align="center">

# 电影分析全栈 | Movie-Analytics-Spark-Django-Vue

### End-to-end movie data analytics — Spark + Django + Vue3.

Distributed processing with Spark, a Django backend and a Vue3 frontend for professional movie-data visualization.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Apache Spark](https://img.shields.io/badge/Spark-3-E25A1C?logo=apachespark&logoColor=white)](https://spark.apache.org/)
[![Django](https://img.shields.io/badge/Django-4-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Vue](https://img.shields.io/badge/Vue-3-4FC08D?logo=vuedotjs&logoColor=white)](https://vuejs.org/)

</div>

---

**Movie-Analytics-Spark-Django-Vue** is an end-to-end movie-data analytics platform: **Spark** for distributed processing, a **Django** backend serving APIs, and a **Vue3** frontend for interactive visualization.

> [!NOTE]
> 中文项目：电影数据分析可视化平台——Spark 分布式处理 + Django 后端 + Vue3 前端。

---

## Features

- **Spark processing** — distributed analytics over movie datasets.
- **Django API** — structured backend endpoints.
- **Vue3 frontend** — interactive, professional visualization.
- **Full-stack** — data → processing → API → visualization.

---

## Quickstart

```bash
git clone https://github.com/Windyhhh/Movie-Analytics-Spark-Django-Vue.git
cd Movie-Analytics-Spark-Django-Vue

# process data with Spark
spark-submit movie_analytics/process.py

# run Django backend
python manage.py runserver

# start Vue frontend
cd movie_analytics/frontend && npm install && npm run serve
```

---

## Project Structure

```
Movie-Analytics-Spark-Django-Vue/
├── movie_analytics/            # Django app
│   └── frontend/               # Vue3 SPA
├── datav/                      # data & processing
└── docs/                       # blog
```

---

## License

MIT — free to use, modify and distribute.
