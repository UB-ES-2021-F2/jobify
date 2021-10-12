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
      message: 'Home',
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
    }
  },
  computed: {
    termsAndCState () {
      return this.register.rTandC
    }
  }
}

</script>
