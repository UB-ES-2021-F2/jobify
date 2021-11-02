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
          <b-nav-item active @click="onUserProfile()">{{ this.username }}</b-nav-item>
          <button class="btn btn-outline-danger" @click="onLogOut()"> Log Out </button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <!--/.Navbar -->

    <b-container>

      <h2 style="font-family: 'Vollkorn', serif"> {{ name }} {{ surname }} </h2>

      <div class="container-md-5 p-2 align-items-center">
        <div v-if="bio != null && !edit_bio " class="bio-text">
          {{bio}}
          <p></p>
        </div>
        <div v-if="bio === null && !edit_bio && edit_mode" class="bio-text">
          {{bio}}
          <p></p>
        </div>
        <b-container v-if="edit_bio" fluid>
          <b-row align="center">
            <b-col sm="10">
              <b-form-textarea v-model="modify_bio" id="textarea-auto-height" rows="3" max-rows="8"/>
            </b-col>
            <b-col align-self="center" sm="1">
              <b-button variant="success" @click="modifyBio()">Save</b-button>
            </b-col>
          </b-row>
          <p></p>
        </b-container>
        <button v-if="edit_mode" class="btn btn-sm" style="margin-bottom: 5px; margin-left: 20px" @click="editBio()" ><b-icon-pencil-fill font-scale="1.5" shift-v="-2"></b-icon-pencil-fill></button>

        <div class="text-left p-2 pb-3" style="max-width: 50rem">
          <p class="section-title"> Work experience </p>
          <button v-if="edit_mode" class="btn btn-sm" style="margin-bottom: 5px; margin-left: 20px" @click="onAddWork()"><b-icon-plus font-scale="1.5" shift-v="-2"></b-icon-plus></button>
          <div class="card mb-lg-1"  v-for="work in work_experience" :key="work.id">
            <div class="card-header d-flex align-items-center">
              <span class="card-title-work">{{work.job_name}}</span>
              <button v-if="edit_mode" class="ml-auto btn btn-sm btn-danger" @click="deleteWork(work)">Delete</button>
            </div>
            <div class="card-body">
              <p class="card-subtitle">{{work.company}}</p>
              <p class="card-text">{{work.description}}</p>
              <p class="card-text" v-if="!work.currently"><small class="text-muted">{{work.start_date}} - {{work.end_date}}</small></p>
              <p class="card-text" v-if="work.currently"><small class="text-muted">{{work.start_date}} - now</small></p>
            </div>
          </div>
        </div>

        <div class="text-left p-2 pb-3" style="max-width: 50rem">
          <p class="section-title"> Education </p>
          <button v-if="edit_mode" class="btn btn-sm" style="margin-bottom: 5px; margin-left: 20px" @click="onAddEducation()"><b-icon-plus font-scale="1.5" shift-v="-2"></b-icon-plus></button>
          <div class="card mb-lg-1" v-for="ed in education" :key="ed.id">
            <div class="card-body">
              <div class="d-flex align-items-center">
                <span class="card-title-ed">{{ed.title}}</span>
                <button v-if="edit_mode" class="ml-auto btn btn-sm btn-danger" @click="deleteEducation(ed)">Delete</button>
              </div>
              <p class="card-subtitle">{{ed.institution}}</p>
              <p class="card-text" v-if="!ed.currently"><small class="text-muted">{{ed.start_date}} - {{ed.end_date}}</small></p>
              <p class="card-text" v-if="ed.currently"><small class="text-muted">{{ed.start_date}} - now</small></p>
            </div>
          </div>
        </div>

        <div class="text-left p-2 pb-3" style="max-width: 50rem">
          <p class="section-title"> Skills </p>
          <button v-if="edit_mode" class="btn btn-sm" style="margin-bottom: 5px; margin-left: 20px" @click="onAddSkill()"><b-icon-plus font-scale="1.5" shift-v="-2"></b-icon-plus></button>
          <div>
            <span class="badge badge-pill badge-warning p-2 m-1"  v-for="skill in skills" :key="skill">{{ skill }}</span>
          </div>
        </div>
      </div>

      <b-modal hide-footer hide-backdrop ref="addWorkModal">
        <template #modal-header><h5 style="font-family: 'Work Sans SemiBold'">Add work experience</h5></template>
        <validation-observer ref="observer" v-slot="{ handleSubmit }">
          <b-form ref="addWorkForm" @submit.prevent="handleSubmit(submitAddWork)" style="font-family: 'Work Sans SemiBold'">

            <validation-provider name="jobTitle"  :rules="{alpha_spaces, required: true, max:64}" v-slot="validationContext">
              <b-form-group label="Job Title">
                <b-form-input v-model="addWork.jobName" type="text" id="jobTitle" placeholder="Enter job title"
                              :state="getValidationState(validationContext)" aria-describedby="live-feedback-1"></b-form-input>
                <b-form-invalid-feedback id="live-feedback-1">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
              </b-form-group>
            </validation-provider>

            <validation-provider name="company"  :rules="{required: true, max:64}" v-slot="validationContext">
              <b-form-group label="Company">
                <b-form-input v-model="addWork.company" type="text" id="company" placeholder="Enter company name"
                              :state="getValidationState(validationContext)" aria-describedby="live-feedback-2"></b-form-input>
                <b-form-invalid-feedback id="live-feedback-2">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
              </b-form-group>
            </validation-provider>

            <validation-provider name="description"  :rules="{max:1000}" v-slot="validationContext">
              <b-form-group label="Description">
                <b-form-textarea v-model="addWork.description" id="description" rows="4" placeholder="Description (optional)"
                              :state="getValidationState(validationContext)" aria-describedby="live-feedback-3"></b-form-textarea>
                <b-form-invalid-feedback id="live-feedback-3">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
              </b-form-group>
            </validation-provider>

            <b-form-group required label="Start date">
              <input placeholder="yyyy-mm" type="month" class="form-control" id="startYear" v-model="addWork.startDate" min="1900-01" max="2040-01">
            </b-form-group>

            <b-form-group label="End date">
              <input placeholder="yyyy-mm" type="month" class="form-control" id="endYear" v-model="addWork.endDate"
                     :disabled="addWork.currently" :state="checkDates('work')" min="1900-01" max="2040-01">
              <span style="font-size: 12px;color:#dd2222" v-if="checkDates('work')">Start date cannot be posterior to end date</span>
            </b-form-group>

            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="currentlyCheckbox" v-model="addWork.currently"
                     @click="addWork.endDate=''">
              <label class="form-check-label" for="currentlyCheckbox">Currently in this job</label>
            </div>

            <div class="float-right">
              <b-button variant="primary" type="submit">Submit</b-button>
            </div>

          </b-form>
        </validation-observer>
      </b-modal>

      <b-modal hide-footer hide-backdrop ref="addSkillModal">
        <template #modal-header><h5 style="font-family: 'Work Sans SemiBold'">Add Skill</h5></template>
        <validation-observer ref="observer" v-slot="{ handleSubmit }">
          <b-form ref="addSkillForm" @submit.prevent="handleSubmit(submitAddSkill)" style="font-family: 'Work Sans SemiBold'">

            <validation-provider name="skill"  :rules="{alpha_spaces, required: true, max:15}" v-slot="validationContext">
              <b-form-group label="Skill">
                <b-form-input v-model="addSkill.skill" type="text" id="skill" placeholder="Enter skill"
                              :state="getValidationState(validationContext)" aria-describedby="live-feedback-1"></b-form-input>
                <b-form-invalid-feedback id="live-feedback-1">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
              </b-form-group>
            </validation-provider>

            <div class="float-right">
              <b-button variant="primary" type="submit">Submit</b-button>
            </div>

          </b-form>
        </validation-observer>
      </b-modal>

      <b-modal hide-footer hide-backdrop  ref="addEducationModal">
        <template #modal-header><h5 style="font-family: 'Work Sans SemiBold'">Add previous education</h5></template>
        <validation-observer ref="observer" v-slot="{ handleSubmit }">
          <b-form ref="addEducationForm" @submit.prevent="handleSubmit(submitAddEducation)" style="font-family: 'Work Sans SemiBold'">

            <validation-provider name="title"  :rules="{alpha_spaces, required: true, max:64}" v-slot="validationContext">
              <b-form-group label="Title">
                <b-form-input v-model="addEducation.title" type="text" id="title" placeholder="Enter title"
                              :state="getValidationState(validationContext)" aria-describedby="live-feedback-1-ed"></b-form-input>
                <b-form-invalid-feedback id="live-feedback-1-ed">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
              </b-form-group>
            </validation-provider>

            <validation-provider name="institution"  :rules="{required: true, max:64}" v-slot="validationContext">
              <b-form-group label="Institution">
                <b-form-input v-model="addEducation.institution" type="text" id="institution" placeholder="Enter institution"
                              :state="getValidationState(validationContext)" aria-describedby="live-feedback-2-ed"></b-form-input>
                <b-form-invalid-feedback id="live-feedback-2-ed">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
              </b-form-group>
            </validation-provider>

            <b-form-group required label="Start date">
              <input placeholder="yyyy-mm" type="month" class="form-control" id="startYearEd" v-model="addEducation.startDate" min="1900-01" max="2040-01">
            </b-form-group>

            <b-form-group label="End date">
              <input placeholder="yyyy-mm" type="month" class="form-control" id="endYearEd" v-model="addEducation.endDate"
                     :disabled="addEducation.currently" :state="checkDates('ed')" min="1900-01" max="2040-01">
              <span style="font-size: 12px;color:#dd2222" v-if="checkDates('ed')">Start date cannot be posterior to end date</span>
            </b-form-group>

            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="" id="currentlyCheckboxEd" v-model="addEducation.currently"
                     @click="addEducation.endDate=''">
              <label class="form-check-label" for="currentlyCheckboxEd">Currently enrolled</label>
            </div>

            <div class="float-right">
              <b-button variant="primary" type="submit">Submit</b-button>
            </div>

          </b-form>
        </validation-observer>
      </b-modal>

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
      }
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
    onLogOut () {
      this.$store.commit('logout')
      this.$router.replace({ path: '/' })
    },
    onUserProfile () {
      if (this.is_jobseeker & this.logged) {
        this.$router.replace({ path: '/job_seeker/' + this.username })
      }
    },
    onJobPostings () {
      this.$router.replace({ path: '/job_postings' })
    },
    onAboutUs () {
      this.$router.replace({ path: '/about_us' })
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
          alert(' An error occurred modifying bio')
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
          alert(error.response.data.message)
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
          alert('Error deleting work experience')
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
          alert('Error adding education')
        })
    },
    submitAddSkill () {
      const path = Vue.prototype.$API_BASE_URL + 'jobseeker/' + this.username
      const parameters = { skills: [this.addSkill.skill] }
      axios.put(path, parameters, {auth: {username: this.token}})
        .then((res) => {
          this.getSkills()
          this.$refs.addSkillModal.hide()
        })
        .catch((error) => {
          console.error(error)
          console.log(this.addSkill.skill)
          alert('Error Adding Skills')
        })
    },
    onAddSkill () {
      this.$refs.addSkillModal.show()
    },
    getSkills () {
      const path = Vue.prototype.$API_BASE_URL + 'jobseeker/' + this.username
      const parameters = {headers: {token: this.token}}
      axios.get(path, parameters)
        .then((res) => {
          this.skills = res.data.account.skills
        })
        .catch((error) => {
          console.error(error)
          alert('Error Getting Skills')
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
          alert('Error deleting education')
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
</style>
