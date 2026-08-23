<template>
  <div class="line-chart">
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
      text: '电影年份趋势',
      textStyle: {
        color: '#333',
        fontSize: 16,
        fontWeight: 'bold'
      }
    },
    tooltip: {
      trigger: 'axis'
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
      type: 'line',
      smooth: true,
      lineStyle: {
        color: '#f5576c',
        width: 3
      },
      itemStyle: {
        color: '#f5576c'
      },
      areaStyle: {
        color: {
          type: 'linear',
          x: 0,
          y: 0,
          x2: 0,
          y2: 1,
          colorStops: [{
            offset: 0, color: 'rgba(245, 87, 108, 0.3)'
          }, {
            offset: 1, color: 'rgba(245, 87, 108, 0.05)'
          }]
        }
      },
      symbol: 'circle',
      symbolSize: 6
    }]
  }
})
</script>

<style scoped>
.line-chart {
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