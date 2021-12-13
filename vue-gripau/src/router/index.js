import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import JobSeekerProfile from '@/components/JobSeekerProfile'
import JobPostings from '@/components/JobPostingList'
import AboutUs from '@/components/AboutUs'
import Login from '@/components/Login'
import CompanyProfile from '@/components/CompanyProfile'
import JobPosting from '@/components/JobPosting'
import Companies from '@/components/Companies'

Vue.use(Router)

export default new Router({
  // mode: 'history',
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
      path: '/job_seeker/:username',
      name: 'JobSeeker',
      component: JobSeekerProfile
    },
    {
      path: '/company/:companyname',
      name: 'Company',
      component: CompanyProfile
    },
    {
      path: '/job_postings',
      name: 'JobPostings',
      component: JobPostings
    },
    {
      path: '/job_posting/:jobid',
      name: 'JobPosting',
      component: JobPosting
    },
    {
      path: '/companies',
      name: 'Companies',
      component: Companies
    },
    {
      path: '/about_us',
      name: 'AboutUs',
      component: AboutUs
    }
  ]
})
