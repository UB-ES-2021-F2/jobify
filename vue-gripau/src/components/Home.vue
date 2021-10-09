<template>
  <div id="app">
    <h1> {{ message }} </h1>
    <button class="btn btn-primary btn-lg" @click="onUserProfile()"> User Profile </button>
    <button class="btn btn-lg" v-b-modal.event-modal1>Register</button>
    <b-modal ref="editShowModal"
             id="event-modal1"
             title="Become a member"
             hide-footer>
      <b-form @reset="onReset">
        <label style="color: #5a6268">All fields are needed.</label>
          <b-form-group id="input-group-0" label="First name:" label-for="input-0">
            <b-form-input v-model="register.fName" placeholder="" input type="text"></b-form-input>
          </b-form-group>
          <b-form-group id="input-group-1" label="Last name:" label-for="input-1">
            <b-form-input v-model="register.lName" placeholder="" input type="text"></b-form-input>
          </b-form-group>
          <b-form-group @submit.stop.prevent id="input-group-2" label="Email:" label-for="input-2">
            <b-form-input v-model="register.email" placeholder="" :state="validationEmail" input type="email"></b-form-input>
            <b-form-invalid-feedback :state="validationPwd">
              Your email must be 5-12 characters long.
            </b-form-invalid-feedback>
            <b-form-valid-feedback :state="validationPwd">
              Looks Good.
            </b-form-valid-feedback>
          </b-form-group>
          <b-form-group id="input-group-3" label="Password:" label-for="input-3">
            <b-form-input v-model="register.password" placeholder="" input type="password"></b-form-input>
            <b-form-text id="password-help-block">
              Your password must be 8-20 characters long, contain letters and numbers, and must not
              contain spaces, special characters, or emoji.
            </b-form-text>
          </b-form-group>
        <form class="was-validated">
          <div class="custom-control custom-checkbox mb-3">
            <input type="checkbox" class="custom-control-input" id="customControlValidation1" required>
            <label class="custom-control-label" for="customControlValidation1">I have read and accept the terms and conditions and privacy policy.</label>
          </div>
        </form>
        <div class="form-check">
          <input class="custom-control-input" type="checkbox" value="" id="invalidCheck" required>
          <label class="custom-control-label" for="invalidCheck">
            I do not want to receive the Jungle Newsletter and tips to optimise my job search.
          </label>
        </div>
        <div class="d-grid gap-2 d-md-flex justify-content-md-end">
          <button class="btn btn-warning justify-content-md-end" @click="onSubmitUpdate">Submit</button>
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
        password: ''
      }
    }
  },
  methods: {
    onUserProfile () {
      this.$router.replace({ path: '/user' })
    },
    onSubmitUpdate (evt) {
      evt.preventDefault()
      this.$refs.editShowModal.hide()
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
    onResetUpdate (evt) {
      evt.preventDefault()
      this.initForm()
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  },
  computed: {
    validationEmail () {
      return this.register.email.length > 4 && this.register.email.length < 13
    }
  }
}

</script>
