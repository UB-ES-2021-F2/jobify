<template>
  <div id="app">
    <!--Navbar -->
    <b-navbar sticky toggleable="lg" type="light" variant="light">
      <b-navbar-brand @click="onHome()">
        <img style="max-width: 150px" :src="require('../assets/logo.svg')">
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item @click="onHome()">Home</b-nav-item>
          <b-nav-item @click="onJobPostings()">Job postings</b-nav-item>
          <b-nav-item active>About Us</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="!logged" class="ml-auto">
          <b-nav-item @click="onLogIn()">Log in</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="logged" class="ml-auto">
          <b-nav-item @click="onUserProfile()">{{ this.username }}</b-nav-item>
          <button class="btn btn-outline-danger" @click="onLogOut()"> Log Out </button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <!--/.Navbar -->
    <div class="container">
      <div class="row">
        <div class="col-12">
          <h2 style="font-family: 'Vollkorn', serif"> {{ message }} </h2>
          <div class="row">
            <!-- Our Project -->
            <div class="col-12">
              <div class="aboutus-title">Our Project</div>
              <div class="row">
                <div class="col-6"></div>
                <div class="col-6"></div>
              </div>
            </div>
            <!-- Our Values -->
            <div class="col-12">
              <div class="aboutus-title">Our Values</div>
              <div class="row">
                <div class="col-4"></div>
                <div class="col-4"></div>
                <div class="col-4"></div>
              </div>
            </div>
            <!-- Who we are?-->
            <div class="col-12">
              <div class="aboutus-title">Who we are?</div>
              <div class="row">
                <div class="col-4">
                  <div class="aboutus-weare-container">
                    <div class="row">
                      <div class="col-4">
                      <div class="aboutus-porfile-picture">
                        <img src="../assets/images/arnau.jpeg">
                      </div>
                    </div>
                      <div class="col-8">
                        <div class="aboutus-text-container">
                          <div class="aboutus-name">
                            Arnau Quindós
                          </div>
                          <div class="aboutus-role">
                            Product Owner
                          </div>
                          <div class="aboutus-description">
                            Lorem ipsum dolor bla bla bla bla.
                          </div>
                        </div>
                    </div>
                    </div>
                  </div>
                </div>
                <div class="col-4">
                  <div class="aboutus-weare-container">
                    <div class="row">
                      <div class="col-4">
                        <div class="aboutus-porfile-picture">
                          <img src="../assets/images/carles.jpeg">
                        </div>
                      </div>
                      <div class="col-8">
                        <div class="aboutus-text-container">
                          <div class="aboutus-name">
                            Carles Pérez Onielfa
                          </div>
                          <div class="aboutus-role">
                            Devops
                          </div>
                          <div class="aboutus-description">
                            Always eager to learn and able to do so swiftly.
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-4">
                  <div class="aboutus-weare-container">
                    <div class="row">
                      <div class="col-4">
                        <div class="aboutus-porfile-picture">
                          <img src="../assets/images/arnau.jpeg">
                        </div>
                      </div>
                      <div class="col-8">
                        <div class="aboutus-text-container">
                          <div class="aboutus-name">
                            Arnau Quindós
                          </div>
                          <div class="aboutus-role">
                            Product Owner
                          </div>
                          <div class="aboutus-description">
                            Lorem ipsum dolor bla bla bla bla.
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-4">
                  <div class="aboutus-weare-container">
                    <div class="row">
                      <div class="col-4">
                        <div class="aboutus-porfile-picture">
                          <img src="../assets/images/arnau.jpeg">
                        </div>
                      </div>
                      <div class="col-8">
                        <div class="aboutus-text-container">
                          <div class="aboutus-name">
                            Arnau Quindós
                          </div>
                          <div class="aboutus-role">
                            Product Owner
                          </div>
                          <div class="aboutus-description">
                            Lorem ipsum dolor bla bla bla bla.
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-4">
                  <div class="aboutus-weare-container">
                    <div class="row">
                      <div class="col-4">
                        <div class="aboutus-porfile-picture">
                          <img src="../assets/images/arnau.jpeg">
                        </div>
                      </div>
                      <div class="col-8">
                        <div class="aboutus-text-container">
                          <div class="aboutus-name">
                            Arnau Quindós
                          </div>
                          <div class="aboutus-role">
                            Product Owner
                          </div>
                          <div class="aboutus-description">
                            Lorem ipsum dolor bla bla bla bla.
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-4">
                  <div class="aboutus-weare-container">
                    <div class="row">
                      <div class="col-4">
                        <div class="aboutus-porfile-picture">
                          <img src="../assets/images/arnau.jpeg">
                        </div>
                      </div>
                      <div class="col-8">
                        <div class="aboutus-text-container">
                          <div class="aboutus-name">
                            Arnau Quindós
                          </div>
                          <div class="aboutus-role">
                            Product Owner
                          </div>
                          <div class="aboutus-description">
                            Lorem ipsum dolor bla bla bla bla.
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-4">
                  <div class="aboutus-weare-container">
                    <div class="row">
                      <div class="col-4">
                        <div class="aboutus-porfile-picture">
                          <img src="../assets/images/arnau.jpeg">
                        </div>
                      </div>
                      <div class="col-8">
                        <div class="aboutus-text-container">
                          <div class="aboutus-name">
                            Arnau Quindós
                          </div>
                          <div class="aboutus-role">
                            Product Owner
                          </div>
                          <div class="aboutus-description">
                            Lorem ipsum dolor bla bla bla bla.
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- -->
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>

export default {
  data () {
    return {
      name: 'Name Surname',
      message: 'About Us',
      logged: false,
      username: '',
      is_admin: false,
      is_jobseeker: true,
      is_company: false,
      token: ''
    }
  },
  methods: {
    onHome () {
      this.$router.replace({path: '/',
        query: {
          username: this.username,
          logged: this.logged,
          is_company: this.is_company,
          is_jobseeker: this.is_jobseeker,
          is_admin: this.is_admin,
          token: this.token
        }
      })
    },
    onUserProfile () {
      if (this.is_jobseeker & this.logged) {
        this.$router.replace({ path: '/job_seeker/' + this.username,
          query: {
            username: this.username,
            logged: this.logged,
            is_company: this.is_company,
            is_jobseeker: this.is_jobseeker,
            is_admin: this.is_admin,
            token: this.token
          }
        })
      }
    },
    onLogIn () {
      this.$router.replace({ path: '/login' })
    },
    onLogOut () {
      this.$router.replace({ path: '/about_us' })
      this.logged = false
      this.username = ''
      this.token = ''
      this.is_jobseeker = true
      this.is_company = false
      this.is_admin = false
    },
    onJobPostings () {
      this.$router.replace({path: '/job_postings',
        query: {
          username: this.username,
          logged: this.logged,
          is_company: this.is_company,
          is_jobseeker: this.is_jobseeker,
          is_admin: this.is_admin,
          token: this.token
        }
      })
    }
  },
  created () {
    this.logged = this.$route.query.logged === 'true'
    this.username = this.$route.query.username ? this.$route.query.username : ''
    this.is_jobseeker = this.$route.query.is_jobseeker === 'true'
    this.is_company = this.$route.query.is_company === 'true'
    this.token = this.$route.query.token ? this.$route.query.token : ''
    this.is_admin = this.$route.query.is_admin === 'true'
  }
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
