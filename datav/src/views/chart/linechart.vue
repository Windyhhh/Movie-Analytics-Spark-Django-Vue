<script setup>
import { onMounted, ref } from 'vue';
import { useDataStore } from '../../stores/data';
const dataStore = useDataStore()
const jz = ref(0)
const hh = ref(0)
const typept = ref(0)
const typeqt = ref(0)
onMounted(()=>{
  for(let i = 0 ; i < dataStore.dataList.length; i++){
    if(dataStore.dataList[i].zhuangxiu == '豪华装修') hh.value++
    if(dataStore.dataList[i].zhuangxiu == '精装修') jz.value++
    if(dataStore.dataList[i].type == '普通住宅') typept.value++
    if(dataStore.dataList[i].type == '其他') typeqt.value++
  }
  console.log(hh.value,jz.value,typept.value,typeqt.value)
})
const option = ref({
  title: {
    text: '房屋及装修类型情况',
    style:{
      fill:'#fff',
      fontSize:14
    }
  },
  xAxis: {
    name: '',
    nameTextStyle:{
      fill:'#fff',
      fontSize:10
    },
    data: ['豪华装修', '精装修', '普通住宅', '其他'],
    axisLabel:{
      style:{
        fill:'#fff'
      }
    }
  },
  yAxis: {
    name: '房屋数量',
    nameTextStyle:{
      fill:'#fff',
      fontSize:10
    },
    data: 'value',
    axisLabel:{
      style:{
        fill:'#fff'
      }
    }
  },
  series: [
    {
     data: [10, 128, 118, 17],
      color:'#ffdb5c',
      type: 'line',
      smooth: true
    }
  ]
})

</script>

<template>
    <dv-charts :option="option" style="width: 100%;height: 380px;"></dv-charts>
</template>

<style scoped>

</style>
