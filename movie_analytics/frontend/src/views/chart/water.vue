<script setup>
import { onMounted, ref } from 'vue';
import { useDataStore } from '../../stores/data';
const dataStore = useDataStore()
const config = ref({
  data:[55,45],
  shape:'roundRect'
})

</script>

<template>
  <dv-water-level-pond :config="config" style="width: 100%;height: 150px; "></dv-water-level-pond>
</template>

<style scoped>

</style>
