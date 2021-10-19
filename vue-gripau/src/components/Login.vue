<template>
  <div id="app">
    <!--Navbar -->
    <b-navbar sticky toggleable="lg" type="light" variant="light">
      <b-navbar-brand href="#" @click="onHome">
        <img style="max-width: 150px" :src="require('../assets/logo.svg')">
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item active href="#">Home</b-nav-item>
          <b-nav-item @click="onJobPostings()">Job postings</b-nav-item>
          <b-nav-item @click="onAboutUs()">About Us</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <!--/.Navbar -->

    <div class = 'container'>
      <div class = 'row justify-content-center'>
        <div class = 'content-table'>
          <div class  = 'content-table-cell'>
            <div class = 'col-9 col-md-5 login-container'>

             <div class = 'logo-container'>
               <img style="max-width: 150px" :src="require('../assets/logo.svg')">
             </div>

              <b-form ref="form" @submit.prevent="checkLogin">
                <b-form-group label-for="username-input">
                  <b-form-input id="username-input" v-model="loginForm.username" type="text" placeholder="Username" required>
                  </b-form-input>
                </b-form-group>

                <b-form-group label-for="password-input">
                  <b-form-input id="password-input" v-model="loginForm.password" type="password" placeholder="Password" required>
                  </b-form-input>
                </b-form-group>
                <div>
                  <b-button type="submit" variant="primary" class='btn-login' >Login</b-button>
                </div>
                <div class="signup-container">
                  You don't have an account?<b-button v-b-modal.register-modal variant="secondary" class='btn-signup'>Sign Up</b-button>
                </div>
              </b-form>

            </div>
          </div>
        </div>

      </div>
    </div>
    <b-modal ref="registerModal"
             id="register-modal"
             title="Become a member"
             hide-footer
    >
      <b-tabs v-model="tabIndex" content-class="mt-3" fill>
        <!--Job Seeker form -->
        <b-tab title="Job Seeker" active>
          <b-form style="font-family:'Work Sans'" @submit.prevent="onSubmit">
            <label style="color: #5a6268">All fields are needed.</label>

            <b-form-group id="input-group-0" label="Username:" label-for="input-0">
              <b-form-input v-model="registerS.username" placeholder="" type="text" required></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-2" label="Email:" label-for="input-2">
              <b-form-input v-model="registerS.email" placeholder="" type="email" required></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-3" label="Password:" label-for="input-3">
              <b-form-input v-model="registerS.password" placeholder="" type="password" required></b-form-input>
              <b-form-text id="password-help-block">
                Your password should be 8-20 characters long.
              </b-form-text>
            </b-form-group>

            <b-form-checkbox id="checkbox-1" :state="termsAndCStateS" v-model="registerS.rTandC" name="checkbox-1" required>
              I have read and accept the terms and conditions and privacy policy.
            </b-form-checkbox>

            <b-form-checkbox id="checkbox-2" v-model="registerS.newsletter" name="checkbox-2">
              I do not want to receive the Jungle Newsletter and tips to optimise my job search.
            </b-form-checkbox>

            <div class="d-grid gap-2 d-md-flex justify-content-md-end">
              <button class="btn btn-warning justify-content-md-end">Submit</button>
            </div>
          </b-form>
        </b-tab>
        <!--/Job Seeker form -->
        <!--Company form -->
        <b-tab disabled title="Company (coming soon)">
          <b-form style="font-family:'Work Sans'" @submit.prevent="onSubmit" >
            <label style="color: #5a6268">All fields are needed.</label>

            <b-form-group id="input-group-0C" label="Company name:" label-for="input-0C">
              <b-form-input v-model="registerC.company" placeholder="" type="text" required></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-2C" label="Email:" label-for="input-2C">
              <b-form-input v-model="registerC.email" placeholder="" type="email" required></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-3C" label="Password:" label-for="input-3C">
              <b-form-input v-model="registerC.password" placeholder="" type="password" required></b-form-input>
              <b-form-text id="password-help-blockC">
                Your password should be 8-20 characters long.
              </b-form-text>
            </b-form-group>

            <b-form-checkbox id="checkbox-1C" :state="termsAndCStateC" v-model="registerC.rTandC" name="checkbox-1C" required>
              I have read and accept the terms and conditions and privacy policy.
            </b-form-checkbox>

            <b-form-checkbox id="checkbox-2C" v-model="registerC.newsletter" name="checkbox-2C">
              I do not want to receive the Jungle Newsletter and tips to optimise my company interests.
            </b-form-checkbox>

            <div class="d-grid gap-2 d-md-flex justify-content-md-end">
              <button class="btn btn-warning justify-content-md-end">Submit</button>
            </div>
          </b-form>
        </b-tab>
        <!--/Company form -->
      </b-tabs>

    </b-modal>
  </div>
</template>

<script>
import axios from 'axios'
import Vue from 'vue'

export default {
  data () {
    return {
      name: 'Login',
      logged: false,
      token: '',
      find_match: false,
      is_admin: false,
      is_jobseeker: false,
      is_company: false,
      tabIndex: 0,
      loginForm: {
        username: '',
        password: ''
      },
      registerS: {
        username: '',
        email: '',
        password: '',
        rTandC: false,
        newsletter: false
      },
      registerC: {
        company: '',
        email: '',
        password: '',
        rTandC: false,
        newsletter: false
      }
    }
  },
  methods: {
    checkLogin () {
      const parameters = {
        username: this.loginForm.username,
        password: this.loginForm.password
      }
      console.log('checkLogin')
      const path = Vue.prototype.$API_BASE_URL + 'login'
      axios.post(path, parameters)
        .then((res) => {
          this.logged = true
          this.token = res.data.token
          this.getAccount()
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
          this.loginForm.username = ''
          this.loginForm.password = ''
          alert('Username or Password incorrect')
        })
    },
    onHome () {
      this.$router.replace({ path: '/' })
    },
    onAboutUs () {
      this.$router.replace({ path: '/about_us' })
    },
    onJobPostings () {
      this.$router.replace({ path: '/job_postings' })
    },
    getAccount (type = 'jobseeker') {
      if (type === 'jobseeker') {
        const pathJobseeker = Vue.prototype.$API_BASE_URL + 'jobseeker/' + this.loginForm.username // to change check endpoints backend
        axios.get(pathJobseeker)
          .then((res) => {
            console.log(res)
            this.is_jobseeker = true
            this.is_admin = res.data.account.is_admin !== 0
            this.$router.replace({
              path: '/',
              query: {
                username: this.loginForm.username,
                is_company: false,
                is_jobseeker: true,
                logged: this.logged,
                is_admin: this.is_admin,
                token: this.token
              }
            })
          })
          .catch(() => {
            // eslint-disable-next-line
            this.is_jobseeker = false
            this.getAccount('company')
            // to change: now check for companies
          })
      } else {
        const pathCompany = Vue.prototype.$API_BASE_URL + 'company/' + this.loginForm.username // to change check endpoints backend
        axios.get(pathCompany)
          .then((res) => {
            this.is_jobseeker = false
            this.is_company = true
            this.is_admin = res.data.account.is_admin !== 0
            this.$router.replace({path: '/',
              query: {
                username: this.loginForm.username,
                logged: this.logged,
                is_company: true,
                is_jobseeker: false,
                is_admin: this.is_admin,
                token: this.token
              }
            })
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error)
            // to change: now check for companies
          })
      }
    },
    onSubmit () {
      const pathS = Vue.prototype.$API_BASE_URL + 'jobseeker'
      const pathC = Vue.prototype.$API_BASE_URL + 'company'
      if (this.tabIndex === 0) {
        const values = {
          username: this.registerS.username,
          password: this.registerS.password,
          email: this.registerS.email
        }
        axios.post(pathS, values)
          .then((res) => {
            alert('Correctly registered ' + this.registerS.username + '. You can now sign in!')
          })
          .catch((error) => {
            console.error(error)
            alert(' An error occurred creating the account')
          })
      } else {
        const values = {
          company: this.registerC.company,
          password: this.registerC.password,
          email: this.registerC.email
        }
        axios.post(pathC, values)
          .then((res) => {
            alert('Correctly registered ' + this.registerS.username + '. You can now sign in!')
          })
          .catch((error) => {
            console.error(error)
            alert(' An error occurred creating the account')
          })
      }
      this.onReset()
      this.$bvModal.hide('register-modal')
    },
    initRegisterForm () {
      this.registerS.username = ''
      this.registerS.email = ''
      this.registerS.password = ''
      this.registerS.rTandC = false
      this.registerS.newsletter = false
      this.registerC.company = ''
      this.registerC.email = ''
      this.registerC.password = ''
      this.registerC.rTandC = false
      this.registerC.newsletter = false
    },
    onReset () {
      this.initRegisterForm()
    },

    initLoginForm () {
      this.loginForm.username = ''
      this.loginForm.password = ''
    }
  },
  computed: {
    termsAndCStateS () {
      return this.registerS.rTandC
    },
    termsAndCStateC () {
      return this.registerC.rTandC
    }
  }
}
</script>

<style scoped>

</style>
