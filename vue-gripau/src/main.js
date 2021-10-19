import {BootstrapVue, BootstrapVueIcons} from 'bootstrap-vue'
import '@/../bootstrap/css/bootstrap.css'
import '@/../src/assets/styles/login.css'
import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.config.productionTip = false

// Vue.prototype.$API_BASE_URL = 'http://localhost:5000/api/'
Vue.prototype.$API_BASE_URL = 'https://ub-jobify.herokuapp.com/api/'

new Vue({
  router,
  render: (h) => h(App)
}).$mount('#app')
