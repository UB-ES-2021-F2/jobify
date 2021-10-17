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
          <b-nav-item active>About Us</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="!logged" class="ml-auto">
          <b-nav-item @click="onLogIn()">Log in</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="logged" class="ml-auto">
          <b-nav-item @click="onUserProfile()"><span class="user-link">{{ this.username }}</span></b-nav-item>
          <button class="btn btn-outline-danger" @click="onLogOut()"> Log Out </button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <!--/.Navbar -->

    <h2 style="font-family: 'Vollkorn', serif"> {{ message }} </h2>
  </div>
</template>

<script>

export default {
  data () {
    return {
      name: 'Name Surname',
      message: 'About Us',
      logged: false,
      username: '',
      is_admin: false,
      is_jobseeker: true,
      is_company: false,
      token: ''
    }
  },
  methods: {
    onHome () {
      this.$router.replace({path: '/',
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
      this.$router.replace({ path: '/about_us' })
      this.logged = false
      this.username = ''
      this.token = ''
      this.is_jobseeker = true
      this.is_company = false
      this.is_admin = false
    },
    onJobPostings () {
      this.$router.replace({path: '/job_postings',
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
.navbar.navbar-light.navbar-light{
  font-family: "Work Sans SemiBold";
  font-size: 18px;
  padding: 20px;
  margin-bottom: 20px;
}
.user-link {
  text-decoration: underline;
  text-decoration-color: #ffc107;
  text-decoration-thickness: 2px;
  text-underline-offset: 2px;
}
</style>
