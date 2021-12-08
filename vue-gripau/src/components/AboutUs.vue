<template>
  <div id="app">
    <!--Navbar -->
    <b-navbar sticky toggleable="lg" type="light" variant="light">
      <b-navbar-brand id="logoNavbar" href="#" @click="onHome()">
        <img style="max-width: 150px" :src="require('../assets/logo.svg')">
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item id="homeNavbarButton" @click="onHome()">Home</b-nav-item>
          <b-nav-item id="jobPostingsNavbarButton" @click="onJobPostings()">Job postings</b-nav-item>
          <b-nav-item id="companiesNavbarButton" @click="onCompanies()">Companies</b-nav-item>
          <b-nav-item id="aboutUsNavbarButton" active>About Us</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="!logged" class="ml-auto">
          <b-nav-item id="logInNavbarButton" @click="onLogIn()">Log in</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="logged" class="ml-auto">
          <b-nav-item id="profileNavbarButton" @click="onProfile()">{{ this.username }}</b-nav-item>
          <button id="logOutNavbarButton" class="btn btn-outline-danger" @click="onLogOut()"> Log Out </button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <!--/.Navbar -->
    <div class="container">
      <div class="row">
        <div class="col-12">
          <div id="aboutUsTitle" class="aboutus-title"> {{ message }} </div>
          <div class="row" style="height: fit-content">
            <!-- Our Project -->
            <div class="ourproject-container">
              <div class="col-12">
                <div class="row">
                  <div class="col-sm-12 col-md-6">
                    <div class="content-table">
                      <div class="content-table-cell">
                        <div class="aboutus-subtitle">Our Project</div>
                        <div class="aboutus-our-project">
                          <p>Jobify is a communication platform whose ambition is to inspire each person during the development of their professional career.</p>
                          <p>To do this, we have a easy-to-use interface and a great team trying to offer all kind of professionals their dream jobs.</p>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-sm-12 col-md-6">
                    <div class="content-table">
                      <div class="content-table-cell">
                        <div class="image-container text-center">
                          <img src="../assets/images/working_stock_image.png">
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- Our Values -->
            <div class="ourvalues-container">
              <div class="col-12">
                <div class="aboutus-subtitle">Our Values</div>
                <div class="row">
                  <div class="col-sm-12 col-md-4">
                    <div class="icon-container">
                      <div class="ourvalues-icon">
                        <div class="content-table">
                          <div class="content-table-cell">
                            <svg class="svg-inline--fa fa-hands-helping fa-w-20" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="hands-helping" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512" data-fa-i2svg=""><path fill="currentColor" d="M488 192H336v56c0 39.7-32.3 72-72 72s-72-32.3-72-72V126.4l-64.9 39C107.8 176.9 96 197.8 96 220.2v47.3l-80 46.2C.7 322.5-4.6 342.1 4.3 357.4l80 138.6c8.8 15.3 28.4 20.5 43.7 11.7L231.4 448H368c35.3 0 64-28.7 64-64h16c17.7 0 32-14.3 32-32v-64h8c13.3 0 24-10.7 24-24v-48c0-13.3-10.7-24-24-24zm147.7-37.4L555.7 16C546.9.7 527.3-4.5 512 4.3L408.6 64H306.4c-12 0-23.7 3.4-33.9 9.7L239 94.6c-9.4 5.8-15 16.1-15 27.1V248c0 22.1 17.9 40 40 40s40-17.9 40-40v-88h184c30.9 0 56 25.1 56 56v28.5l80-46.2c15.3-8.9 20.5-28.4 11.7-43.7z"></path></svg>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="ourvalues-text">
                      <div class="ourvalues-title">Committed</div>
                      <div class="ourvalues-description">As a company, we assure for our job seekers reliable labor conditions.</div>
                    </div>
                  </div>
                  <div class="col-sm-12 col-md-4">
                    <div class="icon-container">
                      <div class="ourvalues-icon">
                        <div class="content-table">
                          <div class="content-table-cell">
                            <svg class="svg-inline--fa fa-gem fa-w-18" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="gem" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" data-fa-i2svg=""><path fill="currentColor" d="M485.5 0L576 160H474.9L405.7 0h79.8zm-128 0l69.2 160H149.3L218.5 0h139zm-267 0h79.8l-69.2 160H0L90.5 0zM0 192h100.7l123 251.7c1.5 3.1-2.7 5.9-5 3.3L0 192zm148.2 0h279.6l-137 318.2c-1 2.4-4.5 2.4-5.5 0L148.2 192zm204.1 251.7l123-251.7H576L357.3 446.9c-2.3 2.7-6.5-.1-5-3.2z"></path></svg>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="ourvalues-text">
                      <div class="ourvalues-title">Precise</div>
                      <div class="ourvalues-description">Using Jobify will grant you the most accurate results for your job applies.</div>
                    </div>
                  </div>
                  <div class="col-sm-12 col-md-4">
                    <div class="icon-container">
                      <div class="ourvalues-icon">
                        <div class="content-table">
                          <div class="content-table-cell">
                            <svg class="svg-inline--fa fa-brain fa-w-18" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="brain" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" data-fa-i2svg=""><path fill="currentColor" d="M208 0c-29.9 0-54.7 20.5-61.8 48.2-.8 0-1.4-.2-2.2-.2-35.3 0-64 28.7-64 64 0 4.8.6 9.5 1.7 14C52.5 138 32 166.6 32 200c0 12.6 3.2 24.3 8.3 34.9C16.3 248.7 0 274.3 0 304c0 33.3 20.4 61.9 49.4 73.9-.9 4.6-1.4 9.3-1.4 14.1 0 39.8 32.2 72 72 72 4.1 0 8.1-.5 12-1.2 9.6 28.5 36.2 49.2 68 49.2 39.8 0 72-32.2 72-72V64c0-35.3-28.7-64-64-64zm368 304c0-29.7-16.3-55.3-40.3-69.1 5.2-10.6 8.3-22.3 8.3-34.9 0-33.4-20.5-62-49.7-74 1-4.5 1.7-9.2 1.7-14 0-35.3-28.7-64-64-64-.8 0-1.5.2-2.2.2C422.7 20.5 397.9 0 368 0c-35.3 0-64 28.6-64 64v376c0 39.8 32.2 72 72 72 31.8 0 58.4-20.7 68-49.2 3.9.7 7.9 1.2 12 1.2 39.8 0 72-32.2 72-72 0-4.8-.5-9.5-1.4-14.1 29-12 49.4-40.6 49.4-73.9z"></path></svg>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="ourvalues-text">
                      <div class="ourvalues-title">Accessible</div>
                      <div class="ourvalues-description">Our nice and clean interface makes it easier to find the job of your life.</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- Who are we -->
            <div class="weare-container">
              <div class="col-12">
                <div class="aboutus-subtitle">Who we are</div>
                <div class="row">
                  <div class="col-sm-12 col-md-6 col-xl-4">
                    <div class="aboutus-weare-container">
                      <div class="row">
                        <div class="col-4">
                        <div class="aboutus-porfile-picture">
                          <img :src="require('../assets/images/arnau.jpeg')">
                        </div>
                      </div>
                        <div class="col-8">
                          <div class="aboutus-text-container">
                            <div class="aboutus-name">
                              Arnau Quindós Sanchez
                            </div>
                            <div class="aboutus-role">
                              Product Owner
                            </div>
                            <div class="aboutus-description">
                              Expecting great results from our team.
                            </div>
                          </div>
                      </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-sm-12 col-md-6 col-xl-4">
                    <div class="aboutus-weare-container">
                      <div class="row">
                        <div class="col-4">
                          <div class="aboutus-porfile-picture">
                            <img :src="require('../assets/images/carles.jpeg')">
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
                  <div class="col-sm-12 col-md-6 col-xl-4">
                    <div class="aboutus-weare-container">
                      <div class="row">
                        <div class="col-4">
                          <div class="aboutus-porfile-picture">
                            <img :src="require('../assets/images/david.jpeg')">
                          </div>
                        </div>
                        <div class="col-8">
                          <div class="aboutus-text-container">
                            <div class="aboutus-name">
                              David Rial Figols
                            </div>
                            <div class="aboutus-role">
                              Quality Assurance
                            </div>
                            <div class="aboutus-description">
                              Willing maximum quality for our costumers.
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-sm-12 col-md-6 col-xl-4">
                    <div class="aboutus-weare-container">
                      <div class="row">
                        <div class="col-4">
                          <div class="aboutus-porfile-picture">
                            <img :src="require('../assets/images/eduard.jpeg')">
                          </div>
                        </div>
                        <div class="col-8">
                          <div class="aboutus-text-container">
                            <div class="aboutus-name">
                              Eduard Graners Castellet
                            </div>
                            <div class="aboutus-role">
                              Front-End Developer
                            </div>
                            <div class="aboutus-description">
                              Aesthetics are always important in software.
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-sm-12 col-md-6 col-xl-4">
                    <div class="aboutus-weare-container">
                      <div class="row">
                        <div class="col-4">
                          <div class="aboutus-porfile-picture">
                            <img :src="require('../assets/images/sergi_ger.jpeg')">
                          </div>
                        </div>
                        <div class="col-8">
                          <div class="aboutus-text-container">
                            <div class="aboutus-name">
                              Sergi Ger Roca
                            </div>
                            <div class="aboutus-role">
                              Front-End Developer
                            </div>
                            <div class="aboutus-description">
                              Delivering cool software is always pleasant.
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-sm-12 col-md-6 col-xl-4">
                    <div class="aboutus-weare-container">
                      <div class="row">
                        <div class="col-4">
                          <div class="aboutus-porfile-picture">
                            <img :src="require('../assets/images/sergi_bech.jpeg')">
                          </div>
                        </div>
                        <div class="col-8">
                          <div class="aboutus-text-container">
                            <div class="aboutus-name">
                              Sergi Bech Sala
                            </div>
                            <div class="aboutus-role">
                              Back-End Developer
                            </div>
                            <div class="aboutus-description">
                              Constantly improving our product.
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-sm-12 col-md-6 col-xl-4">
                    <div class="aboutus-weare-container">
                      <div class="row">
                        <div class="col-4">
                          <div class="aboutus-porfile-picture">
                            <img :src="require('../assets/images/alex.jpeg')">
                          </div>
                        </div>
                        <div class="col-8">
                          <div class="aboutus-text-container">
                            <div class="aboutus-name">
                              Alejandro Lendínez Padilla
                            </div>
                            <div class="aboutus-role">
                              Back-End Developer
                            </div>
                            <div class="aboutus-description">
                              Making everything work is challenging.
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- /.Who we are -->
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import {mapState} from 'vuex'

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
      this.$router.push('/')
    },
    onProfile () {
      if (this.is_jobseeker && this.logged) {
        this.$router.push('/job_seeker/' + this.username)
      } else if (this.is_company && this.logged) {
        this.$router.push('/company/' + this.username)
      }
    },
    onLogIn () {
      this.$router.push('/login')
    },
    onCompanies () {
      this.$router.push('/companies')
    },
    onLogOut () {
      this.$store.commit('logout')
      this.$router.push('/')
    },
    onJobPostings () {
      this.$router.push('/job_postings')
    },
    computed: mapState({
      token: state => state.token,
      logged: state => state.logged,
      username: state => state.username,
      isJobSeeker: state => state.isJobSeeker,
      isCompany: state => state.isCompany,
      isAdmin: state => state.isAdmin
    })
  },
  created () {
    this.logged = this.$store.state.logged
    this.username = this.$store.state.username
    this.is_jobseeker = this.$store.state.isJobSeeker
    this.is_company = this.$store.state.isCompany
    this.token = this.$store.state.token
    this.is_admin = this.$store.state.isAdmin
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
