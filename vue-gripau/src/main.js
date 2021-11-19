import {BootstrapVue, BootstrapVueIcons} from 'bootstrap-vue'
import '@/../bootstrap/css/bootstrap.css'
import '@/../src/assets/styles/styles.css'
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// Import the functions you need from the SDKs you need
import firebase from 'firebase/compat/app'

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
  render: (h) => h(App),
  created () {
    // Your web app's Firebase configuration
    var firebaseConfig = {
      apiKey: 'AIzaSyAvkUYwd-EUzWggK1e4864PBKZ8youpnGQ',
      authDomain: 'gripau-8cd1b.firebaseapp.com',
      projectId: 'gripau-8cd1b',
      storageBucket: 'gripau-8cd1b.appspot.com',
      messagingSenderId: '238784150968',
      appId: '1:238784150968:web:8c60da0985eb474b2d234d'
    }

    // Initialize Firebase
    /* eslint-disable */
    const app = firebase.initializeApp(firebaseConfig)
  }
}).$mount('#app')
