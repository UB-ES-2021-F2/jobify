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
          <b-nav-item active>Job postings</b-nav-item>
          <b-nav-item @click="onCompanies()">Companies</b-nav-item>
          <b-nav-item @click="onAboutUs()">About Us</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="!logged" class="ml-auto">
          <b-nav-item @click="onLogIn()">Log in</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="logged" class="ml-auto">
          <b-nav-item @click="onProfile()">{{ this.username }}</b-nav-item>
          <button class="btn btn-outline-danger" @click="onLogOut()"> Log Out </button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <!--/.Navbar -->

    <h2 style="font-family: 'Vollkorn"> {{ message }} </h2>
    <b-container fluid>
      <b-row align-h="center" v-if="is_company">
        <b-card
          tag="article"
          class="text-center mb-2"
          style="width: 90%; max-width: 600px"
        >
          <b-link v-b-modal.job-offer-modal style="position: absolute; top:0; left:0; height: 100%; width:100%"></b-link>
          <p class="h1"><b-icon icon="patch-plus"></b-icon></p>
        </b-card>
      </b-row>
      <b-row align-h="center" v-for="(job_offer) in job_offers" :key="job_offer.id">
        <b-card
          :title="job_offer.job_name"
          tag="article"
          class="mb-2"
          style="width: 90%; max-width: 600px"
          align="left"
        >
          <b-button class="btn btn-outline-light active" @click="onJobOffer(job_offer.id)" style="background-color:transparent; position: absolute; top:0; left:0; height: 100%; width:100%"></b-button>
          <b-card-text>
            {{ job_offer.company }}
          </b-card-text>
          <footer>
            <b-container fluid>
              <b-row>
                <b-col>
                  <b-icon icon="briefcase"></b-icon> {{ job_offer.contract_type }}
                </b-col>
                <b-col>
                  <b-icon icon="alarm"></b-icon> {{ job_offer.working_hours }}
                </b-col>
                <b-col>
                  <b-icon icon="calendar3-event"></b-icon> {{ job_offer.publication_date }}
                </b-col>
                <b-col>
                  <b-icon icon="geo-alt-fill"></b-icon> {{ job_offer.location }}
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
        <b-form style="font-family:'Work Sans'" @submit.prevent="handleSubmit(onSubmit)">
          <validation-provider name="JobName"  :rules="{alpha_spaces, required: true, max: 40}" v-slot="validationContext">
            <b-form-group id="input-group-1" label="Job name" label-for="input-1">
              <b-form-input v-model="jobOfferForm.jobName" placeholder="" type="text" :state="getValidationState(validationContext)"
                            aria-describedby="input-1-live-feedback"></b-form-input>
              <b-form-invalid-feedback id="input-1-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
            </b-form-group>
          </validation-provider>

          <validation-provider name="Description"  :rules="{ max: 500}" v-slot="validationContext">
            <b-form-group id="input-group-2" label="Description" label-for="input-2">
              <b-form-input v-model="jobOfferForm.description" placeholder="" type="text" :state="getValidationState(validationContext)"
                            aria-describedby="input-2-live-feedback"></b-form-input>
              <b-form-invalid-feedback id="input-2-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
            </b-form-group>
          </validation-provider>

          <validation-provider name="Salary"  :rules="{numeric, max: 10}" v-slot="validationContext">
            <b-form-group id="input-group-3" label="Salary" label-for="input-3">
              <b-form-input v-model="jobOfferForm.salary" placeholder="" type="number" :state="getValidationState(validationContext)"
                            aria-describedby="input-3-live-feedback"></b-form-input>
              <b-form-invalid-feedback id="input-3-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
            </b-form-group>
          </validation-provider>

          <validation-provider name="VacancyNumber"  :rules="{numeric, max: 3}" v-slot="validationContext">
            <b-form-group id="input-group-4" label="Vacancy number" label-for="input-4">
              <b-form-input v-model="jobOfferForm.vacancyNumber" placeholder="" type="number" :state="getValidationState(validationContext)"
                            aria-describedby="input-4-live-feedback"></b-form-input>
              <b-form-invalid-feedback id="input-4-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
            </b-form-group>
          </validation-provider>

          <validation-provider name="Location"  :rules="{alpha_spaces, required: true, max: 40}" v-slot="validationContext">
            <b-form-group id="input-group-1" label="Location" label-for="input-1">
              <b-form-input v-model="jobOfferForm.location" placeholder="" type="text" :state="getValidationState(validationContext)"
                            aria-describedby="input-1-live-feedback"></b-form-input>
              <b-form-invalid-feedback id="input-1-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
            </b-form-group>
          </validation-provider>

          <validation-provider name="ContractType"  :rules="{ max: 500}" v-slot="validationContext">
            <b-form-group id="input-group-2" label="Contract type" label-for="input-2">
              <b-form-input v-model="jobOfferForm.contractType" placeholder="" type="text" :state="getValidationState(validationContext)"
                            aria-describedby="input-2-live-feedback"></b-form-input>
              <b-form-invalid-feedback id="input-2-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
            </b-form-group>
          </validation-provider>

          <validation-provider name="WorkingHours"  :rules="{numeric, max: 10}" v-slot="validationContext">
            <b-form-group id="input-group-3" label="Working hours" label-for="input-3">
              <b-form-input v-model="jobOfferForm.workingHours" placeholder="" type="number" :state="getValidationState(validationContext)"
                            aria-describedby="input-3-live-feedback"></b-form-input>
              <b-form-invalid-feedback id="input-3-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
            </b-form-group>
          </validation-provider>

          <validation-provider name="MinimumExperience"  :rules="{numeric, required: true, max: 300}" v-slot="validationContext">
            <b-form-group id="input-group-4" label="Minimum experience" label-for="input-4">
              <b-form-input v-model="jobOfferForm.minimumExperience" placeholder="" type="number" :state="getValidationState(validationContext)"
                            aria-describedby="input-4-live-feedback"></b-form-input>
              <b-form-invalid-feedback id="input-4-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
            </b-form-group>
          </validation-provider>

          <div class="d-grid gap-2 d-md-flex justify-content-md-end">
            <button class="btn btn-warning justify-content-md-end">Post Job Offer!</button>
          </div>
        </b-form>
      </validation-observer>
    </b-modal>
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
      jobOfferForm: {
        jobName: '',
        description: '',
        salary: '',
        vacancyNumber: '',
        location: '',
        contractType: '',
        workingHours: '',
        minimumExperience: ''
      }
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
    onAboutUs () {
      this.$router.replace({ path: '/about_us' })
    },
    onJobOffer (id) {
      console.log(id)
    },
    getJobOffers () {
      const path = Vue.prototype.$API_BASE_URL + 'offers'
      axios.get(path)
        .then((res) => {
          this.job_offers = res.data.OfferList
          console.log(this.offers)
        })
        .catch((error) => {
          console.error(error)
        })
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
    onSubmit () {
      const path = Vue.prototype.$API_BASE_URL + 'job_offer/' + this.username
      const values = {
        job_name: this.jobOfferForm.jobName,
        description: this.jobOfferForm.description,
        salary: this.jobOfferForm.salary,
        vacancy_number: this.jobOfferForm.vacancyNumber,
        location: this.jobOfferForm.location,
        contract_type: this.jobOfferForm.contractType,
        working_hours: this.jobOfferForm.workingHours,
        minimum_experience: this.jobOfferForm.minimumExperience
      }
      axios.post(path, values)
        .then((res) => {
          console.log('Job Offer correctly posted')
        })
        .catch((error) => {
          alert(error.response.data.message)
        })
      this.onReset()
      this.$bvModal.hide('job-offer-modal')
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
