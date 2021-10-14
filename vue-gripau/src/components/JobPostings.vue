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
          <li class="nav-item active">
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
    <b-container fluid>
      <b-row align-h="center" v-for="(job_offer) in job_offers" :key="job_offer.id">
        <b-card
          :title="job_offer.title"
          tag="article"
          class="mb-2"
          style="width: inherit"
        >
          <b-card-text>
            Some quick example text to build on the card title and make up the bulk of the card's content.
          </b-card-text>

          <b-button href="#" variant="primary">See more</b-button>
        </b-card>
      </b-row>
    </b-container>
  </div>
</template>

<script>

export default {
  data () {
    return {
      message: 'Job Postings',
      logged: false,
      job_offers: [{'id': 0, 'title': 'Waiter'}, {'id': 1, 'title': 'Journalist'}, {'id': 2, 'title': 'Data Scientist'}]
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
    onAboutUs () {
      this.$router.replace({path: '/about_us'})
    }
  }
}
</script>

<style scoped>

</style>
