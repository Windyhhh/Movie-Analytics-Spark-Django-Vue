<template>
  <div class="bar-chart">
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
      text: '电影类型分布',
      textStyle: {
        color: '#333',
        fontSize: 16,
        fontWeight: 'bold'
      }
    },
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      }
    },
    xAxis: {
      type: 'category',
      data: validData.map(item => item.name),
      axisLabel: {
        rotate: 30,
        fontSize: 12
      }
    },
    yAxis: {
      type: 'value',
      name: '电影数量',
      nameTextStyle: {
        fontSize: 12
      }
    },
    series: [{
      data: validData.map(item => item.value),
      type: 'bar',
      itemStyle: {
        color: '#667eea',
        borderRadius: [4, 4, 0, 0]
      },
      label: {
        show: true,
        position: 'top',
        fontSize: 10,
        color: '#333'
      }
    }]
  }
})
</script>

<style scoped>
.bar-chart {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.empty-data {
  text-align: center;
  color: #999;
  font-size: 16px;
}
</style>