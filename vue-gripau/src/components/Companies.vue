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
    <b-container fluid>
      <b-row align-h="center" v-for="(company) in companies" :key="company.id">
        <b-card
          tag="article"
          class="mb-2"
          style="width: 90%; max-width: 600px; font-family: 'Work Sans SemiBold'"
          align="left"
          id="companyCard"
        >
          <div class="row no-gutters">
              <b-container fluid style="font-family: 'Work Sans'">
                <b-row no gutters>
                  <b-col cols="8">
                    <b-card-text id="companyName" >
                      <p class="titleCompanyCard">{{ company.company }}</p>
                    </b-card-text>
                    <b-col lg>
                      <b-icon id="emailIcon" icon="envelope"></b-icon> {{company.email}}
                    </b-col>
                    <b-col lg v-if="company.sector !== 'Unknown'">
                      <b-icon id="sectorIcon" icon="building"></b-icon> {{ company.sector }}
                    </b-col>
                    <b-col lg v-if="company.location !== 'Unknown'">
                      <b-icon id="locationIcon" icon="geo-alt-fill"></b-icon> {{ company.location }}
                    </b-col>
                  </b-col>
                  <b-col v-if="companies_logos[company.username]!=null" cols="4">
                    <img v-if="loadedLogos" class="card-img" :src="companies_logos[company.username]" alt=""
                         style="width:128px;height:128px">
                  </b-col>
                  <b-col v-if="companies_logos[company.username]==null" cols="4">
                    <img class="card-img" src="../assets/images/company_avatar.png" alt=""
                         style="width:128px;height:128px">
                  </b-col>
                </b-row>
              </b-container>
            <b-button id="companyButton" class="btn btn-outline-light active" @click="onCompany(company.username)"
                      style="background-color:transparent; position: absolute; top:0; left:0; height: 100%; width:100%"></b-button>
          </div>
        </b-card>
      </b-row>
    </b-container>
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
      renderKey: 0
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
</style>
