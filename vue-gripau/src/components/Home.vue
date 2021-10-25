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
          <b-nav-item @click="onAboutUs()">About Us</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="!logged" class="ml-auto">
          <b-nav-item @click="onLogIn()">Log in</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="logged" class="ml-auto">
          <b-nav-item @click="onUserProfile()">{{ this.username }}</b-nav-item>
          <button class="btn btn-outline-danger" @click="onLogOut()"> Log Out </button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <!--/.Navbar -->

    <h2 style="font-family: 'Vollkorn', serif"> {{ message }} </h2>
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
    onUserProfile () {
      if (this.is_jobseeker & this.logged) {
        this.$router.replace({ path: '/job_seeker/' + this.username })
      }
    },
    onLogIn () {
      this.$router.replace({path: '/login'})
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
</style>
