import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import UserProfile from '@/components/UserProfile'
import JobPostings from '@/components/JobPostings'
import AboutUs from '@/components/AboutUs'
import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/user',
      name: 'UserProfile',
      component: UserProfile
    },
    {
      path: '/job_postings',
      name: 'JobPostings',
      component: JobPostings
    },
    {
      path: '/about_us',
      name: 'AboutUs',
      component: AboutUs
    }
  ]
})
