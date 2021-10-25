<template>
  <div id="app">
    <!--Navbar -->
    <b-navbar sticky toggleable="lg" type="light" variant="light">
      <b-navbar-brand @click="onHome()">
        <img style="max-width: 150px" :src="require('../assets/logo.svg')">
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item @click="onHome()">Home</b-nav-item>
          <b-nav-item active>Job postings</b-nav-item>
          <b-nav-item @click="onCompanies()">Companies</b-nav-item>
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

    <h2 style="font-family: 'Vollkorn"> {{ message }} </h2>
    <b-container fluid>
      <b-row align-h="center" v-for="(job_offer) in job_offers" :key="job_offer.id">
        <b-card
          :title="job_offer.jobName"
          tag="article"
          class="mb-2"
          style="width: 90%; max-width: 600px"
          align="left"
        >
          <b-card-text>
            {{ job_offer.description }}
          </b-card-text>
          <footer>
            <b-icon icon="alarm"></b-icon> {{ job_offer.type}}
            <b-icon icon="building"></b-icon> {{ job_offer.company}}
          </footer>
        </b-card>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import {mapState} from 'vuex'

export default {
  data () {
    return {
      message: 'Job Postings',
      logged: false,
      job_offers: [{'id': 0, 'jobName': 'Waiter', 'company': 'Terra Restaurant', 'description': 'This offer is fake and it will be deleted in the next update', 'type': 'Part time'}, {'id': 1, 'jobName': 'Journalist', 'company': 'The Sun', 'description': 'This offer is fake and it will be deleted in the next update', 'type': 'Part time'}],
      username: '',
      token: '',
      is_jobseeker: true,
      is_company: false,
      is_admin: false
    }
  },
  methods: {
    onHome () {
      this.$router.replace({ path: '/' })
    },
    onUserProfile () {
      if (this.is_jobseeker & this.logged) {
        this.$router.replace({ path: '/job_seeker/' + this.username })
      }
    },
    onLogIn () {
      this.$router.replace({ path: '/login' })
    },
    onCompanies () {
      this.$router.replace({ path: '/companies' })
    },
    onLogOut () {
      this.$store.commit('logout')
      this.$router.replace({ path: '/' })
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
