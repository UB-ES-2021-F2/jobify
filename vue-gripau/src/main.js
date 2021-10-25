import {BootstrapVue, BootstrapVueIcons} from 'bootstrap-vue'
import '@/../bootstrap/css/bootstrap.css'
import '@/../src/assets/styles/login.css'
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// Veevalidate imports
import {
  ValidationObserver,
  ValidationProvider,
  extend,
  localize
} from 'vee-validate'
import en from 'vee-validate/dist/locale/en.json'
import * as rules from 'vee-validate/dist/rules'

// Install VeeValidate rules and localization
Object.keys(rules).forEach(rule => {
  extend(rule, rules[rule])
})

localize('en', en)

// Install VeeValidate components globally
Vue.component('ValidationObserver', ValidationObserver)
Vue.component('ValidationProvider', ValidationProvider)

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.config.productionTip = false

Vue.prototype.$API_BASE_URL = 'http://localhost:5000/api/'
// Vue.prototype.$API_BASE_URL = 'https://ub-jobify.herokuapp.com/api/'

new Vue({
  router,
  store,
  render: (h) => h(App)
}).$mount('#app')
