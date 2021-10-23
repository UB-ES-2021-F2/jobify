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
          <b-nav-item @click="onJobPostings()">Job postings</b-nav-item>
          <b-nav-item @click="onAboutUs()">About Us</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="!logged" class="ml-auto">
          <b-nav-item @click="onLogIn()">Log in</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="logged" class="ml-auto">
          <b-nav-item active >{{ this.username }}</b-nav-item>
          <button class="btn btn-outline-danger" @click="onLogOut()"> Log Out </button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <!--/.Navbar -->

    <b-container>

      <h2 style="font-family: 'Vollkorn', serif"> {{ company.company }} </h2>

      <div class="container-md-5 p-2 align-items-center">
        <div class="bio-text">
          {{bio}}
        </div>

        <div class="text-left p-2 pb-3" style="max-width: 50rem">
          <p class="section-title"> Work experience </p>
        </div>

        <div class="text-left p-2 pb-3" style="max-width: 50rem">
          <p class="section-title"> Education </p>
        </div>

        <div class="text-left p-2 pb-3" style="max-width: 50rem">
          <p class="section-title"> Skills </p>
        </div>
      </div>

    </b-container>
  </div>
</template>

<script>
import axios from 'axios'
import Vue from 'vue'

export default {
  data () {
    return {
      company: {
        company: '',
        email: '',
        description: '',
        job_offers: '',
        sector: '',
        location: ''
      },
      logged: false,
      is_jobseeker: true,
      is_company: false,
      is_admin: false,
      token: '',
      username: '',
      company_name_profile: '',
      edit_mode: false,
      bio: 'Example bio: I’ve always been a great problem solver, an independent introvert, and a technophile obsessed with the latest devices.\n' +
        'Today, I’m working from home as a software engineer for Google, and I get to show off all these elements of who I am.\n' +
        ' I’m also eager to meet other software engineers in the area, so feel free to connect!'
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
    onLogIn () {
      this.$router.replace({ path: '/login' })
    },
    onLogOut () {
      this.$router.replace({path: '/',
        query: {
          username: '',
          logged: false,
          is_company: false,
          is_jobseeker: true,
          is_admin: false,
          token: ''
        }
      })
    },
    onJobPostings () {
      this.$router.replace({ path: '/job_postings',
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
    onAboutUs () {
      this.$router.replace({ path: '/about_us',
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
    getCompany () {
      const pathCompany = Vue.prototype.$API_BASE_URL + 'company/' + this.company_name_profile.toLowerCase()
      axios.get(pathCompany)
        .then((res) => {
          console.log(res)
          this.company.company = res.data.account.company
          this.company.email = res.data.account.email
          this.company.description = res.data.account.description
          this.company.job_offers = res.data.account.job_offers
          this.company.location = res.data.account.location
        })
        .catch(() => {
          this.company.company = 'Name'
          this.company.email = 'Email'
          this.company.description = 'Description'
          this.company.job_offers = 'Job_offers'
          this.company.location = 'Location'
        })
    }
  },
  created () {
    this.company_name_profile = this.$route.path.split('company/')[1].toLowerCase()
    this.logged = this.$route.query.logged === 'true'
    this.username = this.$route.query.username ? this.$route.query.username : ''
    this.is_jobseeker = this.$route.query.is_jobseeker === 'true'
    this.is_company = this.$route.query.is_company === 'true'
    this.token = this.$route.query.token ? this.$route.query.token : ''
    this.is_admin = this.$route.query.is_admin === 'true'
    this.edit_mode = this.username === this.company_name_profile
    this.getCompany()
    // this.getWorkExperience()
    // this.getEducation()
  }
}

</script>

<style>
.navbar.navbar-light{
  font-family: "Work Sans SemiBold", Montserrat, sans-serif;
  font-size: 18px;
  padding: 20px;
  margin-bottom: 20px;
}
.bio-text {
  text-align: left;
  color: dimgray;
  font-size: 16px;
  padding-bottom: 20px;
}
.card-title-work {
  font-family: "Work Sans SemiBold", Montserrat, sans-serif;
  font-size: 20px;
}
.card-title-ed {
  font-family: "Work Sans SemiBold", Montserrat, sans-serif;
  font-size: 20px;
  padding-bottom: 10px;
}
.card-subtitle {
  font-family: "Work Sans SemiBold", Montserrat, sans-serif;
  font-size: 18px;
  padding-bottom: 5px;
}
.card-text {
  font-family: "Work Sans", sans-serif;
  font-size: 14px;
}
.section-title {
  font-family: "Vollkorn",serif;
  font-size: 26px;
  display:inline-block
}
</style>
