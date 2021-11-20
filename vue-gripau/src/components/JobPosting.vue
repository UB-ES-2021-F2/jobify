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
          <b-nav-item id="jobPostingsNavbarButton" @click="onJobPostings()" active>Job postings</b-nav-item>
          <b-nav-item id="companiesNavbarButton" @click="onCompanies()">Companies</b-nav-item>
          <b-nav-item id="aboutUsNavbarButton" @click="onAboutUs()">About Us</b-nav-item>
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

    <div id="jobOfferView">
      <h2 id="jobOfferJobName" style="font-family: 'Vollkorn', serif">{{job_name}}</h2>
      <b-container align="left">
        <div id="descriptionJobOffer" v-if="description !== '' && description !== null" class="p-2 pb-3" style="max-width: 50rem">
          <h4 style="font-family: 'Vollkorn', serif"> Description</h4>
          <p>{{description}}</p>
        </div>
        <div id="companyNameJobOffer" v-if="company_name !== '' && company_name !== null" class="p-2 pb-3" style="max-width: 50rem">
          <h4 style="font-family: 'Vollkorn', serif"> Company</h4>
          <p>{{company_name}}</p>
        </div>
        <div id="locationJobOffer" v-if="location !== '' && location !== null" class="p-2 pb-3" style="max-width: 50rem">
          <h4 style="font-family: 'Vollkorn', serif"> Location</h4>
          <p>{{location}}</p>
        </div>
        <div id="contractTypeJobOffer" v-if="contract_type !== '' && contract_type !== null" class="p-2 pb-3" style="max-width: 50rem">
          <h4 style="font-family: 'Vollkorn', serif"> Contract type</h4>
          <p>{{contract_type}}</p>
        </div>
        <div id="workingHoursJobOffer" v-if="working_hours !== '' && working_hours !== null" class="p-2 pb-3" style="max-width: 50rem">
          <h4 style="font-family: 'Vollkorn', serif"> Weekly working hours</h4>
          <p>{{working_hours}}</p>
        </div>
        <div id="salaryJobOffer" v-if="salary !== '' && salary !== null" class="p-2 pb-3" style="max-width: 50rem">
          <h4 style="font-family: 'Vollkorn', serif"> Salary</h4>
          <p>{{salary}}</p>
        </div>
        <div id="publicationDateJobOffer" v-if="publication_date !== '' && publication_date !== null" class="p-2 pb-3" style="max-width: 50rem">
          <h4 style="font-family: 'Vollkorn', serif"> Publication date</h4>
          <p>{{publication_date}}</p>
        </div>
      </b-container>
      <b-button id="seenButton" btn variant="warning" class='btn-home' @click="onJobPostings">Seen</b-button>
      <b-button id="deleteButton" v-if="this.is_company && this.company === this.username" btn variant="danger" class='m-2' @click="deleteJobOffer()">Delete Job Offer</b-button>
      <b-button v-if="!applied && is_jobseeker && logged" v-b-modal.modal-apply variant="success">Apply</b-button>
      <b-button v-if="applied && is_jobseeker && logged" disabled variant="outline-success">Applied</b-button>
      <b-modal
        hide-backdrop
        id="modal-apply"
        ref="modal"
        title="Do you want to add some additional information?"
        @ok="applyAction"
        @show="resetApplyModal"
        @hidden="resetApplyModal"
      >
        <form ref="form">
          <b-form-group
            label-for="name-input"
          >
            <b-form-textarea
              v-model="applyMessage"
              placeholder="Write here (optional)"
              rows="3"
              max-rows="6"
            >

            </b-form-textarea>
          </b-form-group>
        </form>
      </b-modal>
    </div>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import Vue from 'vue'
import axios from 'axios'
export default {
  data () {
    return {
      message: 'Job Postings',
      logged: false,
      username: '',
      token: '',
      is_jobseeker: true,
      is_company: false,
      is_admin: false,
      id: '',
      company: '',
      publication_date: '',
      company_name: '',
      job_name: '',
      description: '',
      salary: '',
      location: '',
      contract_type: '',
      working_hours: '',
      applied: false,
      applyMessage: null
    }
  },
  methods: {
    getApplied () {
      const path = Vue.prototype.$API_BASE_URL + '/application/' + this.username + '/' + this.id
      axios.get(path)
        .then((res) => {
          var application = res.data.application
          console.log(application)
          this.applied = true
        })
        // eslint-disable-next-line
        .catch((error) => {
          // eslint-disable-next-line
          // console.error(error)
          this.applied = false
        })
    },
    applyAction () {
      if (!this.applied) {
        const path = Vue.prototype.$API_BASE_URL + 'application/' + this.username
        const values = {
          job_offer_id: this.id
        }
        if (this.applyMessage !== null) {
          values.info = this.applyMessage
        }
        axios.post(path, values, {
          auth: {username: this.token}})
          .then((res) => {
            console.log('Job Offer correctly applied')
            this.applied = true
          })
          .catch((error) => {
            alert(error.response.data.message)
          })
      }
    },
    resetApplyModal () {
      this.applyMessage = null
    },
    onHome () {
      this.$router.push('/')
    },
    getValidationState ({dirty, validated, valid = null}) {
      return dirty || validated ? valid : null
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
    onAboutUs () {
      this.$router.push('/about_us')
    },
    getJobOffer (id) {
      const path = Vue.prototype.$API_BASE_URL + 'job_offer/' + id
      axios.get(path)
        .then((res) => {
          this.company = res.data.offer.company
          this.publication_date = res.data.offer.publication_date.split('T')[0]
          this.company_name = res.data.offer.company_name
          this.job_name = res.data.offer.job_name
          this.description = res.data.offer.description
          this.salary = res.data.offer.salary
          this.location = res.data.offer.location
          this.contract_type = res.data.offer.contract_type
          this.working_hours = res.data.offer.working_hours
        })
        .catch((error) => {
          console.error(error)
        })
    },
    deleteJobOffer () {
      const path = Vue.prototype.$API_BASE_URL + 'job_offer/' + this.id
      axios.delete(path)
        .then((res) => {
          this.onJobPostings()
        })
        .catch((error) => {
          console.error(error)
        })
    }
  },
  created () {
    this.logged = this.$store.state.logged
    this.username = this.$store.state.username
    this.is_jobseeker = this.$store.state.isJobSeeker
    this.is_company = this.$store.state.isCompany
    this.token = this.$store.state.token
    this.is_admin = this.$store.state.isAdmin
    this.id = this.$route.path.split('job_posting/')[1]
    this.getApplied()
    this.getJobOffer(this.id)
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

<style scoped>
</style>
