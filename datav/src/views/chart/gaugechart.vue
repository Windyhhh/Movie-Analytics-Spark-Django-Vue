<script setup>
import { onMounted, ref } from 'vue';
import { useDataStore } from '../../stores/data';
const dataStore = useDataStore()
const chaonan = ref(0)
const chaobei = ref(0)
setTimeout(()=>{
  for(let i = 0 ; i < dataStore.dataList.length; i++){
  if(dataStore.dataList[i].chaoxiang == '朝南') chaonan.value++
  if(dataStore.dataList[i].chaoxiang == '朝北') chaobei.value++
  if(dataStore.dataList[i].chaoxiang == '南北'){
    chaonan.value++
    chaobei.value++
  } 
}
chaonan.value = chaonan.value / (chaonan.value+chaobei.value) * 100
chaobei.value = chaobei.value / (chaonan.value+chaobei.value) * 100
console.log(chaonan.value,chaobei.value)
},0)

 const option = ref({
  title:{
    text:'房屋南朝向',
    offset: [0,-44],//标题偏移量
    style:{
      fill: '#fff',
      fontSize:14
    }
  },
  series: [
    {
      type: 'gauge',
      startAngle: -Math.PI / 2,
      endAngle: Math.PI * 1.5,
      arcLineWidth: 15,
      data: [
        { name: 'itemA', value: 81, gradient: ['#fb7293', '#e690d1', '#2fded6'] }
      ],
      axisLabel: {
        show: false
      },
      axisTick: {
        show: false
      },
      pointer: {
        show: false
      },
      dataItemStyle: {
        lineCap: 'round'
      },
      details: {
        show: true,
        formatter: '{value}%',
        style: {
            fill: '#1ed3e5',
            fontSize: 35
        }
      }
    }
  ]
 })

 const option1 = ref({
  title:{
    text:'房屋北朝向',
    offset: [0,-44],//标题偏移量
    style:{
      fill: '#fff',
      fontSize:14
    }

  },
  series: [
    {
      type: 'gauge',
      startAngle: -Math.PI / 2,
      endAngle: Math.PI * 1.5,
      arcLineWidth: 15,
      data: [
        { name: 'itemA', value:28, gradient: ['#03c2fd', '#1ed3e5', '#2fded6'] }
      ],
      axisLabel: {
        show: false
      },
      axisTick: {
        show: false
      },
      pointer: {
        show: false
      },
      dataItemStyle: {
        lineCap: 'round'
      },
      details: {
        show: true,
        formatter: '{value}%',
        style: {
            fill: '#1ed3e5',
            fontSize: 35
        }
      }
    }
  ]
 })
</script>

<template>
 <div class="d-flex" style="height:180px; padding-top: 20px;">
               <dv-charts :option="option" ></dv-charts>
               <dv-charts :option="option1" ></dv-charts>
            </div>
</template>

<style scoped>

</style>