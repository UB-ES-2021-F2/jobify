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
          <b-nav-item id="jobPostingsNavbarButton" active>Job postings</b-nav-item>
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
    <!-- Job offers company view -->
    <div id="jobPostingsView" v-show="!this.jobOfferView">
      <h2 style="font-family: 'Vollkorn"> {{ message }} </h2>
      <b-container fluid>
        <b-row align-h="center" v-if="is_company">
          <b-card
            tag="article"
            class="text-center mb-2"
            style="width: 90%; max-width: 600px"
            id="addJobOfferCard"
          >
            <b-link id="showJobOfferModal" v-b-modal.job-offer-modal style="position: absolute; top:0; left:0; height: 100%; width:100%"></b-link>
            <p class="h1" style="margin:0 auto"><b-icon icon="patch-plus"></b-icon></p>
          </b-card>
        </b-row>
        <b-row align-h="center" v-for="(job_offer) in job_offers" :key="job_offer.id">
          <b-card
            :title="job_offer.job_name"
            tag="article"
            class="mb-2"
            style="width: 90%; max-width: 600px; font-family: 'Work Sans SemiBold'"
            align="left"
            id="jobOfferCard"
          >
            <b-button id="jobOfferButton" class="btn btn-outline-light active" @click="onJobOffer(job_offer.id)" style="background-color:transparent; position: absolute; top:0; left:0; height: 100%; width:100%"></b-button>
            <b-card-text id="companyName">
              <p>{{ job_offer.company_name }}</p>
            </b-card-text>
            <footer>
              <b-container fluid style="font-family: 'Work Sans'">
                <b-row no-gutters>
                  <b-col lg v-if="job_offer.contract_type.length > 0">
                    <b-icon id="contractTypeIcon" icon="briefcase"></b-icon> {{job_offer.contract_type}}
                  </b-col>
                  <b-col lg v-if="job_offer.working_hours > 0">
                    <b-icon id="workingHoursIcon" icon="alarm"></b-icon> {{job_offer.working_hours}} h
                  </b-col>
                  <b-col lg>
                    <b-icon id="publicationDateIcon" icon="calendar3-event"></b-icon> {{ job_offer.publication_date }}
                  </b-col>
                  <b-col lg>
                    <b-icon id="locationIcon" icon="geo-alt-fill"></b-icon> {{ job_offer.location }}
                  </b-col>
                </b-row>
              </b-container>
            </footer>
          </b-card>
        </b-row>
      </b-container>
      <b-modal ref="jobOfferModal"
               id="job-offer-modal"
               title="Post a job offer"
               hide-footer
               hide-backdrop
      >
        <validation-observer ref="observer" v-slot="{ handleSubmit }">
          <b-form style="font-family:'Work Sans'" @submit.prevent="handleSubmit(onSubmitNewOffer)">
            <ValidationProvider name="JobName"  rules="alpha_spaces|required:true|max: 50" v-slot="validationContext">
              <b-form-group id="input-group-1" label="Job name" label-for="input-1">
                <b-form-input id="jobNameInput" v-model="jobOfferForm.jobName" placeholder="" type="text" :state="getValidationState(validationContext)"
                              aria-describedby="input-1-live-feedback"></b-form-input>
                <b-form-invalid-feedback id="input-1-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
              </b-form-group>
            </ValidationProvider>

            <validation-provider name="Salary"  rules="max:30" v-slot="validationContext">
              <b-form-group id="input-group-3" label="Salary" label-for="input-3">
                <b-form-input id="salaryInput" v-model="jobOfferForm.salary" type="text" :state="getValidationState(validationContext)"
                              aria-describedby="input-3-live-feedback" placeholder="e.g. '15€/hour'"></b-form-input>
                <b-form-invalid-feedback id="input-3-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
              </b-form-group>
            </validation-provider>

            <validation-provider name="Location"  rules="required:true|max: 40" v-slot="validationContext">
              <b-form-group id="input-group-1" label="Location" label-for="input-1">
                <b-form-input id="locationInput" v-model="jobOfferForm.location" placeholder="e.g. 'Barcelona', 'Remote'" type="text" :state="getValidationState(validationContext)"
                              aria-describedby="input-1-live-feedback"></b-form-input>
                <b-form-invalid-feedback id="input-1-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
              </b-form-group>
            </validation-provider>

            <validation-provider name="ContractType"  :rules="{ max: 500, required:true}" v-slot="validationContext">
              <b-form-group id="input-group-2" label="Contract type" label-for="input-2">
                <b-form-select id="contractTypeInput" v-model="jobOfferForm.contractType" :options="optionsContractType" placeholder="" type="text" :state="getValidationState(validationContext)"
                               aria-describedby="input-2-live-feedback"></b-form-select>
                <b-form-invalid-feedback id="input-2-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
              </b-form-group>
            </validation-provider>

            <validation-provider name="WorkingHours"  rules="numeric|max:60" v-slot="validationContext">
              <b-form-group id="input-group-3" label="Weekly working hours" label-for="input-3">
                <b-form-input id="workingHoursInput" v-model="jobOfferForm.workingHours" placeholder="" type="number" :state="getValidationState(validationContext)"
                              aria-describedby="input-3-live-feedback"></b-form-input>
                <b-form-invalid-feedback id="input-3-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
              </b-form-group>
            </validation-provider>

            <validation-provider name="Description"  :rules="{ max: 2000}" v-slot="validationContext">
              <b-form-group id="input-group-2" label="Description" label-for="input-2">
                <b-form-textarea id="descriptionInput" v-model="jobOfferForm.description" :state="getValidationState(validationContext)"
                                 aria-describedby="input-2-live-feedback"  rows="5"
                                 placeholder="(Optional) Description of the job, requirements, job benefits, etc."></b-form-textarea>
                <b-form-invalid-feedback id="input-2-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
              </b-form-group>
            </validation-provider>

            <div class="d-grid gap-2 d-md-flex justify-content-md-end">
              <button id="postJobOfferButton" class="btn btn-warning justify-content-md-end">Post Job Offer!</button>
            </div>
          </b-form>
        </validation-observer>
      </b-modal>
    </div>
    <!-- /Job offers company view -->
    <!-- Job offer view -->
    <div id="jobOfferView" v-if="this.jobOfferView">
      <h2 id="jobOfferJobName" style="font-family: 'Vollkorn', serif">{{jobOfferCurrentView.jobName}}</h2>
      <b-container align="left">
        <div id="descriptionJobOffer" v-if="jobOfferCurrentView.description !== '' && jobOfferCurrentView.description !== null" class="p-2 pb-3" style="max-width: 50rem">
          <h4 style="font-family: 'Vollkorn', serif"> Description</h4>
          <p>{{jobOfferCurrentView.description}}</p>
        </div>
        <div id="companyNameJobOffer" v-if="jobOfferCurrentView.companyName !== '' && jobOfferCurrentView.companyName !== null" class="p-2 pb-3" style="max-width: 50rem">
          <h4 style="font-family: 'Vollkorn', serif"> Company</h4>
          <p>{{jobOfferCurrentView.companyName}}</p>
        </div>
        <div id="locationJobOffer" v-if="jobOfferCurrentView.location !== '' && jobOfferCurrentView.location !== null" class="p-2 pb-3" style="max-width: 50rem">
          <h4 style="font-family: 'Vollkorn', serif"> Location</h4>
          <p>{{jobOfferCurrentView.location}}</p>
        </div>
        <div id="contractTypeJobOffer" v-if="jobOfferCurrentView.contractType !== '' && jobOfferCurrentView.contractType !== null" class="p-2 pb-3" style="max-width: 50rem">
          <h4 style="font-family: 'Vollkorn', serif"> Contract type</h4>
          <p>{{jobOfferCurrentView.contractType}}</p>
        </div>
        <div id="workingHoursJobOffer" v-if="jobOfferCurrentView.workingHours !== '' && jobOfferCurrentView.workingHours !== null" class="p-2 pb-3" style="max-width: 50rem">
          <h4 style="font-family: 'Vollkorn', serif"> Weekly working hours</h4>
          <p>{{jobOfferCurrentView.workingHours}}</p>
        </div>
        <div id="salaryJobOffer" v-if="jobOfferCurrentView.salary !== '' && jobOfferCurrentView.salary !== null" class="p-2 pb-3" style="max-width: 50rem">
          <h4 style="font-family: 'Vollkorn', serif"> Salary</h4>
          <p>{{jobOfferCurrentView.salary}}</p>
        </div>
        <div id="publicationDateJobOffer" v-if="jobOfferCurrentView.publicationDate !== '' && jobOfferCurrentView.publicationDate !== null" class="p-2 pb-3" style="max-width: 50rem">
          <h4 style="font-family: 'Vollkorn', serif"> Publication date</h4>
          <p>{{jobOfferCurrentView.publicationDate}}</p>
        </div>
      </b-container>
      <b-button id="seenButton" btn variant="warning" class='btn-home' @click="onJobOfferView">Seen</b-button>
      <b-button id="deleteButton" v-if="this.is_company" btn variant="danger" class='m-2' @click="deleteJobOffer()">Delete Job Offer</b-button>
    </div>
    <!-- /Job offer view -->
  </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import {mapState} from 'vuex'

export default {
  data () {
    return {
      message: 'Job Postings',
      logged: false,
      job_offers: [], // {'id': 0, 'jobName': 'Waiter', 'company': 'Terra Restaurant', 'description': 'This offer is fake and it will be deleted in the next update', 'type': 'Part time'}, {'id': 1, 'jobName': 'Journalist', 'company': 'The Sun', 'description': 'This offer is fake and it will be deleted in the next update', 'type': 'Part time'}],
      username: '',
      token: '',
      is_jobseeker: true,
      is_company: false,
      is_admin: false,
      jobOfferView: false,
      jobOfferForm: {
        jobName: '',
        description: '',
        salary: '',
        location: '',
        contractType: '',
        workingHours: ''
      },
      jobOfferCurrentView: {
        id: '',
        company: '',
        publicationDate: '',
        companyName: '',
        jobName: '',
        description: '',
        salary: '',
        location: '',
        contractType: '',
        workingHours: ''
      },
      optionsContractType: ['Indefinite', 'Fixed-term', 'Zero Hours', 'Internship', 'Self-employment', 'Apprentice']
    }
  },
  methods: {
    onHome () {
      this.$router.replace({ path: '/' })
    },
    getValidationState ({ dirty, validated, valid = null }) {
      return dirty || validated ? valid : null
    },
    onProfile () {
      if (this.is_jobseeker && this.logged) {
        this.$router.replace({ path: '/job_seeker/' + this.username })
      } else if (this.is_company && this.logged) {
        this.$router.replace({path: '/company/' + this.username})
      }
    },
    onLogIn () {
      this.$router.replace({ path: '/login' })
    },
    onCompanies () {
      this.$router.replace({ path: '/companies' })
    },
    onLogOut () {
      this.$store.commit('logout')
      this.$router.replace({ path: '/' })
    },
    onJobOfferView () {
      this.jobOfferView = !this.jobOfferView
    },
    onAboutUs () {
      this.$router.replace({ path: '/about_us' })
    },
    onJobOffer (id) {
      const path = Vue.prototype.$API_BASE_URL + 'job_offer/' + id
      axios.get(path)
        .then((res) => {
          this.jobOfferCurrentView.companyName = res.data.offer.company_name
          this.jobOfferCurrentView.jobName = res.data.offer.job_name
          this.jobOfferCurrentView.description = res.data.offer.description
          this.jobOfferCurrentView.publicationDate = res.data.offer.publication_date
          this.jobOfferCurrentView.salary = res.data.offer.salary
          this.jobOfferCurrentView.location = res.data.offer.location
          this.jobOfferCurrentView.workingHours = res.data.offer.working_hours
          this.jobOfferCurrentView.contractType = res.data.offer.contract_type
          this.jobOfferCurrentView.id = res.data.offer.id
          this.jobOfferCurrentView.company = res.data.offer.company
          this.onJobOfferView()
        })
        .catch((error) => {
          console.error(error)
        })
    },
    getJobOffers () {
      const path = Vue.prototype.$API_BASE_URL + 'offers'
      axios.get(path)
        .then((res) => {
          this.job_offers = []
          for (var jobOffer in res.data.OfferList) {
            jobOffer = res.data.OfferList[jobOffer]
            console.log(jobOffer)
            jobOffer.publication_date = jobOffer.publication_date.split('T')[0]
            this.job_offers.push(jobOffer)
          }
        })
        .catch((error) => {
          console.error(error)
        })
    },
    onSubmitNewOffer () {
      const path = Vue.prototype.$API_BASE_URL + 'job_offer/' + this.username
      var values = {
        job_name: this.jobOfferForm.jobName,
        description: this.jobOfferForm.description,
        location: this.jobOfferForm.location,
        contract_type: this.jobOfferForm.contractType
      }
      if (!isNaN(this.jobOfferForm.salary)) {
        values.salary = this.jobOfferForm.salary
      }
      if (!isNaN(this.jobOfferForm.workingHours)) {
        values.working_hours = this.jobOfferForm.workingHours
      }
      console.log(values)
      axios.post(path, values, {
        auth: {username: this.token}})
        .then((res) => {
          console.log('Job Offer correctly posted')
          this.getJobOffers()
        })
        .catch((error) => {
          alert(error.response.data.message)
        })
      this.$bvModal.hide('job-offer-modal')
      this.onReset()
    },
    initJobOfferForm () {
      this.jobOfferForm.jobName = ''
      this.jobOfferForm.description = ''
      this.jobOfferForm.salary = ''
      this.jobOfferForm.vacancyNumber = ''
      this.jobOfferForm.location = ''
      this.jobOfferForm.contractType = ''
      this.jobOfferForm.workingHours = ''
      this.jobOfferForm.minimumExperience = ''
    },
    deleteJobOffer () {
      const path = Vue.prototype.$API_BASE_URL + 'job_offer/' + this.jobOfferCurrentView.id
      axios.delete(path)
        .then((res) => {
          window.location.reload()
        })
        .catch((error) => {
          console.error(error)
        })
    },
    onReset () {
      this.initJobOfferForm()
    }
  },
  created () {
    this.logged = this.$store.state.logged
    this.username = this.$store.state.username
    this.is_jobseeker = this.$store.state.isJobSeeker
    this.is_company = this.$store.state.isCompany
    this.token = this.$store.state.token
    this.is_admin = this.$store.state.isAdmin
    this.getJobOffers()
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
