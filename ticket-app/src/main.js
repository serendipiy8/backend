import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import router from './router'
import './assets/css/reset.css'
import store from './store/index'
import './router/permission'
import "./utils/init"
import VueAwesomeSwiper from 'vue-awesome-swiper'
import 'swiper/css'
import axios from 'axios';


const app = createApp(App)
app.use(ElementPlus)
app.use(router)
app.mount('#app')
app.use(store)