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

    <h1 style="font-family: 'Vollkorn"> {{ message }} </h1>

    <b-modal ref="editShowModal"
             id="event-modal"
             title="Become a member"
             hide-footer
    >
      <b-tabs v-model="tabIndex" content-class="mt-3" fill>
        <!--Job Seeker form -->
        <b-tab title="Job Seeker" active>
          <b-form style="font-family:'Work Sans'" @submit="onSubmit">
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
        <b-tab title="Company">
          <b-form style="font-family:'Work Sans'" @submit="onSubmit" >
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
export default {
  data () {
    return {
      message: 'Home',
      tabIndex: 0,
      logged: false,
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
    onUserProfile () {
      this.$router.replace({ path: '/user' })
    },
    onSubmit () {
      const pathS = 'http://127.0.0.1:5000/jobseeker'
      const pathC = 'http://127.0.0.1:5000/company'
      if (this.tabIndex === 0) {
        const values = {
          username: this.registerS.username,
          password: this.registerS.password,
          email: this.registerS.email
        }
        axios.post(pathS, values)
          .then((res) => {
            alert('Form submitted! ' + this.registerS.username)
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
            alert('Form submitted! ' + this.registerC.company)
          })
          .catch((error) => {
            console.error(error)
            alert(' An error occurred creating the account')
          })
      }
      this.onReset()
      this.$bvModal.hide('event-modal')
    },
    initForm () {
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
      this.initForm()
    },
    onLogIn () {
      this.logged = true
    },
    onLogOut () {
      this.logged = false
    },
    onAboutUs () {
      this.$router.replace({ path: '/about_us' })
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
