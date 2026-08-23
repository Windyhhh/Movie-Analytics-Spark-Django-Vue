<script setup>
import { onMounted, ref } from 'vue';
import { useDataStore } from '../../stores/data';
const dataStore = useDataStore()
const mianjibj = ref(0)
const mianjish = ref(0)
const mianjigz = ref(0)
const mianjisz = ref(0)
onMounted(()=>{
  for(let i = 0 ; i < dataStore.dataList.length; i++){
    if(dataStore.dataList[i].zufang == '北京')
     { let mianjiStrbj = dataStore.dataList[i].mianji.replace('平方米', '');
    let bj = parseFloat(mianjiStrbj);
    mianjibj.value += bj
    
   }
    if(dataStore.dataList[i].zufang == '上海')
    { let mianjiStrsh = dataStore.dataList[i].mianji.replace('平方米', '');
    let sh = parseFloat(mianjiStrsh);
    mianjish.value += sh
    console.log(mianjigz.value)
   }
    if(dataStore.dataList[i].zufang == '广州')
    { let mianjiStrgz = dataStore.dataList[i].mianji.replace('平方米', '');
    let gz = parseFloat(mianjiStrgz);
    mianjigz.value += gz
   }
    if(dataStore.dataList[i].zufang == '深圳')
    { let mianjiStrsz = dataStore.dataList[i].mianji.replace('平方米', '');
    let sz = parseFloat(mianjiStrsz);
    mianjisz.value += sz
    
   }
  }
  mianjibj.value = (mianjibj.value / 60)
  mianjish.value = (mianjish.value / 37)
  mianjigz.value = (mianjigz.value / 29)
  mianjisz.value = (mianjisz.value / 23)
  console.log(mianjibj.value,mianjish.value,mianjigz.value,mianjisz.value)
})

 const option = ref({
  title: {
    text: '各地面积价格关系图',
    style:{
      fill:'#fff',
      fontSize:14
    }
  },
  legend: {
    data: ['图例1', '图例2'],
    top: 80,
    textStyle:{
      fill:'#fff'
    }
  },
  xAxis: {
    data: [
    '北京','上海','广州','深圳'
    ],
    axisLabel: {
      style: {
        rotate: 0,
        textAlign: 'left',
        textBaseline: 'top',
        fill:'#fff'
      }
    },
    axisTick: {
      show: false
    }
  },
  yAxis: [
    {
      name: '价格',
      data: 'value',
      min: 0,
      max: 6000,
      interval: 1000,
      splitLine: {
        show: false,
        style: {
          lineDash: [3,3]
        }
      },
      axisLabel: {
        style:{
          fill:'#fff'
        },
        formatter: '{value} 元/月'
      },
      axisTick: {
        show: false
      }
    },
    {
      name: '面积',
      data: 'value',
      position: 'right',
      min: 0,
      max: 100,
      interval: 20,
      splitLine: {
        show: false
      },
      axisLabel: {
        style:{
          fill:'#fff'
        },
        formatter: '{value} 平方米',
      },
      axisTick: {
        show: false
      }
    }
  ],
  series: [
    {
      name: '价格',
      data: [
        2235, 2646, 2011, 4133
      ],
      type: 'bar',
      gradient: {
        color: ['#37a2da', '#ffdb5c']
      },
      animationCurve: 'easeOutBounce'
    },
    {
      name: '面积',
      data: [
        35,39,56,82
      ],
      type: 'line',
      yAxisIndex: 1,
      animationCurve: 'easeOutBounce',
      color:'#ffdb5c'
    }
  ]
 })

</script>

<template>
  <dv-charts :option="option" style="width: 100%;height: 380px;"></dv-charts>
</template>

<style scoped>

</style>
