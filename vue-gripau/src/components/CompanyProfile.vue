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
          <b-nav-item @click="onCompanies()">Companies</b-nav-item>
          <b-nav-item @click="onAboutUs()">About Us</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="!logged" class="ml-auto">
          <b-nav-item @click="onLogIn()">Log in</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="logged" class="ml-auto">
          <b-nav-item active >{{ this.username }}</b-nav-item>
          <button class="btn btn-outline-danger" @click="onLogOut()"> Log Out </button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <!--/.Navbar -->

    <b-container fluid>
      <b-row align-v="stretch">
        <!-- Local Navbar -->
        <b-col style="background-color: #00000007" cols="">
          <b-nav sticky toggleable="lg" type="light" variant="light" vertical>
            <b-navbar-brand style="text-align: center;width: 100%;" >
              <div >
                <h2  style="font-family: 'Vollkorn', serif; text-align:center">{{company.company}}</h2>
                <b-icon icon="building"></b-icon>
              </div>
            </b-navbar-brand>
            <b-nav-item style="text-align: center;width: 100%;" @click="onProfileView()">Profile</b-nav-item>
            <b-nav-item style="text-align: center;width: 100%;" @click="onjobView()">Jobs</b-nav-item>
          </b-nav>
        </b-col>
        <!--/.Local Navbar -->
        <b-col fluid lg="10" cols="12">
          <div v-if="this.profileView && !this.jobView">
            <h2 style="font-family: 'Vollkorn', serif"> Company Profile </h2>
            <div class="container-md-5 p-2 align-items-center">
              <!-- company descripcion -->
              <div v-if="company.description != null && !edit.description " class="bio-text">
                {{company.description}}
                <p></p>
              </div>
              <div v-if="company.description === null && !edit.description && edit_mode" class="bio-text">
                {{bio}}
                <p></p>
              </div>
              <b-container v-if="edit.description" fluid>
                <b-row align="center">
                  <b-col sm="10">
                    <b-form-textarea v-model="modify.description" id="textarea-auto-height" rows="3" max-rows="8"/>
                  </b-col>
                  <b-col align-self="center" sm="1">
                    <b-button variant="success" @click="modifyDescription()">Save</b-button>
                  </b-col>
                </b-row>
                <p></p>
              </b-container>
              <button v-if="edit_mode" class="btn btn-sm" style="margin-bottom: 5px; margin-left: 20px" @click="editDescription()" ><b-icon-pencil-fill font-scale="1.5" shift-v="-2"></b-icon-pencil-fill></button>
              <!-- /company descripcion -->
              <div class="text-left p-2 pb-3" style="max-width: 50rem">
                <h3 style="font-family: 'Vollkorn', serif"> Email</h3>
                <p>{{company.email}}</p>
              </div>
              <!-- company sector -->
              <div v-if="(company.sector !== 'Unknown' && company.sector) || edit_mode " class="text-left p-2 pb-3" style="max-width: 50rem">
                <h3 style="font-family: 'Vollkorn', serif"> Sector</h3>
                <div v-if="!edit.sector">
                  <p>{{company.sector}}</p>
                </div>
                <b-container v-if="edit.sector" fluid>
                  <b-row align="left">
                    <b-col sm="5">
                      <b-form-textarea v-model="modify.sector" id="textarea-auto-height" rows="1" max-rows="2"/>
                    </b-col>
                    <b-col align-self="center" sm="1">
                      <b-button variant="success" @click="modifySector()">Save</b-button>
                    </b-col>
                  </b-row>
                  <p></p>
                </b-container>
                <button v-if="edit_mode" class="btn btn-sm" style="margin-bottom: 5px; margin-left: 20px" @click="editSector()" ><b-icon-pencil-fill font-scale="1.5" shift-v="-2"></b-icon-pencil-fill></button>
              </div>
              <!-- /company sector -->
              <!-- company location -->
              <div v-if="(company.location !== 'Unknown' && company.location) || edit_mode " class="text-left p-2 pb-3" style="max-width: 50rem">
                <h3 style="font-family: 'Vollkorn', serif"> Location</h3>
                <div v-if="!edit.location">
                  <p>{{company.location}}</p>
                </div>
                <b-container v-if="edit.location" fluid>
                  <b-row align="left">
                    <b-col sm="5">
                      <b-form-textarea v-model="modify.location" id="textarea-auto-height" rows="1" max-rows="2"/>
                    </b-col>
                    <b-col align-self="center" sm="1">
                      <b-button variant="success" @click="modifyLocation()">Save</b-button>
                    </b-col>
                  </b-row>
                  <p></p>
                </b-container>
                <button v-if="edit_mode" class="btn btn-sm" style="margin-bottom: 5px; margin-left: 20px" @click="editLocation()" ><b-icon-pencil-fill font-scale="1.5" shift-v="-2"></b-icon-pencil-fill></button>
              </div>
              <!-- /company location -->
            </div>
          </div>
          <div v-show="this.profileView === false && this.jobView === true">
            <h2 style="font-family: 'Vollkorn', serif"> Job Offers </h2>
          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios'
import Vue from 'vue'
import {mapState} from 'vuex'

export default {
  data () {
    return {
      edit: {
        description: false,
        sector: false,
        location: false
      },
      modify: {
        description: '',
        sector: '',
        location: ''
      },
      company: {
        company: '',
        email: '',
        description: '',
        job_offers: '',
        sector: '',
        location: ''
      },
      profileView: true,
      jobView: false,
      logged: false,
      is_jobseeker: true,
      is_company: false,
      is_admin: false,
      token: '',
      username: '',
      company_name_profile: '',
      edit_mode: false,
      bio: 'Add your bio here'
    }
  },
  methods: {
    onHome () {
      this.$router.replace({ path: '/' })
    },
    onLogIn () {
      this.$router.replace({ path: '/login' })
    },
    onCompanies () {
      this.$router.replace({ path: '/companies' })
    },
    onProfileView () {
      this.profileView = true
      this.jobView = false
    },
    onjobView () {
      this.profileView = false
      this.jobView = true
      this.edit.description = false
      this.edit.sector = false
      this.edit.location = false
    },
    onLogOut () {
      this.$store.commit('logout')
      this.$router.replace({ path: '/' })
    },
    onJobPostings () {
      this.$router.replace({ path: '/job_postings' })
    },
    onAboutUs () {
      this.$router.replace({ path: '/about_us' })
    },
    editDescription () {
      this.edit.description = !this.edit.description
      this.modify.description = this.company.description
    },
    editSector () {
      this.edit.sector = !this.edit.sector
      this.modify.sector = this.company.sector
    },
    editLocation () {
      this.edit.location = !this.edit.location
      this.modify.location = this.company.location
    },

    modifyDescription () {
      const pathCompany = Vue.prototype.$API_BASE_URL + 'company/' + this.company_name_profile.toLowerCase()
      const values = {
        description: this.modify.description
      }
      axios.put(pathCompany, values, {
        auth: {username: this.token}})
        .then((res) => {
          this.getCompany()
          this.edit.description = !this.edit.description
        })
        .catch((error) => {
          console.error(error)
          alert(' An error occurred creating the account')
        })
    },
    modifySector () {
      const pathCompany = Vue.prototype.$API_BASE_URL + 'company/' + this.company_name_profile.toLowerCase()
      const values = {
        sector: this.modify.sector
      }
      axios.put(pathCompany, values)
        .then((res) => {
          this.getCompany()
          this.edit.sector = !this.edit.sector
        })
        .catch((error) => {
          console.error(error)
          alert(' An error occurred creating the account')
        })
    },
    modifyLocation () {
      const pathCompany = Vue.prototype.$API_BASE_URL + 'company/' + this.company_name_profile.toLowerCase()
      const values = {
        location: this.modify.location
      }
      axios.put(pathCompany, values)
        .then((res) => {
          this.getCompany()
          this.edit.location = !this.edit.location
        })
        .catch((error) => {
          console.error(error)
          alert(' An error occurred creating the account')
        })
    },
    getCompany () {
      const pathCompany = Vue.prototype.$API_BASE_URL + 'company/' + this.company_name_profile.toLowerCase()
      axios.get(pathCompany)
        .then((res) => {
          console.log(res)
          this.company.company = res.data.account.company
          this.company.email = res.data.account.email
          this.company.description = res.data.account.description
          this.company.job_offers = res.data.account.job_offers
          this.company.location = res.data.account.location
          this.company.sector = res.data.account.sector
        })
        .catch(() => {
          this.company.company = 'Name'
          this.company.email = 'Email'
          this.company.description = 'Description'
          this.company.job_offers = 'Job_offers'
          this.company.location = 'Location'
          this.company.sector = 'sector'
        })
    }
  },
  created () {
    this.company_name_profile = this.$route.path.split('company/')[1].toLowerCase()
    this.logged = this.$store.state.logged
    this.username = this.$store.state.username
    this.is_jobseeker = this.$store.state.isJobSeeker
    this.is_company = this.$store.state.isCompany
    this.token = this.$store.state.token
    this.is_admin = this.$store.state.isAdmin
    this.edit_mode = this.username === this.company_name_profile
    this.getCompany()
  },
  computed: mapState({
    token: state => state.token,
    logged: state => state.logged,
    username: state => state.username,
    isJobSeeker: state => state.isJobSeeker,
    isCompany: state => state.isCompany,
    isAdmin: state => state.isAdmin
  })
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
