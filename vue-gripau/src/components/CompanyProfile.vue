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

    <b-container fluid>
      <b-row align-v="stretch">
        <!-- Local Navbar -->
        <b-col style="background-color: #00000007" cols="">
          <b-nav sticky toggleable="false" type="light" variant="light" vertical>
            <b-navbar-brand style="text-align: center;width: 100%;" >
              <div >
                <h2 id="companyNameNavbar" style="font-family: 'Vollkorn', serif; text-align:center">{{company.company}}</h2>
                <b-icon icon="building"></b-icon>
              </div>
            </b-navbar-brand>
            <b-nav-item active id="activeProfileViewButton" style="text-decoration: underline; text-decoration-thickness:5px; text-decoration-color: #ffc107; text-align: center; width: 100%" v-if="this.profileView" @click="onProfileView()">Profile</b-nav-item>
            <b-nav-item v-else id="profileViewButton" style="text-align: center; width: 100%" @click="onProfileView()">Profile</b-nav-item>
            <b-nav-item active id="activeJobViewButton" class="active" style="text-decoration: underline; text-decoration-thickness:5px; text-decoration-color: #ffc107; text-align: center; width: 100%" v-if="this.jobView" @click="onJobView()">Jobs</b-nav-item>
            <b-nav-item v-else id="jobViewButton" style="text-align: center; width: 100%" @click="onJobView()">Jobs</b-nav-item>
          </b-nav>
        </b-col>
        <!--/.Local Navbar -->
        <b-col fluid lg="10" cols="12">
          <div id="profileView" v-if="this.profileView && !this.jobView">
            <div class="row">
              <div class="row d-flex d-lg-block">
                <div id="divAvatar" class="col-lg-4 order-1 float-left align-items-center">
                  <div v-if="downloadImage != null" id="firebase-avatar">
                    <img class="rounded" style="width:200px;height:200px" :src="downloadImage" alt="">
                  </div>
                  <div v-else id="default-avatar">
                    <img class="rounded" style="width:200px;height:200px" :src="require('../assets/images/company_avatar.png')" alt="">
                  </div>
                  <div id="avatar-edit" v-if="edit_mode" class="container-md-5 p-2 align-items-center">
                    <b-form-group id="fileInput">
                      <b-form-file center
                                   v-model="file"
                                   :state="Boolean(file)"
                                   placeholder="Choose or drop a file"
                                   drop-placeholder="Drop file here..."
                                   accept="image/jpeg, image/png, image/gif"
                      ></b-form-file>
                    </b-form-group>
                    <div class="container-md-5 p-2 align-items-center" v-if="file">
                      <img :src="previewSrc" height='128'>
                      <br>
                      <br>
                      <b-progress :value="uploadValue" :max="100" class="mb-3"></b-progress>
                      <br>
                    </div>
                    <b-button variant="success" :disabled="!file" @click="onUpload">Upload</b-button>
                  </div>
                </div>
                <div id="divName" class="col-lg-8 text-left order-0 float-left">
                  <p class="page-title">
                    {{company.company}} profile
                  </p>
                </div>
                <div id="divBio" class="col-lg-8 text-left order-1 float-left">
                  <!-- company description -->
                  <div id="descriptionCompany1" v-if="company.description != null && company.description !== '' && !edit.description " class="bio-text">
                    {{company.description}}
                    <p></p>
                  </div>
                  <div id="descriptionCompany2" v-if="(company.description === null || company.description === '') && !edit.description && edit_mode" class="bio-text">
                    <p>Write about your company!</p>
                  </div>
                  <b-container id="editDescriptionField" v-if="edit.description" fluid>
                    <b-row align="center">
                      <b-col sm="10">
                        <b-form-textarea id="descriptionInput" v-model="modify.description" rows="3" max-rows="8"/>
                      </b-col>
                      <b-col align-self="center" sm="1">
                        <b-button id="submitEditDescriptionButton" variant="success" @click="modifyDescription()">Save</b-button>
                      </b-col>
                    </b-row>
                    <p></p>
                  </b-container>
                  <button id="enableEditDescriptionButton" v-if="edit_mode" class="btn btn-sm" style="margin-bottom: 5px; margin-left: 20px" @click="editDescription()" ><b-icon-pencil-fill font-scale="1.5" shift-v="-2"></b-icon-pencil-fill></button>
                  <!-- /company description -->
                </div>
              </div>
            </div>
            <div class="row d-flex d-lg-block p-2 align-items-center">
              <!-- company email -->
              <b-row no-gutters>
                <div v-if="(company.email !== 'Unknown' && company.email) || edit_mode " class="text-left p-2 pb-3" style="max-width: 50rem">
                  <h3 style="font-family: 'Vollkorn', serif"> Email</h3>
                  <div id="emailCompany" v-if="!edit.email">
                    <p>{{company.email}}</p>
                  </div>
                  <b-container v-if="edit.email" fluid>
                    <validation-provider name="Company email"  :rules="{email, required: true, max: 128}" v-slot="validationContext">
                      <b-row align="left">
                        <b-col sm="5">
                          <b-form-input id="emailInput" v-model="modify.email" rows="1" max-rows="2" type="email" :state="getValidationState(validationContext)"
                                        aria-describedby="input-2c-live-feedback"/>
                          <b-form-invalid-feedback id="input-2c-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
                        </b-col>
                        <b-col align-self="center" sm="1">
                          <b-button id="submitEditEmailButton" :disabled="!validationContext.valid" variant="success" @click="modifyEmail()">Save</b-button>
                        </b-col>
                      </b-row>
                      <p></p>
                    </validation-provider>
                  </b-container>
                  <button id="enableEditEmailButton" v-if="edit_mode" class="btn btn-sm" style="margin-bottom: 5px; margin-left: 20px" @click="editEmail()" ><b-icon-pencil-fill font-scale="1.5" shift-v="-1"></b-icon-pencil-fill></button>
                </div>
              </b-row>
              <!-- /company email -->
              <!-- company sector -->
              <b-row no-gutters>
                <div v-if="(company.sector !== 'Unknown' && company.sector) || edit_mode " class="text-left p-2 pb-3" style="max-width: 50rem">
                  <h3 style="font-family: 'Vollkorn', serif"> Sector</h3>
                  <div id="sectorCompany" v-if="!edit.sector">
                    <p>{{company.sector}}</p>
                  </div>
                  <b-container id="editSectorField" v-if="edit.sector" fluid>
                    <b-row align="left">
                      <b-col sm="5">
                        <b-form-textarea id="sectorInput" v-model="modify.sector" rows="1" max-rows="2"/>
                      </b-col>
                      <b-col align-self="center" sm="1">
                        <b-button id="submitEditSectorButton" variant="success" @click="modifySector()">Save</b-button>
                      </b-col>
                    </b-row>
                    <p></p>
                  </b-container>
                  <button id="enableEditSectorButton" v-if="edit_mode" class="btn btn-sm" style="margin-bottom: 5px; margin-left: 20px" @click="editSector()" ><b-icon-pencil-fill font-scale="1.5" shift-v="-2"></b-icon-pencil-fill></button>
                </div>
              </b-row>
              <!-- /company sector -->
              <!-- company location -->
              <b-row no-gutters>
                <div v-if="(company.location !== 'Unknown' && company.location) || edit_mode " class="text-left p-2 pb-3" style="max-width: 50rem">
                <h3 style="font-family: 'Vollkorn', serif"> Location</h3>
                <div id="locationCompany" v-if="!edit.location">
                  <p>{{company.location}}</p>
                </div>
                <b-container id="editLocationField" v-if="edit.location" fluid>
                  <b-row align="left">
                    <b-col sm="5">
                      <b-form-textarea id="locationInput" v-model="modify.location" rows="1" max-rows="2"/>
                    </b-col>
                    <b-col align-self="center" sm="1">
                      <b-button id="submitEditLocationButton" variant="success" @click="modifyLocation()">Save</b-button>
                    </b-col>
                  </b-row>
                  <p></p>
                </b-container>
                <button id="enableEditLocationButton" v-if="edit_mode" class="btn btn-sm" style="margin-bottom: 5px; margin-left: 20px" @click="editLocation()" ><b-icon-pencil-fill font-scale="1.5" shift-v="-2"></b-icon-pencil-fill></button>
              </div>
              </b-row>
              <!-- /company location -->
            </div>

          </div>
          <!-- Job Offers page -->
          <div id="jobView" v-if="this.profileView === false && this.jobView === true">
            <!-- Job offers company view -->
            <div id="jobOffersCompanyView" v-if="!this.jobOfferView">
              <h2 style="font-family: 'Vollkorn', serif"> Job Offers </h2>
              <b-container fluid>
                <b-row align-h="center" v-if="edit_mode">
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
                      {{ job_offer.company_name }}
                    </b-card-text>
                    <footer>
                      <b-container fluid style="font-family: 'Work Sans'">
                        <b-row no-gutters>
                          <b-col lg v-if="job_offer.contract_type.length > 0">
                            <b-icon id="contractTypeIcon" icon="briefcase"></b-icon> {{job_offer.contract_type}}
                          </b-col>
                          <b-col lg v-if="job_offer.workingHours > 0">
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

                    <validation-provider name="ContractType"  :rules="{ max: 500, required:true}" v-slot="validationContext">
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
            <!-- /Job offers company view -->
            <!-- Job offer view -->
            <div id="jobOfferCompanyView" v-if="this.jobOfferView">
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
              <b-button id="seenButton" btn variant="warning" class='btn-home' @click="onJoOfferView">Seen</b-button>
              <b-button id="deleteButton" v-if="this.is_company" btn variant="danger" class='m-2' @click="deleteJobOffer()">Delete Job Offer</b-button>
              <b-button v-if="!applied && is_jobseeker && logged" v-b-modal.modal-apply variant="success">Apply</b-button>
              <b-button v-if="applied && is_jobseeker && logged " @click="applyAction" variant="outline-success">Applied</b-button>
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
            <!-- /Job offer view -->
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
      profileView: true,
      jobView: false,
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
            this.applied = !this.applied
          })
          .catch((error) => {
            alert(error.response.data.message)
          })
      } else {
        const path = Vue.prototype.$API_BASE_URL + 'delete_application/' + this.username
        const values = {
          id: this.jobOfferCurrentView.id
        }
        axios.post(path, values, {
          auth: {username: this.token}})
          .then((res) => {
            console.log('Apply job offer correct deleted')
            this.applied = !this.applied
          })
          .catch((error) => {
            alert(error.response.data.message)
          })
      }
    },
    resetApplyModal () {
      this.applyMessage = null
    },
    onJoOfferView () {
      this.jobOfferView = !this.jobOfferView
    },
    onProfile () {
      if (this.is_jobseeker && this.logged) {
        this.$router.replace({ path: '/job_seeker/' + this.username })
      } else if (this.is_company && this.logged) {
        this.$router.replace({path: '/company/' + this.username})
      }
    },
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
    onJobView () {
      this.profileView = false
      this.jobView = true
      this.edit.description = false
      this.edit.sector = false
      this.edit.location = false
      this.jobOfferView = false
    },
    onJobOfferView () {
      this.jobOfferView = !this.jobOfferView
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
        location: this.jobOfferForm.location,
        contract_type: this.jobOfferForm.contractType
      }
      if (this.jobOfferForm.salary !== '') {
        values.salary = this.jobOfferForm.salary
      }
      if (this.jobOfferForm.workingHours !== '') {
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
    downloadAvatar () {
      firebase.storage().ref(`images/${this.company_name_profile}/avatar`).getDownloadURL()
        .then((url) => {
          this.downloadImage = url
          console.log(url)
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
    this.jobView = false
    this.profileView = true
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
