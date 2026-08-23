<template>
  <div class="home-container">
    <div class="dashboard-header">
      <h1>电影数据分析可视化平台</h1>
      <div class="header-actions">
        <button @click="handleRunAnalysis" class="run-btn">
          <span v-if="!isRunning">运行Spark分析</span>
          <span v-else>分析中...</span>
        </button>
        <button @click="handleRefresh" class="refresh-btn">刷新数据</button>
      </div>
    </div>

    <div class="dashboard-content">
      <!-- 概览卡片 -->
      <div class="overview-cards">
        <div class="card">
          <h3>电影总数</h3>
          <p class="card-value">{{ allMovies.length }}</p>
        </div>
        <div class="card">
          <h3>平均评分</h3>
          <p class="card-value">{{ averageRating.toFixed(1) }}</p>
        </div>
        <div class="card">
          <h3>类型数量</h3>
          <p class="card-value">{{ genreAnalysis.length }}</p>
        </div>
        <div class="card">
          <h3>年份范围</h3>
          <p class="card-value">{{ yearRange }}</p>
        </div>
      </div>

      <!-- 图表区域 -->
      <div class="charts-grid">
        <!-- 按类型分析 - 柱状图 -->
        <div class="chart-item">
          <h2>电影类型分布</h2>
          <div class="chart-container">
            <BarChart :data="genreChartData" />
          </div>
        </div>

        <!-- 按年份分析 - 折线图 -->
        <div class="chart-item">
          <h2>电影年份趋势</h2>
          <div class="chart-container">
            <LineChart :data="yearChartData" />
          </div>
        </div>

        <!-- 评分分布 - 饼图 -->
        <div class="chart-item">
          <h2>评分分布</h2>
          <div class="chart-container">
            <PieChart :data="ratingChartData" />
          </div>
        </div>

        <!-- 评分与投票数关系 - 散点图 -->
        <div class="chart-item">
          <h2>评分与投票数关系</h2>
          <div class="chart-container">
            <ScatterChart :data="scatterChartData" />
          </div>
        </div>
      </div>

      <!-- 电影列表 -->
      <div class="movie-list-section">
        <h2>电影列表</h2>
        <div class="movie-table-container">
          <table class="movie-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>标题</th>
                <th>类型</th>
                <th>年份</th>
                <th>评分</th>
                <th>投票数</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="movie in allMovies" :key="movie.movie_id">
                <td>{{ movie.movie_id }}</td>
                <td class="movie-title">{{ movie.title }}</td>
                <td>{{ movie.genre }}</td>
                <td>{{ movie.release_year }}</td>
                <td class="rating">{{ movie.rating }}</td>
                <td>{{ movie.votes.toLocaleString() }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useDataStore } from '../stores/data.js'
import BarChart from './chart/barchart.vue'
import LineChart from './chart/linechart.vue'
import PieChart from './chart/piechart.vue'
import ScatterChart from './chart/scatterchart.vue'

const dataStore = useDataStore()
const isRunning = ref(false)

// 计算属性
const allMovies = computed(() => dataStore.allMovies)
const genreAnalysis = computed(() => dataStore.genreAnalysis)
const yearAnalysis = computed(() => dataStore.yearAnalysis)
const ratingAnalysis = computed(() => dataStore.ratingAnalysis)

// 计算平均评分
const averageRating = computed(() => {
  if (allMovies.value.length === 0) return 0
  const sum = allMovies.value.reduce((acc, movie) => acc + movie.rating, 0)
  return sum / allMovies.value.length
})

// 计算年份范围
const yearRange = computed(() => {
  if (allMovies.value.length === 0) return '0000-0000'
  const years = allMovies.value.map(movie => movie.release_year)
  const min = Math.min(...years)
  const max = Math.max(...years)
  return `${min}-${max}`
})

// 图表数据转换
const genreChartData = computed(() => {
  return genreAnalysis.value.map(item => ({
    name: item.genre,
    value: item.movie_count
  }))
})

const yearChartData = computed(() => {
  return yearAnalysis.value.map(item => ({
    name: item.release_year.toString(),
    value: item.movie_count
  }))
})

const ratingChartData = computed(() => {
  return ratingAnalysis.value.map(item => ({
    name: item.rating.toString(),
    value: item.movie_count
  }))
})

const scatterChartData = computed(() => {
  return allMovies.value.map(movie => ({
    name: movie.title,
    x: movie.rating,
    y: movie.votes
  }))
})

// 方法
const handleRunAnalysis = async () => {
  isRunning.value = true
  try {
    const result = await dataStore.runAnalysis()
    console.log('分析结果:', result)
    await dataStore.fetchAllData()
  } catch (error) {
    console.error('分析失败:', error)
    alert('分析失败，请检查Spark环境配置')
  } finally {
    isRunning.value = false
  }
}

const handleRefresh = async () => {
  try {
    await dataStore.fetchAllData()
  } catch (error) {
    console.error('刷新失败:', error)
    alert('刷新失败，请检查后端服务')
  }
}

// 初始化数据
onMounted(async () => {
  try {
    await dataStore.fetchAllData()
  } catch (error) {
    console.error('初始化数据失败:', error)
    // 首次加载可能没有处理后的数据，提示用户运行分析
    alert('请先运行Spark分析生成数据')
  }
})
</script>

<style scoped>
/* 全局样式 */
.home-container {
  width: 100%;
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 20px;
  box-sizing: border-box;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
}

/* 头部样式 */
.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  background: rgba(255, 255, 255, 0.95);
  padding: 24px 30px;
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.dashboard-header h1 {
  margin: 0;
  color: #333;
  font-size: 28px;
  font-weight: 700;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* 按钮样式 */
.header-actions {
  display: flex;
  gap: 12px;
}

.run-btn, .refresh-btn {
  padding: 12px 24px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 600;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.run-btn {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.run-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
}

.refresh-btn {
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  color: white;
}

.refresh-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(245, 87, 108, 0.4);
}

.run-btn:active, .refresh-btn:active {
  transform: translateY(0);
}

/* 内容区域 */
.dashboard-content {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

/* 概览卡片 */
.overview-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 20px;
}

.card {
  background: rgba(255, 255, 255, 0.95);
  padding: 24px;
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  text-align: center;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
}

.card h3 {
  margin: 0 0 12px 0;
  color: #606266;
  font-size: 14px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.card-value {
  margin: 0;
  font-size: 32px;
  font-weight: 700;
  color: #303133;
  transition: all 0.3s ease;
}

.card:hover .card-value {
  transform: scale(1.05);
}

/* 图表网格 */
.charts-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
  gap: 24px;
}

/* 图表项 */
.chart-item {
  background: rgba(255, 255, 255, 0.95);
  padding: 24px;
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.chart-item:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
}

.chart-item h2 {
  margin: 0 0 20px 0;
  color: #333;
  font-size: 20px;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 8px;
}

.chart-item h2::before {
  content: '';
  display: inline-block;
  width: 4px;
  height: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 2px;
}

.chart-container {
  height: 320px;
  position: relative;
  overflow: hidden;
  border-radius: 12px;
  background: rgba(248, 249, 250, 0.5);
  padding: 10px;
}

/* 电影列表 */
.movie-list-section {
  background: rgba(255, 255, 255, 0.95);
  padding: 24px;
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.movie-list-section h2 {
  margin: 0 0 20px 0;
  color: #333;
  font-size: 20px;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 8px;
}

.movie-list-section h2::before {
  content: '';
  display: inline-block;
  width: 4px;
  height: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 2px;
}

.movie-table-container {
  overflow-x: auto;
  border-radius: 12px;
  background: rgba(248, 249, 250, 0.5);
}

.movie-table {
  width: 100%;
  border-collapse: collapse;
  background: transparent;
}

.movie-table th,
.movie-table td {
  padding: 14px 16px;
  text-align: left;
  border-bottom: 1px solid rgba(235, 237, 240, 0.8);
}

.movie-table th {
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
  font-weight: 600;
  color: #303133;
  text-transform: uppercase;
  font-size: 12px;
  letter-spacing: 0.5px;
  position: sticky;
  top: 0;
  z-index: 10;
}

.movie-table td {
  color: #606266;
  font-size: 14px;
  transition: all 0.2s ease;
}

.movie-table tr:hover td {
  background: rgba(102, 126, 234, 0.05);
  color: #303133;
}

.movie-title {
  font-weight: 500;
  color: #303133;
  cursor: pointer;
  transition: all 0.2s ease;
}

.movie-title:hover {
  color: #667eea;
  text-decoration: underline;
}

.rating {
  color: #f39c12;
  font-weight: 600;
  font-size: 15px;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .dashboard-header {
    flex-direction: column;
    gap: 16px;
    text-align: center;
  }
  
  .charts-grid {
    grid-template-columns: 1fr;
  }
  
  .overview-cards {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .dashboard-header h1 {
    font-size: 24px;
  }
}

@media (max-width: 480px) {
  .overview-cards {
    grid-template-columns: 1fr;
  }
  
  .home-container {
    padding: 10px;
  }
  
  .chart-container {
    height: 250px;
  }
}
</style>