import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    logged: false,
    token: null,
    isJobSeeker: null,
    isCompany: null,
    isAdmin: null,
    username: null
  },
  mutations: {
    login (state, storeData) {
      state.logged = true
      state.token = storeData.token
      state.username = storeData.username
      state.isJobSeeker = storeData.isJobSeeker
      state.isCompany = storeData.isCompany
      state.isAdmin = storeData.isAdmin
    },
    logout (state) {
      state.logged = false
      state.token = null
      state.isJobSeeker = null
      state.username = null
      state.isCompany = null
      state.isAdmin = null
    }
  },
  plugins: [createPersistedState()]
})
