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
            <a class="nav-link" href="#" @click="onHome" >Home
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
          <li class="nav-item active">
            <a class="nav-link" href="#" @click="onLogIn()">Log in</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#" v-b-modal.event-modal>Sign up</a>
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
    <div class = 'container'>
      <div class = 'row justify-content-center'>
        <div class = 'content-table'>
          <div class  = 'content-table-cell'>
            <div class = 'col-5 login-container'>

             <div class = 'logo-container'>
               <img style="max-width: 150px" :src="require('../assets/logo.svg')">
             </div>

              <b-form ref="form" @submit="onSubmit">
                <b-form-group label-for="username-input">
                  <b-form-input id="username-input" v-model="loginForm.username" type="text" placeholder="Username" required>
                  </b-form-input>
                </b-form-group>

                <b-form-group label-for="password-input">
                  <b-form-input id="password-input" v-model="loginForm.password" type="password" placeholder="Password" required>
                  </b-form-input>
                </b-form-group>

                <b-button type="submit" variant="primary" class='btn-login' >Login</b-button>
              </b-form>

            </div>
          </div>
        </div>

      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      name: 'Login',
      logged: false,
      token: '',
      find_match: false,
      is_admin: false,
      loginForm: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    checkLogin () {
      const parameters = {
        username: this.loginForm.username,
        password: this.loginForm.password
      }
      const path = `http://localhost:8080/login`
      axios.post(path, parameters)
        .then((res) => {
          this.logged = true
          this.token = res.data.token
          this.getAccount()
          alert('User correctly logged')
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
          this.user = ''
          alert('Username or Password incorrect')
        })
    },
    onHome () {
      this.$router.replace({ path: '/' })
    },
    onAboutUs () {
      this.$router.replace({ path: '/about_us' })
    },
    getAccount () {
      const pathJobseeker = `http://localhost:8080/jobseeker/${this.username}` // to change check endpoints backend
      axios.get(pathJobseeker)
        .then((res) => {
          this.is_admin = res.data.account.is_admin !== 0
          alert('Sign in done. Welcome ' + this.username + '!')
          this.$router.replace({ path: '/', query: { username: this.username, logged: this.logged, is_admin: this.is_admin, token: this.token } })
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
          // to change: now check for companies
        })

      const pathCompany = `http://localhost:8080/company/${this.username}` // to change check endpoints backend
      axios.get(pathCompany)
        .then((res) => {
          this.is_admin = res.data.account.is_admin !== 0
          alert('Sign in done. Welcome ' + this.username + '!')
          this.$router.replace({ path: '/', query: { username: this.username, logged: this.logged, is_admin: this.is_admin, token: this.token } })
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
          alert('There is no jobseeker or company with this username')
          // to change: now check for companies
        })
    },

    initForm () {
      this.loginForm.username = ''
      this.loginForm.password = ''
    }
  }
}
</script>
<style scoped>
</style>
