import { defineStore } from 'pinia'
import { ref } from 'vue'
import axios from 'axios'

export const useDataStore = defineStore('data', () => {
  // 电影数据相关
  const genreAnalysis = ref([])
  const yearAnalysis = ref([])
  const ratingAnalysis = ref([])
  const allMovies = ref([])

  // API基础URL
  const API_BASE_URL = 'http://127.0.0.1:8000'

  // 获取按类型分析的数据
  const getGenreAnalysis = async () => {
    const res = await axios.get(`${API_BASE_URL}/api/genre/`)
    genreAnalysis.value = res.data
  }

  // 获取按年份分析的数据
  const getYearAnalysis = async () => {
    const res = await axios.get(`${API_BASE_URL}/api/year/`)
    yearAnalysis.value = res.data
  }

  // 获取评分分布分析的数据
  const getRatingAnalysis = async () => {
    const res = await axios.get(`${API_BASE_URL}/api/rating/`)
    ratingAnalysis.value = res.data
  }

  // 获取所有电影数据
  const getAllMovies = async () => {
    const res = await axios.get(`${API_BASE_URL}/api/movies/`)
    allMovies.value = res.data
  }

  // 运行Spark分析
  const runAnalysis = async () => {
    const res = await axios.post(`${API_BASE_URL}/api/run-analysis/`)
    return res.data
  }

  // 获取所有数据
  const fetchAllData = async () => {
    await Promise.all([
      getGenreAnalysis(),
      getYearAnalysis(),
      getRatingAnalysis(),
      getAllMovies()
    ])
  }

  return {
    genreAnalysis,
    yearAnalysis,
    ratingAnalysis,
    allMovies,
    getGenreAnalysis,
    getYearAnalysis,
    getRatingAnalysis,
    getAllMovies,
    runAnalysis,
    fetchAllData
  }
})
