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
          <li class="nav-item active">
            <a class="nav-link" href="#">Home
              <span class="sr-only">(current)</span>
            </a>
          </li>
          <li class="nav-item">
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
            <a class="nav-link" href="#" @click="onUserProfile()">User</a>
          </li>
          <button class="btn btn-outline-danger" @click="onLogOut()"> Log Out </button>
        </ul>
      </div>
    </nav>
    <!--/.Navbar -->

    <h1 style="font-family: 'Vollkorn"> {{ message }} </h1>
  </div>
</template>

<script>
export default {
  data () {
    return {
      message: 'Home',
      logged: false,
      username: '',
      is_admin: false,
      is_jobseeker: true,
      is_company: false,
      token: ''
    }
  },
  methods: {
    onUserProfile () {
      this.$router.replace({ path: '/user',
        query: {
          username: this.loginForm.username,
          logged: this.logged,
          is_company: true,
          is_jobseeker: false,
          is_admin: this.is_admin,
          token: this.token
        }
      })
    },
    onLogIn () {
      this.$router.replace({path: '/login'})
    },
    onLogOut () {
      this.logged = false
      this.username = ''
      this.token = ''
      this.is_jobseeker = true
      this.is_company = false
    },
    onAboutUs () {
      this.$router.replace({ path: '/about_us',
        query: {
          username: this.username,
          logged: this.logged,
          is_company: true,
          is_jobseeker: false,
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
  }
}

</script>
