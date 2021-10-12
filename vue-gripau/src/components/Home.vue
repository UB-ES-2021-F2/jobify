<template>
  <div id="app">
    <h1> {{ message }} </h1>
    <button class="btn btn-primary btn-lg" @click="onUserProfile()"> User Profile </button>
    <button class="btn btn-lg" v-b-modal.event-modal>Register</button>
    <b-modal ref="editShowModal"
             id="event-modal"
             title="Become a member"
             hide-footer>
      <b-form @submit="onSubmit" @reset="onReset">
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
    }
  },
  computed: {
    termsAndCState () {
      return this.register.rTandC
    }
  }
}

</script>
