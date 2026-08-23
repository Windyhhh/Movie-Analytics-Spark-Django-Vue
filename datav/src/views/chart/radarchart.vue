<script setup>
import { onMounted, ref } from 'vue';
import { useDataStore } from '../../stores/data';
const dataStore = useDataStore()
 const option= ref({
  title: {
    text: `房屋数量-149`,
    style:{
      fill:'#fff',
      fontsize:14,
      
    }
  },
  radar: {
    indicator: [
      { name: '北京', max: 70 },
      { name: '上海', max: 70 },
      { name: '广州', max: 70 },
      { name: '深圳', max: 70,},
    ],
    polygon: true,
    splitLine: {
      style: {
        stroke: 'rgba(159, 230, 184, 1)'
      }
    },
    axisLine: {
      style: {
        stroke: 'rgba(159, 230, 184, 1)'
      }
    },
    splitArea: {
      show: true,
      color: ['rgba(251, 114, 147, .2)', 'rgba(159, 230, 184, .2)']
    }
  },
  series: [
    {
      type: 'radar',
      data: [60, 37, 29, 23],
      animationCurve: 'easeInOutBack'
    }
  ]
})
</script>

<template>
  <dv-border-box-12 style="width: 100%;height: 380px;padding:0 20px;" >
          <dv-charts :option="option" style="width: 100%;height: 100%;"></dv-charts>
      </dv-border-box-12>
</template>

<style scoped>
</style>