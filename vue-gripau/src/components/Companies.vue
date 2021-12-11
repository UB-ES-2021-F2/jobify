<template>
  <div id="app">

    <!--Navbar -->
    <b-navbar sticky toggleable="lg" type="light" variant="light">
      <b-navbar-brand id="logoNavbar" href="#" @click="onHome()">
        <img style="max-width: 150px" :src="require('../assets/logo.svg')">
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item id="homeNavbarButton" @click="onHome()">Home</b-nav-item>
          <b-nav-item id="jobPostingsNavbarButton" @click="onJobPostings()">Job postings</b-nav-item>
          <b-nav-item id="companiesNavbarButton" active>Companies</b-nav-item>
          <b-nav-item id="aboutUsNavbarButton" @click="onAboutUs()">About Us</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="!logged" class="ml-auto">
          <b-nav-item id="logInNavbarButton" @click="onLogIn()">Log in</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="logged" class="ml-auto">
          <b-nav-item id="profileNavbarButton" @click="onProfile()">{{ this.username }}</b-nav-item>
          <button id="logOutNavbarButton" class="btn btn-outline-danger" @click="onLogOut()"> Log Out </button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <!--/.Navbar -->

    <h2 style="font-family: 'Vollkorn', serif"> {{ message }} </h2>
    <div class="mx-2" id="companiesView">
      <b-container fluid id="searchContainer"  style="padding: 20px; align-self: center;
                                                font-family:'Work Sans SemiBold', Montserrat, sans-serif">
        <b-row align-h="center" id="searchTitleRow" class="mb-1">
          <p class="text-center" style="font-size: 22px">Find your ideal company!</p>
        </b-row>
        <b-row align-h="center" id="searchContentRow" class="mb-2" style="font-family:'Work Sans', sans-serif">
          <b-row id="searchSearchbarRow">
            <b-input id="searchbar" type="text" length=60 v-model="search"
                     placeholder="Search company...   "
                     style="border-radius: 0 !important" />
          </b-row>
          <b-button id="searchButton" variant="warning" @click="searchCompanies">
            Search!
          </b-button>
        </b-row>
      </b-container>
      <b-row style="margin-inline: 0">
        <b-col class="mb-4" align="center"  align-self="stretch" v-for="(company) in companies.slice((current_page-1)*per_page, current_page*per_page)" :key="company.id">
          <b-card
            tag="article"
            style="height: 100%; min-width: 350px; max-width: 500px; font-family: 'Work Sans SemiBold'"
            id="companyCard"
          >
            <b-container style="font-family: 'Work Sans'">
              <b-row align-v="center">
                <b-col align="left" cols="8">
                  <b-card-text id="companyName" >
                    <p class="titleCompanyCard">{{ company.company }}</p>
                  </b-card-text>
                  <b-col>
                    <b-icon id="emailIcon"  icon="envelope-fill"></b-icon> {{ company.email}}
                  </b-col>
                  <b-col lg v-if="company.sector !== 'Unknown'">
                    <b-icon id="sectorIcon" icon="inboxes-fill"></b-icon> {{ company.sector }}
                  </b-col>
                  <b-col lg v-if="company.location !== 'Unknown'">
                    <b-icon id="locationIcon" icon="geo-alt-fill"></b-icon> {{ company.location }}
                  </b-col>
                </b-col>
                <b-col align-v="center">
                  <img v-if="companies_logos[company.username]!=null" class="card-img" :src="companies_logos[company.username]" alt=""
                      style="max-width:128px; max-height:128px; border-radius: 128px">
                  <img v-if="companies_logos[company.username]==null" class="card-img" src="../assets/images/company_avatar.png" alt=""
                      style="max-width:128px; max-height:128px; border-radius: 128px; opacity: 0.3">
                </b-col>
              </b-row>
            </b-container>
          <b-button id="companyButton" class="btn btn-outline-light active" @click="onCompany(company.username)"
                    style="background-color:transparent; position: absolute; top:0; left:0; height: 100%; width:100%"></b-button>
          </b-card>
        </b-col>
      </b-row>
      <b-row style="margin-inline: 0" class="mt-4" align-h="center">
          <b-col align-self="center" cols="10">
            <b-pagination
              align="center"
              v-model = "current_page"
              :total-rows = "companies.length"
              :per-page = "per_page"
            >
            </b-pagination>
          </b-col>
      </b-row>
      <b-col align="center">
        Items per page:
      </b-col>
      <b-col class="pb-4" align-h="center">
        <b-form-select style="width:10%; min-width: 60px" v-model="per_page" :options="options" size="sm">Items per page:</b-form-select>
      </b-col>
    </div>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import Vue from 'vue'
import axios from 'axios'
import firebase from 'firebase/compat'

export default {
  data () {
    return {
      message: 'Companies',
      logged: false,
      username: '',
      is_admin: false,
      is_jobseeker: null,
      is_company: false,
      token: '',
      companies: [],
      companies_logos: {},
      loadedLogos: false,
      renderKey: 0,
      current_page: 1,
      options: [5, 10, 25, 50],
      per_page: 25,
      search: '',
      notFound: false,
      notFoundMessage: 'Oops, we did not find any company matching your search...'
    }
  },
  methods: {
    onProfile () {
      if (this.is_jobseeker && this.logged) {
        this.$router.push('/job_seeker/' + this.username)
      } else if (this.is_company && this.logged) {
        this.$router.push('/company/' + this.username)
      }
    },
    onLogIn () {
      this.$router.push('/login')
    },
    onHome () {
      this.$router.push('/')
    },
    onLogOut () {
      this.$store.commit('logout')
      this.$router.push('/')
      this.logged = false
      this.username = null
      this.token = null
      this.is_jobseeker = null
      this.is_company = null
      this.is_admin = null
    },
    onJobPostings () {
      this.$router.push('/job_postings')
    },
    onAboutUs () {
      this.$router.push('/about_us')
    },
    onCompany (username) {
      this.$router.push('/company/' + username)
    },
    getCompanies () {
      const path = Vue.prototype.$API_BASE_URL + 'companies'
      axios.get(path)
        .then((res) => {
          this.companies = res.data
          for (let c in this.companies) {
            let comp = this.companies[c]
            this.companies_logos[comp.username] = null
          }
          this.getCompaniesLogos()
        })
        .catch((error) => {
          console.error(error)
        })
    },
    getCompaniesLogos () {
      for (let c in this.companies) {
        let comp = this.companies[c]
        this.companies_logos[comp.username] = null
        firebase.storage().ref(`images/${comp.username}/avatar`).getDownloadURL()
          .then((url) => {
            this.companies_logos[comp.username] = url
            this.$forceUpdate()
          })
          .catch(() => {
            console.log('This avatar does not exist yet')
          })
      }
      this.loadedLogos = true
      this.$forceUpdate()
    },
    searchCompanies () {
      const path = Vue.prototype.$API_BASE_URL + 'companies'
      let searchParams = {}
      if ((this.search === '')) {
        searchParams = {params: {}}
      } else if ((this.search !== '')) {
        searchParams = {params: {'keyword': this.search}}
      }

      axios.get(path, searchParams)
        .then((res) => {
          this.companies = []
          this.companies = res.data
          for (let c in this.companies) {
            let comp = this.companies[c]
            this.companies_logos[comp.username] = null
          }
          this.getCompaniesLogos()
          if (this.companies.length > 0) {
            this.notFound = false
          } else {
            this.notFound = true
          }
        })
        .catch((error) => {
          console.error(error)
        })
    }
  },
  created () {
    this.logged = this.$store.state.logged
    this.username = this.$store.state.username
    this.is_jobseeker = this.$store.state.isJobSeeker
    this.is_company = this.$store.state.isCompany
    this.token = this.$store.state.token
    this.is_admin = this.$store.state.isAdmin
    this.getCompanies()
  },
  computed: mapState({
    token: state => state.token,
    logged: state => state.logged,
    username: state => state.username,
    isJobSeeker: state => state.isJobSeeker,
    isCompany: state => state.isCompany,
    isAdmin: state => state.isAdmin
  })
}

</script>

<style>
.navbar.navbar-light{
  font-family: "Work Sans SemiBold", Montserrat, sans-serif;
  font-size: 18px;
  padding: 20px;
  margin-bottom: 20px;
}
.titleCompanyCard{
  font-family: "Work Sans SemiBold", Montserrat, sans-serif;
  font-weight: bold;
  font-size: 24px;
  margin-bottom: 0.3rem;
}
.page-item.active .page-link {
  background-color: #ffc107 !important;
  border-color: #ffc107 !important;
}
.page-link {
  font-family: "Work Sans SemiBold", Montserrat, sans-serif;
  color: #ffc107;
}
</style>
