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
          <b-nav-item @click="onHome()">Home</b-nav-item>
          <b-nav-item @click="onJobPostings()">Job postings</b-nav-item>
          <b-nav-item @click="onCompanies()">Companies</b-nav-item>
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
             hide-backdrop
    >
      <b-tabs v-model="tabIndex" content-class="mt-3" fill>
        <!--Job Seeker form -->
        <b-tab title="Job Seeker" active>
          <validation-observer ref="observer" v-slot="{ handleSubmit }">
            <b-form style="font-family:'Work Sans'" @submit.prevent="handleSubmit(onSubmit)">

              <validation-provider name="FirstName"  :rules="{ alpha_spaces, required: true, max: 30}" v-slot="validationContext">
                <b-form-group id="input-group-1" label="First Name" label-for="input-1">
                  <b-form-input v-model="registerS.fName" placeholder="" type="text" :state="getValidationState(validationContext)"
                                aria-describedby="input-1-live-feedback"></b-form-input>
                  <b-form-invalid-feedback id="input-1-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>

              <validation-provider name="LastName"  :rules="{ alpha_spaces, required: true, max: 30}" v-slot="validationContext">
                <b-form-group id="input-group-2" label="Last Name" label-for="input-2">
                  <b-form-input v-model="registerS.lName" placeholder="" type="text" :state="getValidationState(validationContext)"
                                aria-describedby="input-2-live-feedback"></b-form-input>
                  <b-form-invalid-feedback id="input-2-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>

              <validation-provider name="Username"  :rules="{ alpha_num, required: true, min:4, max: 30}" v-slot="validationContext">
                <b-form-group id="input-group-3" label="Username" label-for="input-3">
                  <b-form-input v-model="registerS.username" placeholder="" type="text" :state="getValidationState(validationContext)"
                                aria-describedby="input-3-live-feedback"></b-form-input>
                  <b-form-invalid-feedback id="input-3-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>

              <validation-provider name="Email"  :rules="{ email, required: true, max: 128}" v-slot="validationContext">
                <b-form-group id="input-group-4" label="Email" label-for="input-4">
                  <b-form-input v-model="registerS.email" placeholder="" type="email" :state="getValidationState(validationContext)"
                                aria-describedby="input-4-live-feedback"></b-form-input>
                  <b-form-invalid-feedback id="input-4-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>

              <validation-provider name="password"  :rules="{required: true, regex: /^(?=.*[A-Z])(?=.*[0-9])(?=.*[a-z]).{8,20}$/ }" v-slot="validationContext" vid="password">
                <b-form-group id="input-group-5" label="Password" label-for="input-5">
                  <b-form-input v-model="registerS.password" placeholder="" type="password" :state="getValidationState(validationContext)"
                                aria-describedby="input-5-live-feedback"></b-form-input>
                  <b-form-text id="password-help-block">
                    Your password must be 8-20 characters long and contain numbers and both uppercase and lowercase letters
                  </b-form-text>
                  <b-form-invalid-feedback id="input-5-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>

              <validation-provider name="confirmation"  rules="required|confirmed:password" v-slot="validationContext">
                <b-form-group id="input-group-6" label="Confirm password" label-for="input-6">
                  <b-form-input v-model="registerS.confirmation" placeholder="" type="password" :state="getValidationState(validationContext)"
                                aria-describedby="input-6-live-feedback"></b-form-input>
                  <b-form-invalid-feedback id="input-6-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>

              <!--
              <b-form-checkbox id="checkbox-1" :state="this.registerS.rTandC" v-model="registerS.rTandC" name="checkbox-1">
                I have read and accept the terms and conditions and privacy policy.
              </b-form-checkbox>-->

              <b-form-checkbox id="checkbox-2" v-model="registerS.newsletter" name="checkbox-2">
                I do not want to receive the Jungle Newsletter and tips to optimise my job search.
              </b-form-checkbox>

              <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                <button class="btn btn-warning justify-content-md-end">Join Jobify!</button>
              </div>
            </b-form>
          </validation-observer>
        </b-tab>
        <!--/Job Seeker form -->
        <!--Company form -->
        <b-tab title="Company (coming soon)">
          <validation-observer ref="observerCompany" v-slot="{ handleSubmit }">
            <b-form style="font-family:'Work Sans'" @submit.prevent="handleSubmit(onSubmit)" >

              <validation-provider name="Company name"  :rules="{alpha_spaces, required: true, max: 30}" v-slot="validationContext">
                <b-form-group id="input-group-1C" label="Company name" label-for="input-1C">
                  <b-form-input v-model="registerC.company" placeholder="" type="text" :state="getValidationState(validationContext)"
                                aria-describedby="input-1c-live-feedback"></b-form-input>
                  <b-form-invalid-feedback id="input-1c-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>

              <validation-provider name="Company email"  :rules="{email, required: true, max: 128}" v-slot="validationContext">
                <b-form-group id="input-group-2C" label="Email" label-for="input-2C">
                  <b-form-input v-model="registerC.email" placeholder="" type="email" :state="getValidationState(validationContext)"
                                aria-describedby="input-2c-live-feedback">></b-form-input>
                  <b-form-invalid-feedback id="input-2c-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>

              <validation-provider name="Company password"  :rules="{required: true, regex: /^(?=.*[A-Z])(?=.*[0-9])(?=.*[a-z]).{8,20}$/ }" v-slot="validationContext" vid="passwordc">
                <b-form-group id="input-group-3C" label="Password" label-for="input-3C">
                  <b-form-input v-model="registerC.password" placeholder="" type="password" :state="getValidationState(validationContext)"
                                aria-describedby="input-3C-live-feedback"></b-form-input>
                  <b-form-text id="password-help-block">
                    Your password must be 8-20 characters long and contain numbers and both uppercase and lowercase letters
                  </b-form-text>
                  <b-form-invalid-feedback id="input-3C-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>

              <validation-provider name="confirmation"  rules="required|confirmed:passwordc" v-slot="validationContext">
                <b-form-group id="input-group-4C" label="Confirm password" label-for="input-4C">
                  <b-form-input v-model="registerC.confirmation" placeholder="" type="password" :state="getValidationState(validationContext)"
                                aria-describedby="input-4C-live-feedback"></b-form-input>
                  <b-form-invalid-feedback id="input-4C-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>
              <!--
              <b-form-checkbox id="checkbox-1C" :state="this.registerC.rTandC" v-model="registerC.rTandC" name="checkbox-1C" required>
                I have read and accept the terms and conditions and privacy policy.
              </b-form-checkbox>-->

              <b-form-checkbox id="checkbox-2C" v-model="registerC.newsletter" name="checkbox-2C">
                I do not want to receive the Jungle Newsletter and tips to optimise my company interests.
              </b-form-checkbox>

              <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                <button class="btn btn-warning justify-content-md-end">Join Jobify!</button>
              </div>
            </b-form>
          </validation-observer>
        </b-tab>
        <!--/Company form -->
      </b-tabs>

    </b-modal>
  </div>
</template>

<script>
import axios from 'axios'
import Vue from 'vue'
import {mapState} from 'vuex'

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
        fName: '',
        lName: '',
        username: '',
        email: '',
        password: '',
        confirmation: '',
        rTandC: false,
        newsletter: false
      },
      registerC: {
        company: '',
        email: '',
        password: '',
        confirmation: '',
        rTandC: false,
        newsletter: false
      }
    }
  },
  methods: {
    checkLogin () {
      const parameters = {
        username: this.loginForm.username.toLowerCase(),
        password: this.loginForm.password
      }
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
    getValidationState ({ dirty, validated, valid = null }) {
      return dirty || validated ? valid : null
    },
    onHome () {
      this.$router.replace({ path: '/' })
    },
    onAboutUs () {
      this.$router.replace({ path: '/about_us' })
    },
    onCompanies () {
      this.$router.replace({ path: '/companies' })
    },
    onJobPostings () {
      this.$router.replace({ path: '/job_postings' })
    },
    getAccount (type = 'jobseeker') {
      if (type === 'jobseeker') {
        const pathJobseeker = Vue.prototype.$API_BASE_URL + 'jobseeker/' + this.loginForm.username.toLowerCase() // to change check endpoints backend
        axios.get(pathJobseeker)
          .then((res) => {
            const storeData = {token: this.token, username: this.loginForm.username, isAdmin: res.data.account.is_admin !== 0, isJobSeeker: true, isCompany: false}
            this.$store.commit('login', storeData)
            this.$router.replace({path: '/'})
          })
          .catch(() => {
            // eslint-disable-next-line
            this.is_jobseeker = false
            this.getAccount('company')
            // to change: now check for companies
          })
      } else {
        const pathCompany = Vue.prototype.$API_BASE_URL + 'company/' + this.loginForm.username.toLowerCase() // to change check endpoints backend
        axios.get(pathCompany)
          .then((res) => {
            const storeData = {token: this.token, username: this.loginForm.username, isAdmin: res.data.account.is_admin !== 0, isJobSeeker: false, isCompany: true}
            this.$store.commit('login', storeData)
            this.$router.replace({path: '/'})
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
          username: this.registerS.username.toLowerCase(),
          password: this.registerS.password,
          name: this.registerS.fName,
          surname: this.registerS.lName,
          email: this.registerS.email
        }
        axios.post(pathS, values)
          .then((res) => {
            console.log('Correctly registered ' + this.registerS.username + '. You can now sign in!')
          })
          .catch((error) => {
            alert(error.response.data.message)
          })
      } else {
        const values = {
          company: this.registerC.company,
          password: this.registerC.password,
          email: this.registerC.email
        }
        axios.post(pathC, values)
          .then((res) => {
            console.log('Correctly registered ' + this.registerS.username + '. You can now sign in!')
          })
          .catch((error) => {
            alert(error.response.data.message)
          })
      }
      this.onReset()
      this.$bvModal.hide('register-modal')
    },
    initRegisterForm () {
      this.registerS.username = ''
      this.registerS.lName = ''
      this.registerS.fName = ''
      this.registerS.email = ''
      this.registerS.password = ''
      this.registerS.confirmation = ''
      this.registerS.rTandC = false
      this.registerS.newsletter = false
      this.registerC.company = ''
      this.registerC.email = ''
      this.registerC.password = ''
      this.registerC.confirmation = ''
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
