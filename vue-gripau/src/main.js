import BootstrapVue from 'bootstrap-vue'
import '@/../bootstrap/css/bootstrap.css'
import '@/../src/assets/styles/login.css'
import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.use(BootstrapVue)
Vue.config.productionTip = false

new Vue({
  router,
  render: (h) => h(App)
}).$mount('#app')
