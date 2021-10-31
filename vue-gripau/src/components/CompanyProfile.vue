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
          <!-- Job Offers page -->
          <div v-show="this.profileView === false && this.jobView === true">
            <h2 style="font-family: 'Vollkorn', serif"> Job Offers </h2>
            <b-container fluid>
              <b-row align-h="center" v-if="edit_mode">
                <b-card
                  tag="article"
                  class="text-center mb-2"
                  style="width: 90%; max-width: 600px"
                >
                  <b-link v-b-modal.job-offer-modal style="position: absolute; top:0; left:0; height: 100%; width:100%"></b-link>
                  <p class="h1" style="margin:0 auto"><b-icon icon="patch-plus"></b-icon></p>
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
                        <b-col cols="4" v-if="job_offer.contract_type.length > 0">
                          <b-icon icon="briefcase"></b-icon> {{job_offer.contract_type}}
                        </b-col>
                        <b-col cols="2" v-if="job_offer.workingHours > 0">
                          <b-icon icon="alarm"></b-icon> {{job_offer.working_hours}} h
                        </b-col>
                        <b-col cols="3">
                          <b-icon icon="calendar3-event"></b-icon> {{ job_offer.publication_date }}
                        </b-col>
                        <b-col cols="3">
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
                <b-form style="font-family:'Work Sans'" @submit.prevent="handleSubmit(onSubmitNewOffer)">
                  <ValidationProvider name="JobName"  rules="alpha_spaces|required:true|max: 40" v-slot="validationContext">
                    <b-form-group id="input-group-1" label="Job name" label-for="input-1">
                      <b-form-input v-model="jobOfferForm.jobName" placeholder="" type="text" :state="getValidationState(validationContext)"
                                    aria-describedby="input-1-live-feedback"></b-form-input>
                      <b-form-invalid-feedback id="input-1-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
                    </b-form-group>
                  </ValidationProvider>

                  <validation-provider name="Description"  :rules="{ max: 500}" v-slot="validationContext">
                    <b-form-group id="input-group-2" label="Description" label-for="input-2">
                      <b-form-input v-model="jobOfferForm.description" placeholder="" type="text" :state="getValidationState(validationContext)"
                                    aria-describedby="input-2-live-feedback"></b-form-input>
                      <b-form-invalid-feedback id="input-2-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
                    </b-form-group>
                  </validation-provider>

                  <validation-provider name="Salary"  rules="numeric|max:10" v-slot="validationContext">
                    <b-form-group id="input-group-3" label="Salary" label-for="input-3">
                      <b-form-input v-model="jobOfferForm.salary" placeholder="" type="number" :state="getValidationState(validationContext)"
                                    aria-describedby="input-3-live-feedback"></b-form-input>
                      <b-form-invalid-feedback id="input-3-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
                    </b-form-group>
                  </validation-provider>

                  <validation-provider name="VacancyNumber"  rules="numeric|max:3" v-slot="validationContext">
                    <b-form-group id="input-group-4" label="Vacancy number" label-for="input-4">
                      <b-form-input v-model="jobOfferForm.vacancyNumber" placeholder="" type="number" :state="getValidationState(validationContext)"
                                    aria-describedby="input-4-live-feedback"></b-form-input>
                      <b-form-invalid-feedback id="input-4-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
                    </b-form-group>
                  </validation-provider>

                  <validation-provider name="Location"  rules="alpha_spaces|required:true|max: 40" v-slot="validationContext">
                    <b-form-group id="input-group-1" label="Location" label-for="input-1">
                      <b-form-input v-model="jobOfferForm.location" placeholder="" type="text" :state="getValidationState(validationContext)"
                                    aria-describedby="input-1-live-feedback"></b-form-input>
                      <b-form-invalid-feedback id="input-1-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
                    </b-form-group>
                  </validation-provider>

                  <validation-provider name="ContractType"  :rules="{ max: 500}" v-slot="validationContext">
                    <b-form-group id="input-group-2" label="Contract type" label-for="input-2">
                      <b-form-select v-model="jobOfferForm.contractType" :options="optionsContractType" placeholder="" type="text" :state="getValidationState(validationContext)"
                                     aria-describedby="input-2-live-feedback"></b-form-select>
                      <b-form-invalid-feedback id="input-2-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
                    </b-form-group>
                  </validation-provider>

                  <validation-provider name="WorkingHours"  rules="numeric|max:10" v-slot="validationContext">
                    <b-form-group id="input-group-3" label="Working hours" label-for="input-3">
                      <b-form-input v-model="jobOfferForm.workingHours" placeholder="" type="number" :state="getValidationState(validationContext)"
                                    aria-describedby="input-3-live-feedback"></b-form-input>
                      <b-form-invalid-feedback id="input-3-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
                    </b-form-group>
                  </validation-provider>

                  <validation-provider name="MinimumExperience"  rules="numeric|required:true|max:300" v-slot="validationContext">
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
          <!-- /Job Offers page -->
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
      bio: 'Add your bio here',
      job_offers: [],
      jobOfferForm: {
        jobName: '',
        description: '',
        salary: '',
        vacancyNumber: '',
        location: '',
        contractType: '',
        workingHours: '',
        minimumExperience: ''
      },
      optionsContractType: ['Indefinite', 'Fixed-term', 'Zero Hours', 'Internship', 'Self-employment', 'Apprentice']
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
      axios.put(pathCompany, values)
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
    },
    getCompanyJobOffers () {
      const path = Vue.prototype.$API_BASE_URL + 'offers/' + this.company_name_profile.toLowerCase()
      axios.get(path)
        .then((res) => {
          console.log(res.data)
          this.job_offers = []
          for (var jobOffer in res.data) {
            jobOffer = res.data[jobOffer]
            jobOffer.publication_date = jobOffer.publication_date.split('T')[0]
            this.job_offers.push(jobOffer)
          }
        })
        .catch((error) => {
          console.error(error)
        })
    },
    getValidationState ({ dirty, validated, valid = null }) {
      return dirty || validated ? valid : null
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
      if (!isNaN(this.jobOfferForm.vacancyNumber)) {
        values.salary = this.jobOfferForm.vacancyNumber
      }
      if (!isNaN(this.jobOfferForm.workingHours)) {
        values.salary = this.jobOfferForm.workingHours
      }
      if (!isNaN(this.jobOfferForm.minimumExperience)) {
        values.salary = this.jobOfferForm.minimumExperience
      }
      console.log(values)
      axios.post(path, values)
        .then((res) => {
          console.log('Job Offer correctly posted')
          this.getCompanyJobOffers()
        })
        .catch((error) => {
          alert(error.response.data.message)
        })
      this.$bvModal.hide('job-offer-modal')
      this.onReset()
    },
    onReset () {
      this.initJobOfferForm()
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
    this.getCompanyJobOffers()
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
