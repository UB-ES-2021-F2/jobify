<template>
  <div id="app">
    <!--Navbar -->
    <b-navbar sticky toggleable="lg" type="light" variant="light">
      <b-navbar-brand id="homeNavbar" href="#" @click="onHome()">
        <img id="logoNavbar" style="max-width: 150px" :src="require('../assets/logo.svg')">
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item id="homeNavbarButton" @click="onHome()">Home</b-nav-item>
          <b-nav-item id="jobPostingsNavbarButton" @click="onJobPostings()">Job postings</b-nav-item>
          <b-nav-item id="companiesNavbarButton" @click="onCompanies()">Companies</b-nav-item>
          <b-nav-item id="aboutUsNavbarButton" @click="onAboutUs()">About Us</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="!logged" class="ml-auto">
          <b-nav-item id="logInNavbarButton" @click="onLogIn()">Log in</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="logged" class="ml-auto">
          <b-nav-item active id="activeProfileNavbarButton" @click="onUserProfile()" v-if="this.username===this.username_profile">{{ this.username }}</b-nav-item>
          <b-nav-item id="profileNavbarButton" @click="onUserProfile()" v-else>{{ this.username }}</b-nav-item>
          <button id="logOutNavbarButton" class="btn btn-outline-danger" @click="onLogOut()"> Log Out </button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <!--/.Navbar -->

    <div class="container">
      <div class="row jobseeker-description-container">
        <div id="divAvatar" class="col-12 col-sm-12 col-md-6 col-lg-3">
          <div class="content-table">
            <div class="content-table-cell">
              <div v-if="downloadImage != null" id="firebase-avatar">
                <img :src="downloadImage" alt="">
              </div>
              <div v-else-if="file">
                <img :src="previewSrc" alt="">
              </div>
              <div v-else id="default-avatar">
                <img :src="require('../assets/images/avatar.png')" alt="">
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
            </div>
          </div>
      </div>
        <div id="divBio" class="col-12 col-sm-12 col-md-6 col-lg-6">
          <div id="divName" class=" jobseeker-name">
            <p id="nameSurnameFields" class="page-title">
              {{ name }} {{ surname }}
            </p>
          </div>
          <div id="bioField1" v-if="bio != null && bio !== '' && !edit_bio " class="bio-text">
            {{bio}}
            <p></p>
          </div>
          <div id="bioField2" v-if="(bio === null || bio === '') && !edit_bio && edit_mode" class="bio-text">
            Write about yourself!
          </div>
          <div id="editBioField" v-if="edit_bio">
            <validation-observer ref="observer" v-slot="{ handleSubmit }">
              <b-form style="font-family:'Work Sans'" @submit.prevent="handleSubmit(modifyBio)">
                <ValidationProvider name="bio"  rules="max: 1000" v-slot="validationContext">
                  <b-form-group id="input-group-1">
                    <b-form-textarea id="bioInput" v-model="modify_bio" placeholder="Write your bio here..." rows="4" :state="getValidationState(validationContext)"
                                  aria-describedby="input-1-live-feedback"></b-form-textarea>
                    <b-form-invalid-feedback id="input-1-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
                  </b-form-group>
                  <b-button v-if="edit_bio" class="save-button" id="submitEditBioButton" variant="success" type="submit">
                    <b-icon icon="check-circle" font-scale="1.5"></b-icon>
                  </b-button>
                </ValidationProvider>
              </b-form>
            </validation-observer>
          </div>
          <button id="enableEditBioButton" v-if="edit_mode" class="btn btn-sm edit-button" @click="editBio()" >
            <b-icon-pencil-fill font-scale="1.5" shift-v="-2"></b-icon-pencil-fill>
          </button>
        </div>
        <div id="divSkills" class="col-12 col-sm-12 col-md-12 col-lg-3">
          <p class="section-title"> Skills </p>
          <button id="addSkillButton" v-if="edit_mode" class="btn btn-sm add-skill" @click="onAddSkill()">
            <b-icon icon="patch-plus" font-scale="2"></b-icon>
          </button>
          <div class="skills-container">
            <div class="badge-container badge badge-pill badge-warning p-2 m-1" v-for="skill in skills" :key="skill">
              <span id="nameSkill">{{ skill }}</span>
              <b-button id="deleteSkillButton" pill size="sm" class="badge-button badge badge-pill badge-warning" @click="deleteSkill(skill)">X</b-button>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-12 col-sm-12 col-md-6">
          <div id="divEducation" class="text-left p-2 pb-3" style="max-width: 50rem">
            <p class="section-title"> Education </p>
            <button id="addEducationButton" v-if="edit_mode" class="btn btn-sm add-skill" @click="onAddEducation()">
              <b-icon icon="patch-plus" font-scale="2"></b-icon>
            </button>
            <div class="education-item" v-for="ed in education" :key="ed.id">
              <div class="row education-name">
                  <div class="col-6 education-title">
                    {{ed.title}}
                  </div>
                  <div class="col-6 delete-education">
                    <button id="deleteEducationButton" v-if="edit_mode" class="ml-auto btn btn-sm" @click="deleteEducation(ed)">
                      <b-icon icon="trash" font-scale="1"></b-icon>
                    </button>
                  </div>
                </div>
              <div class="row education-info-contanier">
                <div class="col-8">
                  <p id="institutionEducation" class="education-place">{{ed.institution}}</p>
                </div>
                <div class="col-4 education-time">
                  <b-icon icon="calendar-event" font-scale="1"></b-icon>
                  <p id="datesEducation" v-if="!ed.currently"><small class="text-muted">{{ed.start_date}} - {{ed.end_date}}</small></p>
                  <p id="datesCurrentlyEducation" v-if="ed.currently"><small class="text-muted">{{ed.start_date}} - now</small></p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-12 col-sm-12 col-md-6">
          <div id="divWorkExperience" class="text-left p-2 pb-3" style="max-width: 50rem">
            <p class="section-title"> Work experience </p>
            <button id="addWorkButton" v-if="edit_mode" class="btn btn-sm add-skill" @click="onAddWork()">
              <b-icon icon="patch-plus" font-scale="2"></b-icon>
            </button>
            <div class="work-item"  v-for="work in work_experience" :key="work.id">
              <div class="row work-name">
                <div class="col-6 work-title">
                  <span id="jobNameWorkExperience" class="card-title-work">{{work.job_name}}</span>
                </div>
                <div class="col-6 delete-work">
                  <button id="deleteWorkButton" v-if="edit_mode" class="ml-auto btn btn-sm" @click="deleteWork(work)">
                    <b-icon icon="trash" font-scale="1"></b-icon>
                  </button>
                </div>
              </div>
              <div class="row">
                <div class="col-8">
                  <p id="companyWorkExperience" class="work-place">{{work.company}}</p>
                </div>
                <div class="col-4 work-time">
                  <b-icon icon="calendar-event" font-scale="1"></b-icon>
                  <p id="datesWorkExperience" v-if="!work.currently"><small class="text-muted">{{work.start_date}} - {{work.end_date}}</small></p>
                  <p id="datesCurrentlyWorkExperience" v-if="work.currently"><small class="text-muted">{{work.start_date}} - now</small></p>
                </div>
                <div class="col-12">
                  <p id="descriptionWorkExperience" class="card-text">{{work.description}}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="row" v-if="edit_mode">
        <div class="col-12">
          <p class="section-title">My Applications</p>
          <b-table :fields="fields"    :items="this.jobs_applied">
            <template v-slot:cell(Company)="slot">
              <router-link :to="`/company/${slot.item.Username}`">{{slot.item.Company}}</router-link>
            </template>
            <template v-slot:cell(Offer)="slot">
              <router-link :to="`/job_posting/${slot.item.Reference}`">{{slot.item.Offer}}</router-link>
            </template>
          </b-table>
        </div>
      </div>

      <b-modal id="addWorkModal" hide-footer ref="addWorkModal">
        <template #modal-header><h5 style="font-family: 'Work Sans SemiBold'">Add work experience</h5></template>
        <validation-observer ref="observer" v-slot="{ handleSubmit }">
          <b-form ref="addWorkForm" @submit.prevent="handleSubmit(submitAddWork)" style="font-family: 'Work Sans SemiBold'">

            <validation-provider name="jobTitle"  :rules="{alpha_spaces, required: true, max:64}" v-slot="validationContext">
              <b-form-group label="Job Title">
                <b-form-input id="jobNameInput" v-model="addWork.jobName" type="text" placeholder="Enter job title"
                              :state="getValidationState(validationContext)" aria-describedby="live-feedback-1"></b-form-input>
                <b-form-invalid-feedback id="live-feedback-1">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
              </b-form-group>
            </validation-provider>

            <validation-provider name="company"  :rules="{required: true, max:64}" v-slot="validationContext">
              <b-form-group label="Company">
                <b-form-input id="companyInput" v-model="addWork.company" type="text" placeholder="Enter company name"
                              :state="getValidationState(validationContext)" aria-describedby="live-feedback-2"></b-form-input>
                <b-form-invalid-feedback id="live-feedback-2">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
              </b-form-group>
            </validation-provider>

            <validation-provider name="description"  :rules="{max:1000}" v-slot="validationContext">
              <b-form-group label="Description">
                <b-form-textarea id="descriptionInput" v-model="addWork.description" rows="4" placeholder="Description (optional)"
                                 :state="getValidationState(validationContext)" aria-describedby="live-feedback-3"></b-form-textarea>
                <b-form-invalid-feedback id="live-feedback-3">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
              </b-form-group>
            </validation-provider>

            <b-form-group required label="Start date">
              <input id="startDateWorkExperienceInput" placeholder="yyyy-mm" type="month" class="form-control" v-model="addWork.startDate" min="1900-01" max="2040-01">
            </b-form-group>

            <b-form-group label="End date">
              <input id="endDateWorkExperienceInput" placeholder="yyyy-mm" type="month" class="form-control" v-model="addWork.endDate"
                     :disabled="addWork.currently" :state="checkDates('work')" min="1900-01" max="2040-01">
              <span style="font-size: 12px;color:#dd2222" v-if="checkDates('work')">Start date cannot be posterior to end date</span>
            </b-form-group>

            <div class="form-check">
              <input id="currentlyWorkExperienceInput" class="form-check-input" type="checkbox" value="" v-model="addWork.currently"
                     @click="addWork.endDate=''">
              <label class="form-check-label" for="currentlyWorkExperienceInput">Currently in this job</label>
            </div>

            <div class="float-right">
              <b-button id="submitWorkExperienceButton" variant="warning" type="submit">Submit</b-button>
            </div>

          </b-form>
        </validation-observer>
      </b-modal>

      <b-modal id="addSkillModal" hide-footer ref="addSkillModal">
        <template #modal-header><h5 style="font-family: 'Work Sans SemiBold'">Add Skill</h5></template>
        <validation-observer ref="observer" v-slot="{ handleSubmit }">
          <b-form ref="addSkillForm" @submit.prevent="handleSubmit(submitAddSkill)" style="font-family: 'Work Sans SemiBold'">

            <validation-provider name="skill"  :rules="{alpha_spaces, required: true, max:15}" v-slot="validationContext">
              <b-form-group label="Skill">
                <b-form-input id="nameSkillInput" v-model="addSkill.skill" type="text" placeholder="Enter skill"
                              :state="getValidationState(validationContext)" aria-describedby="live-feedback-1"></b-form-input>
                <b-form-invalid-feedback id="live-feedback-1">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
              </b-form-group>
            </validation-provider>

            <div class="float-right">
              <b-button id="submitSkillButton" variant="warning" type="submit">Submit</b-button>
            </div>

          </b-form>
        </validation-observer>
      </b-modal>

      <b-modal id="addEducationModal" hide-footer  ref="addEducationModal">
          <template #modal-header><h5 style="font-family: 'Work Sans SemiBold'">Add previous education</h5></template>
          <validation-observer ref="observer" v-slot="{ handleSubmit }">
            <b-form ref="addEducationForm" @submit.prevent="handleSubmit(submitAddEducation)" style="font-family: 'Work Sans SemiBold'">

              <validation-provider name="title"  :rules="{alpha_spaces, required: true, max:64}" v-slot="validationContext">
                <b-form-group label="Title">
                  <b-form-input id="titleInput" v-model="addEducation.title" type="text" placeholder="Enter title"
                                :state="getValidationState(validationContext)" aria-describedby="live-feedback-1-ed"></b-form-input>
                  <b-form-invalid-feedback id="live-feedback-1-ed">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>

              <validation-provider name="institution"  :rules="{required: true, max:64}" v-slot="validationContext">
                <b-form-group label="Institution">
                  <b-form-input id="institutionInput" v-model="addEducation.institution" type="text" placeholder="Enter institution"
                                :state="getValidationState(validationContext)" aria-describedby="live-feedback-2-ed"></b-form-input>
                  <b-form-invalid-feedback id="live-feedback-2-ed">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>

              <b-form-group required label="Start date">
                <input id="startDateEducationInput" placeholder="yyyy-mm" type="month" class="form-control" v-model="addEducation.startDate" min="1900-01" max="2040-01">
              </b-form-group>

              <b-form-group label="End date">
                <input id="endDateEducationInput" placeholder="yyyy-mm" type="month" class="form-control" v-model="addEducation.endDate"
                       :disabled="addEducation.currently" :state="checkDates('ed')" min="1900-01" max="2040-01">
                <span style="font-size: 12px;color:#dd2222" v-if="checkDates('ed')">Start date cannot be posterior to end date</span>
              </b-form-group>

              <div class="form-check">
                <input id="currentlyEducationInput" class="form-check-input" type="checkbox" value="" v-model="addEducation.currently"
                       @click="addEducation.endDate=''">
                <label class="form-check-label" for="currentlyEducationInput">Currently enrolled</label>
              </div>

              <div class="float-right">
                <b-button id="submitEducationButton" variant="warning" type="submit">Submit</b-button>
              </div>

            </b-form>
          </validation-observer>
        </b-modal>

    </div>
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
      name: '',
      surname: '',
      logged: false,
      is_jobseeker: true,
      is_company: false,
      is_admin: false,
      token: '',
      username: '',
      username_profile: '',
      edit_mode: false,
      work_experience: [],
      education: [],
      skills: [],
      addSkill: {skill: ''},
      bio: '',
      edit_bio: false,
      modify_bio: '',
      addWork: {
        jobName: '',
        company: '',
        description: '',
        startDate: '',
        endDate: '',
        currently: false
      },
      addEducation: {
        title: '',
        institution: '',
        startDate: '',
        endDate: '',
        currently: false
      },
      file: null,
      uploadValue: 0,
      previewSrc: null,
      downloadImage: null,
      jobs_applied: [],
      fields: ['Offer', 'Company']
    }
  },
  methods: {
    onHome () {
      this.$router.push('/')
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
    onUserProfile () {
      if (this.is_jobseeker & this.logged) {
        this.$router.push('/job_seeker/' + this.username)
      }
    },
    onJobPostings () {
      this.$router.push('/job_postings')
    },
    onAboutUs () {
      this.$router.push('/about_us')
    },
    editBio () {
      this.edit_bio = !this.edit_bio
      this.modify_bio = this.bio
    },
    modifyBio () {
      const path = Vue.prototype.$API_BASE_URL + 'jobseeker/' + this.username_profile.toLowerCase()
      const values = {
        bio: this.modify_bio
      }
      axios.put(path, values, {
        auth: {username: this.token}})
        .then((res) => {
          this.getBio()
          this.edit_bio = !this.edit_bio
        })
        .catch((error) => {
          console.error(error)
          this.showToastError('An error occurred modifying bio')
        })
    },
    showToastError (error) {
      /* eslint-disable */
      this.$bvToast.toast(error, {
        title: `Warning`,
        variant: 'danger',
        solid: true
      })
    },
    getValidationState ({ dirty, validated, valid = null }) {
      return dirty || validated ? valid : null
    },
    checkDates (form) {
      if (form === 'work') {
        if (this.addWork.endDate === '' || this.addWork.startDate === '') {
          return false
        } else {
          const endDate = this.addWork.endDate.split('-')
          const startDate = this.addWork.startDate.split('-')
          if (endDate[0] < startDate[0]) {
            return true
          } else if (endDate[0] === startDate[0]) {
            if (endDate[1] < startDate[1]) {
              return true
            }
          }
        }
        return false
      } else {
        if (this.addEducation.endDate === '' || this.addEducation.startDate === '') {
          return false
        } else {
          const endDate = this.addEducation.endDate.split('-')
          const startDate = this.addEducation.startDate.split('-')
          if (endDate[0] < startDate[0]) {
            return true
          } else if (endDate[0] === startDate[0]) {
            if (endDate[1] < startDate[1]) {
              return true
            }
          }
        }
        return false
      }
    },
    getApplicants () {
      const path = Vue.prototype.$API_BASE_URL + 'applications/' + this.username_profile
      axios.get(path, {
        auth: {username: this.token}})
        .then((res) => {
          this.jobs_applied = []
          for (let application in res.data) {
            this.jobs_applied.push({'Offer': res.data[application].job_offer_name, 'Company': res.data[application].job_offer_company, 'Reference': res.data[application].job_offer_id, 'Username': res.data[application].company_username})
          }
        })
        // eslint-disable-next-line
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
        })
    },
    getWorkExperience () {
      const path = Vue.prototype.$API_BASE_URL + 'work_experience/' + this.username_profile
      axios.get(path)
        .then((res) => {
          this.work_experience = res.data
        })
        .catch((error) => {
          console.error(error)
        })
    },
    getEducation () {
      const path = Vue.prototype.$API_BASE_URL + 'education/' + this.username_profile
      axios.get(path)
        .then((res) => {
          this.education = res.data
        })
        .catch((error) => {
          console.error(error)
        })
    },
    onAddWork () {
      this.$refs.addWorkModal.show()
    },
    submitAddWork () {
      const path = Vue.prototype.$API_BASE_URL + 'work_experience/' + this.username
      const parameters = {
        job_name: this.addWork.jobName,
        company: this.addWork.company,
        start_date: this.addWork.startDate,
        end_date: this.addWork.endDate,
        description: this.addWork.description,
        currently: this.addWork.currently
      }
      axios.post(path, parameters, {
        auth: {username: this.token}})
        .then((res) => {
          this.getWorkExperience()
          this.$refs.addWorkModal.hide('addWorkModal')
          this.addWork = {
            jobName: '',
            company: '',
            description: '',
            startDate: '',
            endDate: '',
            currently: false
          }
        })
        .catch((error) => {
          this.showToastError('An error occurred modifying Work experience')
          console.error(error)
        })
    },
    deleteWork (work) {
      const path = Vue.prototype.$API_BASE_URL + 'delete_work_experience/' + this.username
      const parameters = {id: work.id}
      axios.post(path, parameters, {
        auth: {username: this.token}})
        .then((res) => {
          this.getWorkExperience()
        })
        .catch((error) => {
          console.error(error)
          this.showToastError('Error deleting work experience')
        })
    },
    onAddEducation () {
      this.$refs.addEducationModal.show()
    },
    submitAddEducation () {
      const path = Vue.prototype.$API_BASE_URL + 'education/' + this.username
      const parameters = {
        title: this.addEducation.title,
        institution: this.addEducation.institution,
        start_date: this.addEducation.startDate,
        end_date: this.addEducation.endDate,
        currently: this.addEducation.currently
      }
      axios.post(path, parameters, {
        auth: {username: this.token}})
        .then((res) => {
          this.getEducation()
          this.$refs.addEducationModal.hide('addEducationModal')
          this.addEducation = {
            title: '',
            institution: '',
            startDate: '',
            endDate: '',
            currently: false
          }
        })
        .catch((error) => {
          console.error(error)
          this.showToastError('Error adding education')
        })
    },
    submitAddSkill () {
      const path = Vue.prototype.$API_BASE_URL + 'jobseeker/' + this.username
      const parameters = { skills: [this.addSkill.skill] }
      axios.put(path, parameters, {auth: {username: this.token}})
        .then((res) => {
          this.getSkills()
          this.$refs.addSkillModal.hide()
          this.addSkill = {skill: ''}
        })
        .catch((error) => {
          console.error(error)
          console.log(this.addSkill.skill)
          this.showToastError('Error Adding Skills')
        })
    },
    onAddSkill () {
      this.$refs.addSkillModal.show()
    },
    getSkills () {
      const path = Vue.prototype.$API_BASE_URL + 'jobseeker/' + this.username_profile
      axios.get(path)
        .then((res) => {
          this.skills = res.data.account.skills
        })
        .catch((error) => {
          console.error(error)
        })
    },
    deleteEducation (ed) {
      const path = Vue.prototype.$API_BASE_URL + 'delete_education/' + this.username
      const parameters = {id: ed.id}
      axios.post(path, parameters, {
        auth: {username: this.token}})
        .then((res) => {
          this.getEducation()
        })
        .catch((error) => {
          console.error(error)
          this.showToastError('Error deleting education')

        })
    },
    deleteSkill (skill) {
      const path = Vue.prototype.$API_BASE_URL + 'jobseeker/' + this.username
      const parameters = { remove_skills: [skill] }
      axios.put(path, parameters, {auth: {username: this.token}})
        .then((res) => {
          this.getSkills()
        })
        .catch((error) => {
          console.error(error)
          this.showToastError('Error Adding Skills')
        })
    },
    resetAddWork () {
      this.addWork = {
        jobName: '',
        company: '',
        startDate: '',
        endDate: '',
        currently: false
      }
    },
    resetAddEducation () {
      this.addEducation = {
        title: '',
        institution: '',
        startDate: '',
        endDate: '',
        currently: false
      }
    },
    getName () {
      const pathJobseeker = Vue.prototype.$API_BASE_URL + 'jobseeker/' + this.username_profile.toLowerCase()
      axios.get(pathJobseeker)
        .then((res) => {
          console.log(res)
          this.name = res.data.account.name
          this.surname = res.data.account.surname
        })
        .catch(() => {
          this.name = 'Name'
          this.surname = 'Surname'
        })
    },
    getBio () {
      const pathJobseeker = Vue.prototype.$API_BASE_URL + 'jobseeker/' + this.username_profile.toLowerCase()
      axios.get(pathJobseeker)
        .then((res) => {
          console.log(res)
          this.bio = res.data.account.bio
        })
        .catch(() => {
          this.bio = ''
        })
    },
    downloadAvatar () {
      firebase.storage().ref(`images/${this.username_profile}/avatar`).getDownloadURL()
        .then((url) => {
          this.downloadImage = url
          console.log(url)
        })
        .catch(() => {
          console.log('This avatar does not exist yet')
        })
    },
    onUpload () {
      const storageRef = firebase.storage().ref(`images/${this.username}/avatar`).put(this.file)
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
    this.username_profile = this.$route.path.split('job_seeker/')[1].toLowerCase()
    this.logged = this.$store.state.logged
    this.username = this.$store.state.username
    this.is_jobseeker = this.$store.state.isJobSeeker
    this.is_company = this.$store.state.isCompany
    this.token = this.$store.state.token
    this.is_admin = this.$store.state.isAdmin
    this.edit_mode = this.username === this.username_profile
    this.getName()
    this.getWorkExperience()
    this.getEducation()
    this.getSkills()
    this.getBio()
    this.downloadAvatar()
    this.getApplicants()
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
.bio-text {
  text-align: left;
  color: dimgray;
  font-size: 16px;
  padding-bottom: 20px;
}
.card-title-work {
  font-family: "Work Sans SemiBold", Montserrat, sans-serif;
  font-size: 20px;
}
.card-title-ed {
  font-family: "Work Sans SemiBold", Montserrat, sans-serif;
  font-size: 20px;
  padding-bottom: 10px;
}
.card-subtitle {
  font-family: "Work Sans SemiBold", Montserrat, sans-serif;
  font-size: 18px;
  padding-bottom: 5px;
}
.card-text {
  font-family: "Work Sans", sans-serif;
  font-size: 14px;
}
.section-title {
  font-family: "Vollkorn",serif;
  font-size: 26px;
  display:inline-block
}
.page-title {
  font-family: "Vollkorn",serif;
  font-size: 30px;
  display:inline-block
}
</style>
