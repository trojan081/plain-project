import { createApp } from 'vue'
import { MotionPlugin } from '@vueuse/motion'
import App from './App.vue'
import i18n from './i18n'
import './styles.css'
import router from './router'
import axios from 'axios'

axios.defaults.withCredentials = true


const app = createApp(App)
app.use(MotionPlugin)
app.use(i18n)  
app.use(router)
app.mount('#app')
app.config.globalProperties.$axios = axios
