<template>
  <div class="scatter-chart">
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
      text: '评分与投票数关系',
      textStyle: {
        color: '#333',
        fontSize: 16,
        fontWeight: 'bold'
      }
    },
    tooltip: {
      trigger: 'item',
      formatter: (params) => {
        return `${params.data.name}<br/>评分: ${params.data.x}<br/>投票数: ${params.data.y.toLocaleString()}`
      }
    },
    xAxis: {
      type: 'value',
      name: '评分',
      nameTextStyle: {
        fontSize: 12
      },
      min: 8.0,
      max: 9.5
    },
    yAxis: {
      type: 'value',
      name: '投票数',
      nameTextStyle: {
        fontSize: 12
      }
    },
    series: [{
      name: '评分与投票数',
      type: 'scatter',
      data: validData,
      symbolSize: 6,
      itemStyle: {
        color: '#4facfe',
        opacity: 0.7
      }
    }]
  }
})
</script>

<style scoped>
.scatter-chart {
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