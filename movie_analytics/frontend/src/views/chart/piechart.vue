<template>
  <div class="pie-chart">
    <div v-if="props.data.length === 0" class="empty-data">
      <p>暂无数据</p>
    </div>
    <div v-else>
      <dv-charts
        :option="chartConfig"
        :style="{ width: '100%', height: '100%' }"
      />
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  data: {
    type: Array,
    default: () => []
  }
})

const chartConfig = computed(() => {
  // 确保数据是有效的数组
  const validData = props.data || []
  
  return {
    title: {
      text: '电影评分分布',
      textStyle: {
        color: '#333',
        fontSize: 16,
        fontWeight: 'bold'
      }
    },
    tooltip: {
      trigger: 'item',
      formatter: '{b}: {c} ({d}%)'
    },
    legend: {
      orient: 'vertical',
      right: 10,
      top: 'center',
      type: 'scroll',
      formatter: (name) => {
        const item = validData.find(item => item.name === name)
        return `${name}: ${item ? item.value : 0}`
      }
    },
    series: [{
      name: '评分分布',
      type: 'pie',
      radius: ['40%', '70%'],
      avoidLabelOverlap: false,
      itemStyle: {
        borderRadius: 8,
        borderColor: '#fff',
        borderWidth: 2
      },
      label: {
        show: false,
        position: 'center'
      },
      emphasis: {
        label: {
          show: true,
          fontSize: '18',
          fontWeight: 'bold'
        }
      },
      labelLine: {
        show: false
      },
      data: validData
    }]
  }
})
</script>

<style scoped>
.pie-chart {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.empty-data {
  text-align: center;
  color: '#999';
  font-size: 16px;
}
</style>