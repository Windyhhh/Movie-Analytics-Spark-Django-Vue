<script setup>
import { onMounted, ref } from 'vue';
import { useDataStore } from '../../stores/data';
const dataStore = useDataStore()
const count101 = ref(0)
const count111 = ref(0)
const count211 = ref(0)
const count212 = ref(0)
setTimeout(()=>{
  for(let i = 0; i<dataStore.dataList.length; i++){
    if(dataStore.dataList[i].huxing == '1室0厅1卫') count101.value++
    if(dataStore.dataList[i].huxing == '1室1厅1卫') count111.value++
    if(dataStore.dataList[i].huxing == '2室1厅1卫') count211.value++
    if(dataStore.dataList[i].huxing == '2室1厅2卫') count212.value++
  }
  console.log(count101.value,count111.value,count211.value,count212.value)
},0)

const config = ref({
  data: [
    {
      name: '1室0厅1卫',
      value: 10
    },
    {
      name: '1室1厅1卫',
      value: 42
    },
    {
      name: '2室1厅1卫',
      value: 20
    },
    {
      name: '2室1厅2卫',
      value: 5
    },
  ],
  colors: ['#e062ae', '#fb7293', '#e690d1', '#32c5e9', '#96bfff'],
  unit: '单位',
  showValue: true
 })

</script>

<template>
<div style="flex: 2">
                <div style="color: aqua;">
                  <i class="icon iconfont icon-tubiao"></i>
                部分房屋户型数量
                </div>
              <dv-capsule-chart :config="config" style="width:100%;height: 175px; padding-right: 20px;" />
              </div>
</template>

<style scoped>

</style>