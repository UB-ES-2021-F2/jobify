<template>
  <div id="app">

    <!--Navbar -->
    <b-navbar sticky toggleable="lg" type="light" variant="light">
      <b-navbar-brand href="#" @click="onHome()">
        <img style="max-width: 150px" :src="require('../assets/logo.svg')">
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item @click="onHome()">Home</b-nav-item>
          <b-nav-item @click="onJobPostings()">Job postings</b-nav-item>
          <b-nav-item active>Companies</b-nav-item>
          <b-nav-item @click="onAboutUs()">About Us</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="!logged" class="ml-auto">
          <b-nav-item @click="onLogIn()">Log in</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="logged" class="ml-auto">
          <b-nav-item @click="onProfile()">{{ this.username }}</b-nav-item>
          <button class="btn btn-outline-danger" @click="onLogOut()"> Log Out </button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <!--/.Navbar -->

    <h2 style="font-family: 'Vollkorn', serif"> {{ message }} </h2>
    <b-container fluid>
      <b-row align-h="center" v-for="(company) in companies" :key="company.id">
        <b-card
          :title="company.company"
          tag="article"
          class="mb-2"
          style="width: 90%; max-width: 600px; font-family: 'Work Sans SemiBold'"
          align="left"
        >
          <b-button class="btn btn-outline-light active" @click="onCompany(company.username)" style="background-color:transparent; position: absolute; top:0; left:0; height: 100%; width:100%"></b-button>
          <footer>
            <b-container fluid style="font-family: 'Work Sans'">
              <b-row>
                <b-col cols="4">
                  <b-icon icon="envelope"></b-icon> {{company.email}}
                </b-col>
                <b-col cols="4" v-if="company.sector !== 'Unknown'">
                  <b-icon icon="building"></b-icon> {{ company.sector }}
                </b-col>
                <b-col cols="4" v-if="company.location !== 'Unknown'">
                  <b-icon icon="geo-alt-fill"></b-icon> {{ company.location }}
                </b-col>
              </b-row>
            </b-container>
          </footer>
        </b-card>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import Vue from 'vue'
import axios from 'axios'

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
      companies: []
    }
  },
  methods: {
    onProfile () {
      if (this.is_jobseeker && this.logged) {
        this.$router.replace({ path: '/job_seeker/' + this.username })
      } else if (this.is_company && this.logged) {
        this.$router.replace({path: '/company/' + this.username})
      }
    },
    onLogIn () {
      this.$router.replace({path: '/login'})
    },
    onHome () {
      this.$router.replace({ path: '/' })
    },
    onLogOut () {
      this.$store.commit('logout')
      this.$router.replace({path: '/'})
      this.logged = false
      this.username = null
      this.token = null
      this.is_jobseeker = null
      this.is_company = null
      this.is_admin = null
    },
    onJobPostings () {
      this.$router.replace({ path: '/job_postings' })
    },
    onAboutUs () {
      this.$router.replace({ path: '/about_us' })
    },
    onCompany (username) {
      this.$router.replace({ path: '/company/' + username })
    },
    getCompanies () {
      const path = Vue.prototype.$API_BASE_URL + 'companies'
      axios.get(path)
        .then((res) => {
          this.companies = res.data
          console.log(res.data)
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
</style>
