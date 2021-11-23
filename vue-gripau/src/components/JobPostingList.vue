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
      <h2 class="title-offer"> {{ message }} </h2>
      <b-link v-if="is_company" id="showJobOfferModal" class="add-offer" v-b-modal.job-offer-modal>
        <b-icon icon="patch-plus" font-scale="2"></b-icon>
      </b-link>
      <b-container fluid>
        <!--<b-row align-h="center" v-if="is_company">
          <b-card
            tag="article"
            class="text-center mb-2"
            style="width: 90%; max-width: 600px"
            id="addJobOfferCard"
          >
            <b-button id="addJobOfferButton" v-b-modal.job-offer-modal class="btn btn-outline-light active" style="background-color:transparent; position: absolute; top:0; left:0; height: 100%; width:100%"></b-button>
            <p class="h1" style="margin:0 auto"><b-icon icon="patch-plus"></b-icon></p>
          </b-card>
        </b-row>-->
        <b-row align-h="center" v-for="(job_offer) in job_offers" :key="job_offer.id">
          <b-card
            tag="article"
            class="mb-2"
            style="width: 90%; max-width: 600px; font-family: 'Work Sans SemiBold'"
            align="left"
            id="jobOfferCard"
          >
            <div>
              <b-container fluid style="font-family: 'Work Sans'">
                <b-row no-gutters>
                  <b-col cols="8">
                    <b-card-text id="companyName" >
                      <p class="titleJobOfferCard">{{ job_offer.job_name }}</p>
                      <p class="companyNameJobOfferCard">{{ job_offer.company_name }}</p>
                    </b-card-text>
                    <b-col lg v-if="job_offer.contract_type !== null && job_offer.contract_type !== ''">
                      <b-icon id="contractTypeIcon" icon="briefcase"></b-icon> {{job_offer.contract_type}}
                    </b-col>
                    <!--<b-col lg v-if="job_offer.working_hours > 0">
                      <b-icon id="workingHoursIcon" icon="alarm"></b-icon> {{job_offer.working_hours}} h
                    </b-col> potser no posarho a la card-->
                    <b-col lg>
                      <b-icon id="publicationDateIcon" icon="calendar3-event"></b-icon> {{ job_offer.publication_date }}
                    </b-col>
                    <b-col lg>
                      <b-icon id="locationIcon" icon="geo-alt-fill"></b-icon> {{ job_offer.location }}
                    </b-col>
                  </b-col>
                  <b-col v-if="companies_logos[job_offer.company]!=null" cols="4">
                    <img class="card-img" :src="companies_logos[job_offer.company]" alt=""
                         style="width:128px;height:128px">
                  </b-col>
                  <b-col v-if="companies_logos[job_offer.company]==null" cols="4">
                    <img class="card-img" src="../assets/images/company_avatar.png" alt=""
                         style="width:128px;height:128px">
                  </b-col>
                </b-row>
              </b-container>
              <b-button id="jobOfferButton" class="btn btn-outline-light active" @click="onJobOffer(job_offer.id)" style="background-color:transparent; position: absolute; top:0; left:0; height: 100%; width:100%"></b-button>
            </div>
          </b-card>
        </b-row>
      </b-container>
      <b-modal ref="jobOfferModal"
               id="job-offer-modal"
               title="Post a job offer"
               hide-footer
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

            <validation-provider name="ContractType"  :rules="{ max: 500}" v-slot="validationContext">
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
  </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import {mapState} from 'vuex'
import firebase from 'firebase/compat'

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
      jobOfferForm: {
        jobName: '',
        description: '',
        salary: '',
        location: '',
        contractType: '',
        workingHours: ''
      },
      optionsContractType: ['Indefinite', 'Fixed-term', 'Zero Hours', 'Internship', 'Self-employment', 'Apprentice'],
      companies_logos: {}
    }
  },
  methods: {
    onHome () {
      this.$router.push('/')
    },
    getValidationState ({ dirty, validated, valid = null }) {
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
      this.$router.push({ path: '/companies' })
    },
    onLogOut () {
      this.$store.commit('logout')
      this.$router.push('/')
    },
    onAboutUs () {
      this.$router.push('/about_us')
    },
    onJobOffer (id) {
      this.$router.push('/job_posting/' + id)
    },
    getJobOffers () {
      const path = Vue.prototype.$API_BASE_URL + 'offers'
      axios.get(path)
        .then((res) => {
          this.job_offers = []
          for (var jobOffer in res.data.OfferList) {
            jobOffer = res.data.OfferList[jobOffer]
            jobOffer.publication_date = jobOffer.publication_date.split('T')[0]
            this.job_offers.push(jobOffer)
            this.getCompaniesLogos()
          }
        })
        .catch((error) => {
          console.error(error)
        })
    },
    getCompaniesLogos () {
      for (let o in this.job_offers) {
        let offer = this.job_offers[o]
        this.companies_logos[offer.company] = null
        firebase.storage().ref(`images/${offer.company}/avatar`).getDownloadURL()
          .then((url) => {
            this.companies_logos[offer.company] = url
            this.companies_logos[offer.company] = url
            console.log(url)
            this.$forceUpdate()
          })
          .catch(() => {
            console.log('This avatar does not exist')
          })
      }
      this.$forceUpdate()
    },
    onSubmitNewOffer () {
      const path = Vue.prototype.$API_BASE_URL + 'job_offer/' + this.username
      var values = {
        job_name: this.jobOfferForm.jobName,
        description: this.jobOfferForm.description,
        location: this.jobOfferForm.location
      }
      if (this.jobOfferForm.contractType !== '' && this.jobOfferForm.contractType !== null) {
        values.contract_type = this.jobOfferForm.contractType
      }
      if (this.jobOfferForm.salary !== '' && this.jobOfferForm.salary !== null) {
        values.salary = this.jobOfferForm.salary
      }
      if (!isNaN(this.jobOfferForm.workingHours) && this.jobOfferForm.workingHours !== '') {
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
.companyNameJobOfferCard{
  font-family: "Work Sans SemiBold", Montserrat, sans-serif;
  font-size: 18px;
  margin-bottom: 0.3rem;
}
.titleJobOfferCard{
  font-family: "Work Sans SemiBold", Montserrat, sans-serif;
  font-weight: bold;
  font-size: 24px;
  margin-bottom: 0;
}
</style>
