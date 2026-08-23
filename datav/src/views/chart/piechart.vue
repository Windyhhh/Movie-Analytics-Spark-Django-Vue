<script setup>

import { onMounted, ref } from 'vue';
import { useDataStore } from '../../stores/data';
const dataStore = useDataStore()
let pinjun = 0
let pinjunsh = 0
let pinjunsz = 0
let pinjunbj = 0
let pinjungz = 0
let totalPrice = ref(0)
let totalPricesh = ref(0)
let totalPricebj = ref(0)
let totalPricegz = ref(0)
let totalPricesz = ref(0)
let countsh = 0
let countsz = 0
let countgz = 0
let countbj = 0
let count = 0
onMounted(()=>dataStore.getList())
setTimeout(()=>console.log(dataStore.dataList),1000)
for(let i = 0; i < dataStore.dataList.length; i++){
  let priceStr = dataStore.dataList[i].jiage.replace('元/月', '');
  let price = parseFloat(priceStr);  
  
  totalPrice.value += price;  
  count++; 
  if(dataStore.dataList[i].zufang == '上海'){
    let priceStrsh = dataStore.dataList[i].jiage.replace('元/月', '');
    let pricesh = parseFloat(priceStrsh); 
    console.log(priceStrsh,pricesh)
    totalPricesh.value += pricesh
    countsh++;
  }
  if(dataStore.dataList[i].zufang == '广州'){
    let priceStrgz = dataStore.dataList[i].jiage.replace('元/月', '');
    let pricegz = parseFloat(priceStrgz); 
    console.log(priceStrgz,pricegz)
    totalPricegz.value += pricegz
    countgz++;
  }
  if(dataStore.dataList[i].zufang == '深圳'){
    let priceStrsz = dataStore.dataList[i].jiage.replace('元/月', '');
    let pricesz = parseFloat(priceStrsz); 
    console.log(priceStrsz,pricesz)
    totalPricesz.value += pricesz
    countsz++;
  }
  if(dataStore.dataList[i].zufang == '北京'){
    let priceStrbj = dataStore.dataList[i].jiage.replace('元/月', '');
    let pricebj = parseFloat(priceStrbj); 
    console.log(priceStrbj,pricebj)
    totalPricebj.value += pricebj
    countbj++;
  }
}
setTimeout(()=>pinjun = totalPrice._value/count/(35+39+56+82)*4,2000)
setTimeout(()=>pinjunsh = totalPricesh._value/countsh/39,2000)
setTimeout(()=>pinjunbj = totalPricebj._value/countbj/35,2000)
setTimeout(()=>pinjunsz = totalPricesz._value/countsz/82,2000)
setTimeout(()=>pinjungz = totalPricegz._value/countgz/56,2000)
setTimeout(()=>console.log(pinjun.toFixed(2),pinjunsh.toFixed(2),pinjunsz.toFixed(2),pinjungz.toFixed(2),pinjunbj.toFixed(2)),2000)

const option = ref({
  title: {
    text: '房屋租赁平均价格/平方/月',
    style:{
      fill:'#fff',
      fontsize:14,
      
    }
  },
  color:['#37a2da','#32c5e9','#67e0e3','#9fe6b8','#96bfff'],
  series: [
    {
      type: 'pie',
      data: [
        { name: '平均-49.93', value: 49.93 },
        { name: '广州-35.92', value: 35.02 },
        { name: '深圳-50.40', value: 50.40 },
        { name: '上海-69.83', value: 69.83 },
        { name: '北京-66.72', value: 66.72 },
      ],
     
      insideLabel: {
        show: true
      },
      roseType: true,
      outsideLabel:{
        labelLineEndLength:5 //线长
      }
    }
  ]
})
//第一个
</script>

<template>
        <div demo-bg>
          <dv-border-box-12 style="width: 100%;height: 380px;padding:0 20px;">
            
              <dv-charts :option="option" style="width: 100%;height: 100%;"></dv-charts>
            
          </dv-border-box-12>
        </div>
 </template>