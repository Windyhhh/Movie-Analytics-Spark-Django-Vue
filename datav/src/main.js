import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router/index.js'
import DataVVue3 from '@kjgl77/datav-vue3'
import './assets/css/index.css'
import '@/assets/font/iconfont.css'
import { createPinia } from 'pinia'


const pinia = createPinia()
const app = createApp(App)
app.use(DataVVue3).use(pinia).mount('#app')
