import './assets/css/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:8000'

const app = createApp(App)
const pinia = createPinia();

app.use(createPinia())
app.use(router)

app.mount('#app')
