<template>
  <div id="app">
    <!--Navbar -->
    <b-navbar sticky="true" toggleable="lg" type="light" variant="light">
      <b-navbar-brand href="#" @click="onHome()">
        <img style="max-width: 150px" :src="require('../assets/logo.svg')">
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="#" @click="onHome()">Home</b-nav-item>
          <b-nav-item href="#">Job postings</b-nav-item>
          <b-nav-item active href="#">About Us</b-nav-item>
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
  </div>
</template>

<script>

export default {
  data () {
    return {
      name: 'Name Surname',
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
    },
    getName () {
      // TODO: GET to API
    }
  }
}
</script>

<style scoped>
.navbar.navbar-light.navbar-light{
  font-family: "Work Sans SemiBold";
  font-size: 18px;
  padding: 20px;
  margin-bottom: 20px;
}
</style>
