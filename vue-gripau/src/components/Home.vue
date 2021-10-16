<template>
  <div id="app">
    <!--Navbar -->
    <b-navbar sticky="true" toggleable="lg" type="light" variant="light">
      <b-navbar-brand href="#">
        <img style="max-width: 150px" :src="require('../assets/logo.svg')">
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item active href="#">Home</b-nav-item>
          <b-nav-item href="#">Job postings</b-nav-item>
          <b-nav-item href="#" @click="onAboutUs()">About Us</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="!logged" class="ml-auto">
          <b-nav-item href="#" @click="onLogIn()">Log in</b-nav-item>
          <b-nav-item href="#">Sign up</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="logged" class="ml-auto">
          <b-nav-item href="#" @click="onUserProfile()">{{ this.name }}</b-nav-item>
          <button class="btn btn-outline-danger" @click="onLogOut()"> Log Out </button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <!--/.Navbar -->

    <h1 style="font-family: 'Vollkorn"> {{ message }} </h1>

    <b-modal ref="editShowModal"
             id="event-modal"
             title="Become a member"
             hide-footer
    >
      <b-form style="font-family:'Work Sans'" @submit="onSubmit" @reset="onReset">
        <label style="color: #5a6268">All fields are needed.</label>

        <b-form-group id="input-group-0" label="First name:" label-for="input-0">
          <b-form-input v-model="register.fName" placeholder="" type="text" required></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-1" label="Last name:" label-for="input-1">
          <b-form-input v-model="register.lName" placeholder="" type="text" required></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-2" label="Email:" label-for="input-2">
          <b-form-input v-model="register.email" placeholder="" type="email" required></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-3" label="Password:" label-for="input-3">
          <b-form-input v-model="register.password" placeholder="" type="password" required></b-form-input>
          <b-form-text id="password-help-block">
            Your password should be 8-20 characters long.
          </b-form-text>
        </b-form-group>

        <b-form-checkbox id="checkbox-1" :state="termsAndCState" v-model="register.rTandC" name="checkbox-1" required>
          I have read and accept the terms and conditions and privacy policy.
        </b-form-checkbox>

        <b-form-checkbox id="checkbox-2" v-model="register.newsletter" name="checkbox-2">
          I do not want to receive the Jungle Newsletter and tips to optimise my job search.
        </b-form-checkbox>

        <div class="d-grid gap-2 d-md-flex justify-content-md-end">
          <button class="btn btn-warning justify-content-md-end">Submit</button>
        </div>

      </b-form>
    </b-modal>
  </div>
</template>

<script>

export default {
  data () {
    return {
      name: 'Name Surname',
      message: 'Homepage',
      logged: false,
      register: {
        fName: '',
        lName: '',
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
      alert('Form submitted!')
    },
    initForm () {
      this.register.fName = ''
      this.register.lName = ''
      this.register.email = ''
      this.register.password = ''
    },
    onReset (evt) {
      evt.preventDefault()
      this.initForm()
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    },
    onLogIn () {
      this.logged = true
    },
    onLogOut () {
      this.logged = false
    },
    onAboutUs () {
      this.$router.replace({ path: '/about_us' })
    },
    getName () {
      // TODO: GET to API
    }
  },
  computed: {
    termsAndCState () {
      return this.register.rTandC
    }
  }
}

</script>

<style>
.navbar.navbar-light{
  font-family: "Work Sans SemiBold";
  font-size: 18px;
  padding: 20px;
  margin-bottom: 20px;
}
</style>
