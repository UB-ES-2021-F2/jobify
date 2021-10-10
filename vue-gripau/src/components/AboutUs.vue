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
            <a class="nav-link" href="#" @click="onHome()">Home
              <span class="sr-only">(current)</span>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Job postings</a>
          </li>
          <li class="nav-item active">
            <a class="nav-link" href="#">About us</a>
          </li>
        </ul>
        <ul v-if="!logged" class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link" href="#" @click="onLogIn()">Log in</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Sign up</a>
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
      message: 'About Us',
      logged: false
    }
  },
  methods: {
    onHome () {
      this.$router.replace({path: '/'})
    },
    onUserProfile () {
      this.$router.replace({ path: '/user' })
    },
    onLogIn () {
      this.logged = true
    },
    onLogOut () {
      this.logged = false
    }
  }
}
</script>

<style scoped>

</style>
