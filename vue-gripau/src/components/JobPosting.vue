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
      <!-- Job offer view (el que hi havia a company profile) -->
      <div id="jobOfferCompanyView" class="job-offer-container">
        <h2 id="jobOfferJobName" class="job-offer-title">{{job_name}}</h2>
        <div class="container">
          <div class="row row-attributes">
            <div class="col-12">
              <div id="descriptionJobOffer" v-if="description !== '' && description !== null" class="job-offer-field-container">
                <p class="job-offer-field-text">{{description}}</p>
              </div>
            </div>
            <div class="col-12 col-sm-12 col-lg-6">
              <div id="companyNameJobOffer" v-if="company_name !== '' && company_name !== null" class="job-offer-field-container">
                <p class="job-offer-field-text"><b-icon id="companyIcon" icon="building"></b-icon>{{company_name}}</p>
              </div>
            </div>
            <div class="col-12 col-sm-12 col-lg-6">
              <div id="locationJobOffer" v-if="location !== '' && location !== null" class="job-offer-field-container">
                <p class="job-offer-field-text"><b-icon id="locationIcon2" icon="geo-alt-fill"></b-icon>{{location}}</p>
              </div>
            </div>
            <div class="col-12 col-sm-12 col-lg-6">
              <div id="contractTypeJobOffer" v-if="contract_type !== '' && contract_type !== null" class="job-offer-field-container">
                <p class="job-offer-field-text"><b-icon id="contractIcon" icon="journal-text"></b-icon>{{contract_type}} contract</p>
              </div>
            </div>
            <div class="col-12 col-sm-12 col-lg-6">
              <div id="workingHoursJobOffer" v-if="working_hours !== '' && working_hours !== null" class="job-offer-field-container">
                <p class="job-offer-field-text"><b-icon id="hoursIcon" icon="hourglass-split"></b-icon>{{working_hours}} hours/week</p>
              </div>
            </div>
            <div class="col-12 col-sm-12 col-lg-6">
              <div id="salaryJobOffer" v-if="salary !== '' && salary !== null" class="job-offer-field-container">
                <p class="job-offer-field-text"><b-icon id="salaryIcon" icon="cash"></b-icon>{{salary}}</p>
              </div>
            </div>
            <div class="col-12 col-sm-12 col-lg-6">
              <div id="publicationDateJobOffer" v-if="publication_date !== '' && publication_date !== null" class="job-offer-field-container">
                <p class="job-offer-field-text"><b-icon id="salaryIcon" icon="calendar-day"></b-icon>First published on: {{publication_date}}</p>
              </div>
            </div>
            <div class="col-12 col-sm-12 col-lg-6 job-offer-button-back">
              <b-button id="seenButton" btn variant="warning" class='btn-home' @click="onSeenOffer()">
                Back
              </b-button>
            </div>
            <div v-if="edit_mode" class="col-12 col-sm-12 col-lg-6 job-offer-button-delete">
              <b-button id="deleteButton" v-if="this.is_company && this.company_name_profile === this.username" btn variant="danger" class='m-2' @click="deleteJobOffer()">
                <!--<b-icon id="salaryIcon" icon="trash"></b-icon>--> Delete
              </b-button>
            </div>
            <div v-if="is_jobseeker && logged" class="col-12 col-sm-12 col-lg-6">
              <b-button id="applyButton" class="job-offer-button-apply" v-if="!applied" v-b-modal.modal-apply variant="success">Apply</b-button>
              <b-button id="appliedButton" class="job-offer-button-apply" v-else disabled variant="outline-success">Applied</b-button>
            </div>
          </div>
        </div>

        <!--<b-button id="applyButton" v-if="!applied && is_jobseeker && logged" v-b-modal.modal-apply variant="success">Apply</b-button>-->
        <!--<b-button id="appliedButton" v-if="applied && is_jobseeker && logged " disabled variant="outline-success">Applied</b-button>-->
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
                id="applyMessageInput"
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
      <!-- /Job offer view (el que hi havia a company profile) -->
      <h2 id="jobOfferJobName" style="font-family: 'Vollkorn', serif">{{job_name}}</h2>
      <b-container fluid >
        <b-row>
          <b-col align="left">
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
          </b-col>
          <b-col align="left" v-if="this.is_company && this.company === this.username">
            <b-card>
              <p>Applicants</p>
              <div>
                <b-table :fields="fields" striped hover :items="this.applicants_list">
                    <template #cell(Profile)="data">
                      <router-link :to="`/job_seeker/${data.value}`">{{data.value}}</router-link>
                    </template>
                </b-table>
              </div>
            </b-card>
          </b-col>
        </b-row>
      </b-container>
      <b-button id="seenButton" btn variant="warning" class='btn-home' @click="onJobPostings">Seen</b-button>
      <b-button id="deleteButton" v-if="this.is_company && this.company === this.username" btn variant="danger" class='m-2' @click="deleteJobOffer()">Delete Job Offer</b-button>
      <b-button id="applyButton" v-if="!applied && is_jobseeker && logged" v-b-modal.modal-apply variant="success">Apply</b-button>
      <b-button id="appliedButton" v-if="applied && is_jobseeker && logged" disabled variant="outline-success">Applied</b-button>
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
              id="applyMessageInput"
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
      applyMessage: null,
      applicants_list: []
    }
  },
  methods: {
    getApplicants () {
      const path = Vue.prototype.$API_BASE_URL + 'offer_applicants/' + this.id
      axios.get(path, {
        auth: {username: this.token}})
        .then((res) => {
          this.applicants_list = []
          for (let applicant in res.data) {
            this.applicants_list.push({'Name': res.data[applicant].name, 'Email': res.data[applicant].email, 'Profile': res.data[applicant].username})
          }
        })
        // eslint-disable-next-line
        .catch((error) => {
          // eslint-disable-next-line
           console.error(error)
        })
    },
    getApplied () {
      const path = Vue.prototype.$API_BASE_URL + 'application/' + this.username + '/' + this.id
      axios.get(path, {
        auth: {username: this.token}})
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
      axios.delete(path, {
        auth: {username: this.token}})
        .then((res) => {
          this.onJobPostings()
        })
        .catch((error) => {
          console.error(error)
        })
    },
    onSeenOffer () {
      this.$router.go(-1)
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
    if (this.logged) {
      if (this.is_jobseeker) {
        this.getApplied()
      } else {
        this.getApplicants()
      }
    }
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
