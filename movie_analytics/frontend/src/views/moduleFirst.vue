<script setup>
 import Scrollboard from './chart/scrollboard.vue';
 import Piechart from './chart/piechart.vue';
 import Radarchart from './chart/radarchart.vue'
 import Gaugechart from './chart/gaugechart.vue';
import Capsulechart from './chart/capsulechart.vue';
import Water from './chart/water.vue';

 
</script>

<template>
 <div class="module-box">
      <div style="flex:0 1 20%">
        <Piechart/>
      </div>

      <div style="flex:0 1 20%">
        <Radarchart/>
      </div>

      <div style="flex:0 1 40%">
        <div demo-bg>
          <dv-border-box8 :dur="5" style="width: 100%;height: 380px;">
            <Gaugechart></Gaugechart>
            <div class="d-flex" style="height:200px; padding: 0 20px;">
              <Capsulechart></Capsulechart>
              <div style="flex: 1;padding-top: 30px;" ><Water></Water></div>
            </div>
          </dv-border-box8>
          </div>
      </div>
      
      <div style="flex:0 1 20%">
        <Scrollboard />
      </div>
    </div>
</template>

<style scoped>

</style>
