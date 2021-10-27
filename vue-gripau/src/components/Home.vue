<template>
  <div id="app">

    <!--Navbar -->
    <b-navbar sticky toggleable="lg" type="light" variant="light">
      <b-navbar-brand href="#">
        <img style="max-width: 150px" :src="require('../assets/logo.svg')">
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item active href="#">Home</b-nav-item>
          <b-nav-item @click="onJobPostings()">Job postings</b-nav-item>
          <b-nav-item @click="onCompanies()">Companies</b-nav-item>
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

    <div class="container-sm pt-5 align-items-center">
      <div class="container" style="max-width: 900px">
        <div class="container pl-5 pr-5 p-2" style="font-size:11vmin;line-height: 80%;font-family:'Bright', serif">
          Welcome to Jobify!
        </div>
        <img class="img-fluid" src="../assets/images/working_image_vector.svg">

        <div class="container mt-5">
            <span style="white-space: nowrap">
                <b-button btn variant="primary" class='btn-home' @click="onJobPostings">Find the newest jobs</b-button>
            </span>
          <span style="white-space: nowrap">
                <b-button variant="primary" class='btn-home' @click="onCompanies">Check our companies</b-button>
            </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapState} from 'vuex'

export default {
  data () {
    return {
      message: 'Home',
      logged: false,
      username: '',
      is_admin: false,
      is_jobseeker: null,
      is_company: false,
      token: ''
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
    onCompanies () {
      this.$router.replace({ path: '/companies' })
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
    }
  },
  created () {
    this.logged = this.$store.state.logged
    this.username = this.$store.state.username
    this.is_jobseeker = this.$store.state.isJobSeeker
    this.is_company = this.$store.state.isCompany
    this.token = this.$store.state.token
    this.is_admin = this.$store.state.isAdmin
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
.btn-home{
  margin: 10px;
  font-size: 1em;
  font-family: "Work Sans SemiBold", Montserrat, sans-serif;
  background-color: #ffc107;
  color:#000000;
  border: 0;
  border-radius: 5px;
}
.btn-home:focus{
  outline: none;
}
.btn-home:hover{
  background-color: #ffc107;
}
</style>
