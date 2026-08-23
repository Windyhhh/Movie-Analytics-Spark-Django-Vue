<script setup>
 import { ref } from 'vue';
 import Barchart from './chart/barchart.vue';
 import Linechart from './chart/linechart.vue';
 import scrollboard from './chart/scrollboard.vue';
</script>

<template>
  <div class="d-flex">
    <div style="flex:0 1 50%">
    <dv-border-box-13 style="width: 100%;height: 350px;">
      <Barchart></Barchart>
      <!-- <scrollboard></scrollboard> -->
    </dv-border-box-13>
  </div>
   
  <div style="flex:0 1 50%">
    <dv-border-box-12 style="width:100%;height: 350px;">
      <Linechart></Linechart>
    </dv-border-box-12>
  </div>
  </div>
</template>

<style scoped>

</style>
