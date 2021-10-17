<template>
  <div id="app">
    <!--Navbar -->
    <nav class="mb-1 navbar navbar-expand-lg navbar-light bg-white py-4">
      <a class="navbar-brand">
        <img style="max-width: 150px" :src="require('../assets/logo.svg')">
      </a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent-333"
              aria-controls="navbarSupportedContent-333" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent-333" style="font-size:18px;
       font-family:'Work Sans SemiBold'">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <a class="nav-link" href="#" @click="onHome()">Home
              <span class="sr-only">(current)</span>
            </a>
          </li>
          <li class="nav-item active">
            <a class="nav-link" href="#">Job postings</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#" @click="onAboutUs()">About us</a>
          </li>
        </ul>
        <ul v-if="!logged" class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link" href="#" @click="onLogIn()">Log in</a>
          </li>
        </ul>
        <ul v-if="logged" class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link" href="#" @click="onUserProfile()">{{ this.username }}</a>
          </li>
          <button class="btn btn-outline-danger" @click="onLogOut()"> Log Out </button>
        </ul>
      </div>
    </nav>
    <!--/.Navbar -->

    <h1 style="font-family: 'Vollkorn"> {{ message }} </h1>
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
      this.$router.replace({ path: '/',
        query: {
          username: this.username,
          logged: this.logged,
          is_company: this.is_company,
          is_jobseeker: this.is_jobseeker,
          is_admin: this.is_admin,
          token: this.token
        }
      })
    },
    onUserProfile () {
      this.$router.replace({ path: '/user',
        query: {
          username: this.username,
          logged: this.logged,
          is_company: this.is_company,
          is_jobseeker: this.is_jobseeker,
          is_admin: this.is_admin,
          token: this.token
        }
      })
    },
    onLogIn () {
      this.$router.replace({ path: '/login' })
    },
    onLogOut () {
      this.$router.replace({ path: '/job_postings' })
      this.logged = false
      this.username = ''
      this.token = ''
      this.is_jobseeker = true
      this.is_company = false
      this.is_admin = false
    },
    onAboutUs () {
      this.$router.replace({path: '/about_us',
        query: {
          username: this.username,
          logged: this.logged,
          is_company: this.is_company,
          is_jobseeker: this.is_jobseeker,
          is_admin: this.is_admin,
          token: this.token
        }
      })
    }
  },
  created () {
    this.logged = this.$route.query.logged === 'true'
    this.username = this.$route.query.username ? this.$route.query.username : ''
    this.is_jobseeker = this.$route.query.is_jobseeker === 'true'
    this.is_company = this.$route.query.is_company === 'true'
    this.token = this.$route.query.token ? this.$route.query.token : ''
    this.is_admin = this.$route.query.is_admin === 'true'
  }
}
</script>

<style scoped>

</style>
