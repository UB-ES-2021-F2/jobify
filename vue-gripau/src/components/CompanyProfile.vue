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

          <b-nav-item id="companiesNavbarButton" v-if="this.username===this.company_name_profile" @click="onCompanies()">Companies</b-nav-item>
          <b-nav-item id="companiesNavbarButtonIfWatchingCompany" v-else active @click="onCompanies()">Companies</b-nav-item>
          <b-nav-item id="aboutUsNavbarButton" @click="onAboutUs()">About Us</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="!logged" class="ml-auto">
          <b-nav-item id="logInNavbarButton" @click="onLogIn()">Log in</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="logged" class="ml-auto">
          <b-nav-item id="activeProfileNavbarButton" active v-if="this.username===this.company_name_profile">{{ this.username }}</b-nav-item>
          <b-nav-item id="profileNavbarButton" @click="onProfile()" v-else>{{ this.username }}</b-nav-item>
          <button id="logOutNavbarButton" class="btn btn-outline-danger" @click="onLogOut()"> Log Out </button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <!--/.Navbar -->

    <b-container>
      <b-row>
        <b-col cols="12">
          <div id="profileView" v-if="!this.jobOfferView">
            <div class="row">
              <div id="divAvatar" class="col-12 col-sm-12 col-md-6 col-lg-3">
                <div v-if="downloadImage != null" id="firebase-avatar">
                  <img :src="downloadImage" alt="">
                </div>
                <div v-else-if="file">
                  <img :src="previewSrc" alt="">
                </div>
                <div v-else id="default-avatar">
                  <img :src="require('../assets/images/company_avatar.png')" alt="" style="opacity: 0.3">
                </div>
                <div id="avatar-edit" v-if="edit_mode" class="container-md-5 p-2 browser-container">
                  <b-form-group id="fileInput">
                    <b-form-file center
                                 v-model="file"
                                 :state="Boolean(file)"
                                 placeholder="Choose a file"
                                 drop-placeholder="Drop file here..."
                                 accept="image/jpeg, image/png, image/gif"
                    ></b-form-file>
                  </b-form-group>
                  <b-button v-if="file" class="big-button" variant="success" :disabled="!file" @click="onUpload">
                    Upload  <b-icon-upload font-scale="1" shift-v="-2"></b-icon-upload>
                  </b-button>
                </div>
                <div id="nameCompany" class="name-profile">
                  {{company.company}} <!--Amazon Inc.-->
                </div>
              </div>
              <div id="divName" class="col-12 col-sm-12 col-md-6 col-lg-4">
                <div class="content-table">
                  <div class="content-table-cell">
                    <!-- company email -->
                    <div no-gutters>
                      <div v-if="(company.email !== 'Unknown' && company.email) || edit_mode " class="company-info" style="max-width: 50rem">
                        <span>
                          <b-icon id="emailIcon" icon="envelope-fill"></b-icon>
                        </span>
                        <div class="text-edit" id="emailCompany" v-if="!edit.email">
                          <span>{{company.email}}</span> <!-- amazon@amazon.com -->
                        </div>
                        <div id="editEmailField" v-if="edit.email" class="text-edit">
                          <validation-provider name="Company email"  :rules="{email, required: true, max: 128}" v-slot="validationContext">
                            <b-form-input id="emailInput" v-model="modify.email" rows="1" max-rows="2" type="email" :state="getValidationState(validationContext)"
                                          aria-describedby="input-2c-live-feedback"/>
                            <b-form-invalid-feedback id="input-2c-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
                            <b-button class="save-button" id="submitEditEmailButton" :disabled="!validationContext.valid" variant="success" @click="modifyEmail()">
                              <b-icon icon="check-circle" font-scale="1.5"></b-icon>
                            </b-button>
                            <p></p>
                          </validation-provider>
                        </div>
                        <button id="enableEditEmailButton" v-if="edit_mode" class="btn btn-sm edit-button" @click="editEmail()" ><b-icon-pencil-fill font-scale="1.5" shift-v="-1"></b-icon-pencil-fill></button>
                      </div>
                    </div>
                    <!-- /company email -->
                    <!-- company sector -->
                    <div no-gutters>
                      <div v-if="(company.sector !== 'Unknown' && company.sector) || edit_mode " class="company-info" style="max-width: 50rem">
                        <span>
                          <b-icon id="sectorIcon" icon="inboxes-fill"></b-icon>
                        </span>
                        <div class="text-edit" id="sectorCompany" v-if="!edit.sector">

                          <span>{{company.sector}}</span> <!-- Computer Sience -->
                        </div>
                        <div id="editSectorField" class="text-edit" v-if="edit.sector" fluid>
                          <!--<div class="save-input">-->
                            <b-form-input id="sectorInput" v-model="modify.sector" rows="1" max-rows="1"/>
                          <!--</div>-->
                          <div class="save-button">
                            <b-button id="submitEditSectorButton" variant="success" @click="modifySector()">
                              <b-icon icon="check-circle" font-scale="1.5"></b-icon>
                            </b-button>
                          </div>
                          <p></p>
                        </div>
                        <button id="enableEditSectorButton" v-if="edit_mode" class="btn btn-sm edit-button" @click="editSector()" ><b-icon-pencil-fill font-scale="1.5" shift-v="-2"></b-icon-pencil-fill></button>
                      </div>
                    </div>
                    <!-- /company sector -->
                    <!-- company location -->
                    <div no-gutters>
                      <div v-if="(company.location !== 'Unknown' && company.location) || edit_mode " class="company-info" style="max-width: 50rem">
                        <span>
                          <b-icon id="locationIcon" icon="geo-alt-fill"></b-icon>
                        </span>
                        <div class="text-edit" id="locationCompany" v-if="!edit.location">
                          <span>{{company.location}}</span> <!-- California, CA. Cupertino -->
                        </div>
                        <div id="editLocationField" class="text-edit" v-if="edit.location">
                          <b-form-input id="locationInput" v-model="modify.location" rows="1" max-rows="1"/>
                          <b-button class="save-button" id="submitEditLocationButton" variant="success" @click="modifyLocation()">
                            <b-icon icon="check-circle" font-scale="1.5"></b-icon>
                          </b-button>
                          <p></p>
                        </div>
                        <button id="enableEditLocationButton" v-if="edit_mode" class="btn btn-sm edit-button" @click="editLocation()" >
                          <b-icon-pencil-fill font-scale="1.5" shift-v="-2"></b-icon-pencil-fill>
                        </button>
                      </div>
                    </div>
                    <!-- /company location -->
                  </div>
                </div>

              </div>
              <div id="divBio" class="col-12 col-sm-12 col-md-12 col-lg-5">
                <!-- company description -->
                <div id="descriptionCompany1" v-if="company.description != null && company.description !== '' && !edit.description " class="bio-text">
                  {{company.description}}
                  <div class="description-text">
                    <!--Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.-->
                  </div>
                </div>
                <div id="descriptionCompany2" v-if="(company.description === null || company.description === '') && !edit.description && edit_mode" class="bio-text">
                  <p>Write about your company!</p>
                </div>
                <div id="editDescriptionField" v-if="edit.description" fluid>
                  <b-form-textarea id="descriptionInput" v-model="modify.description" rows="3" max-rows="8"/>
                  <b-button class="save-button" id="submitEditDescriptionButton" variant="success" @click="modifyDescription()">
                    <b-icon icon="check-circle" font-scale="1.5"></b-icon>
                  </b-button>
                  <p></p>
                </div>
                <button id="enableEditDescriptionButton" v-if="edit_mode" class="btn btn-sm edit-button" @click="editDescription()" >
                  <b-icon-pencil-fill font-scale="1.5" shift-v="-2"></b-icon-pencil-fill>
                </button>
                <!-- /company description -->
              </div>
            </div>
            <div class="row d-flex d-lg-block p-2 align-items-center">
            </div>

          </div>
          <!-- Job Offers page -->
          <div id="jobView">
            <!-- Job offers company view -->
            <div id="jobOffersCompanyView" v-if="!this.jobOfferView">
              <h2 class="title-offer"> Job Offers </h2>
              <b-link v-if="edit_mode" id="showJobOfferModal" class="add-offer" v-b-modal.job-offer-modal>
                <b-icon icon="patch-plus" font-scale="2"></b-icon>
              </b-link>
              <div class="container">
                <div class="row" align-h="center">
                  <!--<div class="col-6">
                    <b-card tag="article" class="text-center mb-2" id="addJobOfferCard">

                      <p class="h1"></p>
                    </b-card>
                  </div>-->
                  <b-container>
                    <job-offer-view
                      v-bind:job_offers = "job_offers"
                      v-bind:show_company = false
                    ></job-offer-view>
                  </b-container>
                </div>
              </div>
              <b-modal ref="jobOfferModal"
                       id="job-offer-modal"
                       title="Post a job offer"
                       hide-footer
              >
                <validation-observer ref="observer" v-slot="{ handleSubmit }">
                  <b-form style="font-family:'Work Sans'" @submit.prevent="handleSubmit(onSubmitNewOffer)">
                    <ValidationProvider name="JobName"  rules="alpha_spaces|required:true|max: 50" v-slot="validationContext">
                      <b-form-group id="input-group-1" label="Job name" label-for="input-1">
                        <b-form-input id="jobNameInput" v-model="jobOfferForm.jobName" placeholder="e.g. Product Owner" type="text" :state="getValidationState(validationContext)"
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
                        <b-form-select id="contractTypeInput" v-model="jobOfferForm.contractType" :options="optionsContractType"  type="text" :state="getValidationState(validationContext)"
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
import firebase from 'firebase/compat/app'
import 'firebase/compat/storage'

export default {
  data () {
    return {
      edit: {
        description: false,
        sector: false,
        email: false,
        location: false
      },
      modify: {
        description: '',
        sector: '',
        email: '',
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
      jobOfferView: false,
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
      optionsContractType: ['Indefinite', 'Fixed-term', 'Zero Hours', 'Internship', 'Self-employment', 'Apprentice'],
      file: null,
      uploadValue: 0,
      previewSrc: null,
      downloadImage: null,
      applied: false,
      applyMessage: null
    }
  },
  methods: {
    getApplied () {
      const path = Vue.prototype.$API_BASE_URL + 'application/' + this.username + '/' + this.jobOfferCurrentView.id
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
          job_offer_id: this.jobOfferCurrentView.id
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
    onProfile () {
      if (this.is_jobseeker && this.logged) {
        this.$router.replace({ path: '/job_seeker/' + this.username })
      } else if (this.is_company && this.logged) {
        this.$router.replace({path: '/company/' + this.username})
      }
    },
    onHome () {
      this.$router.push('/')
    },
    onLogIn () {
      this.$router.push('/login')
    },
    onCompanies () {
      this.$router.push('/companies')
    },
    onJobOfferView () {
      this.jobOfferView = true
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
    editEmail () {
      this.edit.email = !this.edit.email
      this.modify.email = this.company.email
    },
    getValidationStateEmail ({ dirty, validated, valid = null }) {
      return dirty || validated ? valid : null
    },

    modifyDescription () {
      const pathCompany = Vue.prototype.$API_BASE_URL + 'company/' + this.company_name_profile.toLowerCase()
      const values = {
        description: this.modify.description
      }
      axios.put(pathCompany, values, {
        auth: {username: this.token}})
        .then((res) => {
          console.log(this.modify.description)
          this.getCompany()
          this.edit.description = !this.edit.description
        })
        .catch((error) => {
          console.error(error)
          alert(' An error occurred modifying description')
        })
    },
    modifySector () {
      const pathCompany = Vue.prototype.$API_BASE_URL + 'company/' + this.company_name_profile.toLowerCase()
      const values = {
        sector: this.modify.sector
      }
      axios.put(pathCompany, values, {
        auth: {username: this.token}})
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
      axios.put(pathCompany, values, {
        auth: {username: this.token}})
        .then((res) => {
          this.getCompany()
          this.edit.location = !this.edit.location
        })
        .catch((error) => {
          console.error(error)
          alert(' An error occurred creating the account')
        })
    },
    modifyEmail () {
      const pathCompany = Vue.prototype.$API_BASE_URL + 'company/' + this.company_name_profile.toLowerCase()
      const values = {
        email: this.modify.email
      }
      axios.put(pathCompany, values, {
        auth: {username: this.token}})
        .then((res) => {
          this.getCompany()
          this.edit.email = !this.edit.email
        })
        .catch((error) => {
          console.error(error)
          alert(' An error occurred editing the email')
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
    getValidationState ({ dirty, validated, valid = null }) {
      return dirty || validated ? valid : null
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
          this.getCompanyJobOffers()
        })
        .catch((error) => {
          alert(error.response.data.message)
        })
      this.$bvModal.hide('job-offer-modal')
      this.onReset()
    },
    downloadAvatar () {
      firebase.storage().ref(`images/${this.company_name_profile}/avatar`).getDownloadURL()
        .then((url) => {
          this.downloadImage = url
          console.log(url)
        })
        .catch(() => {
          console.log('This avatar does not exist yet')
        })
    },
    onUpload () {
      const storageRef = firebase.storage().ref(`images/${this.company_name_profile}/avatar`).put(this.file)
      storageRef.on(`state_changed`, snapshot => {
        this.uploadValue = (snapshot.bytesTransferred / snapshot.totalBytes) * 100
      }, error => { console.log(error.message) }, () => {
        this.uploadValue = 100
        this.file = null
        storageRef.snapshot.ref.getDownloadURL().then((url) => {
          console.log('File uploaded to ' + url)
          this.downloadAvatar()
        })
      })
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
          console.log(this.jobOfferCurrentView)
          if (this.logged && this.is_jobseeker) {
            this.getApplied()
          }
          this.onJobOfferView()
        })
        .catch((error) => {
          console.error(error)
        })
    }
  },
  watch: {
    file (val) {
      if (!val) return
      const fileReader = new FileReader()
      fileReader.onload = (e) => { this.previewSrc = e.target.result }
      fileReader.readAsDataURL(this.file)
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
    this.downloadAvatar()
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
.page-title {
  font-family: "Vollkorn",serif;
  font-size: 30px;
  display:inline-block
}
</style>
