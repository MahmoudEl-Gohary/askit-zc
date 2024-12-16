import './assets/css/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import VueSmoothScroll from 'vue3-smooth-scroll'


import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(VueSmoothScroll)
app.use(router)

app.mount('#app')
