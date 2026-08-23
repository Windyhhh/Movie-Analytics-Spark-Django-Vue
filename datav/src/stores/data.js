import { defineStore } from 'pinia'
import { ref } from 'vue'
import axios from 'axios'

export const useDataStore = defineStore('data', () => {
  const dataList = ref({})

  const getList = async () => {
    const res = await axios.get('http://127.0.0.1:8081/get_data')
    dataList.value = res.data
  }
  return {
    getList,
    dataList
  }
})
