# 电影数据分析可视化平台

## 项目概述

本项目是一个基于大数据技术栈的电影数据分析可视化平台，旨在通过Spark进行数据处理和分析，并通过Web前端直观展示分析结果。该项目适合作为大数据课程的作业或毕业设计，涵盖了数据处理、后端开发、前端可视化等完整的大数据应用开发流程。

## 技术栈

### 后端技术
- **Python 3.9+**：主要开发语言
- **Apache Spark 3.5+**：大数据处理框架
- **Django 4.2+**：Web后端框架
- **PySpark**：Spark的Python API
- **Pandas**：数据处理库

### 前端技术
- **Vue 3**：前端框架
- **Vite**：构建工具
- **Pinia**：状态管理
- **Axios**：HTTP客户端
- **@kjgl77/datav-vue3**：数据可视化组件库

## 项目结构

```
movie_analytics/
├── data/                 # 数据目录
│   ├── movies.csv        # 原始电影数据
│   └── processed/        # 处理后的数据（自动生成）
├── data_processing/      # 数据处理模块
│   └── spark_analysis.py # Spark数据分析脚本
├── backend/              # Django后端
│   ├── analytics/        # 分析应用
│   ├── movie_api/        # 项目配置
│   ├── manage.py         # Django管理脚本
│   └── requirements.txt  # 后端依赖
├── frontend/             # Vue前端
│   ├── src/              # 前端源代码
│   ├── index.html        # HTML入口
│   └── package.json      # 前端依赖
├── config/               # 配置文件
└── README.md             # 项目说明文档
```

## 功能特性

1. **数据处理**：使用Spark对电影数据进行分布式处理和分析
2. **多维度分析**：
   - 电影类型分布分析
   - 电影年份趋势分析
   - 评分分布分析
   - 评分与投票数关系分析
3. **可视化展示**：
   - 柱状图展示类型分布
   - 折线图展示年份趋势
   - 饼图展示评分分布
   - 散点图展示评分与投票数关系
4. **实时数据分析**：支持通过前端按钮触发Spark分析
5. **响应式设计**：适配不同屏幕尺寸

## 安装与运行

### 环境要求

- Python 3.9+
- Java 8/11（Spark运行依赖）
- Node.js 16+
- npm/yarn

### 安装步骤

#### 1. 克隆项目

```bash
git clone <项目地址>
cd movie_analytics
```

#### 2. 安装后端依赖

```bash
cd backend
pip install -r requirements.txt
```

#### 3. 安装前端依赖

```bash
cd ../frontend
npm install
# 或使用yarn
yarn install
```

### 运行项目

#### 1. 启动后端服务

```bash
cd backend
python manage.py runserver 0.0.0.0:8000
```

后端服务将在 http://localhost:8000 启动

#### 2. 启动前端开发服务器

```bash
cd frontend
npm run dev
# 或使用yarn
yarn dev
```

前端服务将在 http://localhost:5173 启动

#### 3. 访问应用

在浏览器中访问 http://localhost:5173 即可使用应用

## 使用说明

1. **首次使用**：打开应用后，点击"运行Spark分析"按钮生成分析数据
2. **查看数据**：分析完成后，页面将显示各类图表和电影列表
3. **刷新数据**：点击"刷新数据"按钮可重新加载最新数据
4. **查看详情**：将鼠标悬停在图表上可查看详细数据

## 数据说明

### 原始数据格式

`movies.csv`文件包含以下字段：

| 字段名       | 描述               | 示例                          |
|------------|--------------------|-------------------------------|
| movie_id   | 电影ID             | 1                             |
| title      | 电影标题           | The Shawshank Redemption      |
| genre      | 电影类型           | Drama                         |
| release_year | 发行年份          | 1994                          |
| rating     | 电影评分           | 9.3                           |
| votes      | 投票数量           | 2700000                       |

### 处理后的数据

Spark分析脚本将生成以下JSON文件，存储在`data/processed/`目录下：

- `genre_analysis.json`：按类型分析结果
- `year_analysis.json`：按年份分析结果
- `rating_analysis.json`：评分分布分析结果
- `movies.json`：完整电影数据

## API接口

### 1. 获取按类型分析数据

```
GET /api/genre/
```

### 2. 获取按年份分析数据

```
GET /api/year/
```

### 3. 获取评分分布分析数据

```
GET /api/rating/
```

### 4. 获取所有电影数据

```
GET /api/movies/
```

### 5. 运行Spark分析

```
POST /api/run-analysis/
```

## 扩展建议

1. **添加更多数据源**：支持从多个来源获取电影数据
2. **增加更多分析维度**：如导演分析、演员分析等
3. **添加预测功能**：使用机器学习模型预测电影评分
4. **优化前端界面**：添加更多交互功能和动画效果
5. **部署到生产环境**：使用Docker和Kubernetes进行容器化部署

## 注意事项

1. 确保Java环境已正确配置（Spark运行依赖）
2. 首次运行需要点击"运行Spark分析"按钮生成数据
3. 大数据集处理可能需要较长时间，请耐心等待
4. 开发环境下建议使用小数据集进行测试

## 许可证

MIT License

## 联系方式

如有问题或建议，欢迎联系项目开发者。

---

**备注**：本项目适合作为大数据课程作业或毕业设计，涵盖了完整的大数据应用开发流程，包括数据处理、后端开发、前端可视化等核心技术。