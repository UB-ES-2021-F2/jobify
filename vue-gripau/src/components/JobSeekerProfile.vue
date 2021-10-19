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
        <div class="bio-text">
          {{bio}}
        </div>

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
          <button v-if="edit_mode" class="btn btn-sm" style="margin-bottom: 5px; margin-left: 20px"><b-icon-plus font-scale="1.5" shift-v="-2"></b-icon-plus></button>
          <div>
            <span class="badge badge-pill badge-warning" style="font-size: 15px">Python</span>
            <span class="badge badge-pill badge-warning" style="font-size: 15px">Java</span>
            <span class="badge badge-pill badge-warning" style="font-size: 15px">SQL</span>
          </div>
        </div>
      </div>

      <b-modal hide-footer="true" hide-backdrop="false"  ref="addWorkModal">
        <template #modal-header><h5 style="font-family: 'Work Sans SemiBold'">Add work experience</h5></template>
        <b-form ref="addWorkForm" @submit.prevent="submitAddWork" @reset.prevent="resetAddWork" style="font-family: 'Work Sans SemiBold'">
          <div class="form-group">
            <label for="jobTitle">Job Title </label>
            <input type="text" class="form-control" id="jobTitle" placeholder="Enter job title" v-model="addWork.jobName">
          </div>
          <div class="form-group">
            <label for="companyName">Company </label>
            <input type="text" class="form-control" id="companyName" placeholder="Enter company name" v-model="addWork.company">
          </div>
          <div class="form-group">
            <label>Description </label>
            <textarea class="form-control" id="description" rows="3" placeholder="Enter job description"
                      v-model="addWork.description"></textarea>
          </div>
          <div class="form-group">
            <label for="startYear">Start month </label>
            <input type="month" class="form-control" id="startYear" v-model="addWork.startDate">
          </div>
          <div class="form-group">
            <label for="endYear">End month </label>
            <input type="month" class="form-control" id="endYear" v-model="addWork.endDate">
          </div>
          <div class="form-check">
            <input class="form-check-input" type="checkbox" value="" id="currentlyCheckbox" v-model="addWork.currently">
            <label class="form-check-label" for="currentlyCheckbox">Currently in this job</label>
          </div>
          <div class="float-right">
            <b-button variant="primary" type="submit">Submit</b-button>
            <b-button variant="secondary" type="reset">Reset</b-button>
          </div>
        </b-form>
      </b-modal>

      <b-modal hide-footer="true" hide-backdrop="false"  ref="addEducationModal">
        <template #modal-header><h5 style="font-family: 'Work Sans SemiBold'">Add previous education</h5></template>
        <b-form ref="addEducationForm" @submit.prevent="submitAddEducation" @reset.prevent="resetAddEducation" style="font-family: 'Work Sans SemiBold'">
          <div class="form-group">
            <label for="title">Title </label>
            <input type="text" class="form-control" id="title" placeholder="Enter job title" v-model="addEducation.title">
          </div>
          <div class="form-group">
            <label for="institution">Institution </label>
            <input type="text" class="form-control" id="institution" placeholder="Enter institution" v-model="addEducation.institution">
          </div>
          <div class="form-group">
            <label for="startYearEd">Start month </label>
            <input type="month" class="form-control" id="startYearEd" v-model="addEducation.startDate">
          </div>
          <div class="form-group">
            <label for="endYearEd">End month </label>
            <input type="month" class="form-control" id="endYearEd" v-model="addEducation.endDate">
          </div>
          <div class="form-check">
            <input class="form-check-input" type="checkbox" value="" id="currentlyCheckboxEd" v-model="addEducation.currently">
            <label class="form-check-label" for="currentlyCheckboxEd">Currently enrolled</label>
          </div>
          <div class="float-right">
            <b-button variant="primary" type="submit">Submit</b-button>
            <b-button variant="secondary" type="reset">Reset</b-button>
          </div>
        </b-form>
      </b-modal>

    </b-container>
  </div>
</template>

<script>
import axios from 'axios'
import Vue from 'vue'

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
      skills: ['Python', 'Java', 'SQL'],
      bio: 'Example bio: I’ve always been a great problem solver, an independent introvert, and a technophile obsessed with the latest devices.\n' +
        'Today, I’m working from home as a software engineer for Google, and I get to show off all these elements of who I am.\n' +
        ' I’m also eager to meet other software engineers in the area, so feel free to connect!',
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
      this.$router.replace({ path: '/',
        query: {
          username: this.username,
          logged: this.logged,
          is_company: this.is_company,
          is_jobseeker: this.is_jobseeker,
          is_admin: this.is_admin,
          token: this.token
        }
      })
    },
    onLogIn () {
      this.$router.replace({ path: '/login' })
    },
    onLogOut () {
      this.$router.replace({path: '/',
        query: {
          username: '',
          logged: false,
          is_company: false,
          is_jobseeker: true,
          is_admin: false,
          token: ''
        }
      })
    },
    onUserProfile () {
      if (this.is_jobseeker & this.logged) {
        this.$router.replace({ path: '/job_seeker/' + this.username,
          query: {
            username: this.username,
            logged: this.logged,
            is_company: this.is_company,
            is_jobseeker: this.is_jobseeker,
            is_admin: this.is_admin,
            token: this.token
          }
        })
      }
    },
    onJobPostings () {
      this.$router.replace({ path: '/job_postings',
        query: {
          username: this.username,
          logged: this.logged,
          is_company: this.is_company,
          is_jobseeker: this.is_jobseeker,
          is_admin: this.is_admin,
          token: this.token
        }
      })
    },
    onAboutUs () {
      this.$router.replace({ path: '/about_us',
        query: {
          username: this.username,
          logged: this.logged,
          is_company: this.is_company,
          is_jobseeker: this.is_jobseeker,
          is_admin: this.is_admin,
          token: this.token
        }
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
      console.log('Submit ' + this.addWork.jobName)
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
      console.log('Delete ' + work.id)
      const path = Vue.prototype.$API_BASE_URL + 'work_experience/' + this.username
      const parameters = {data: { id: work.id }}
      axios.delete(path, parameters, {
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
    deleteEducation (ed) {
      const path = Vue.prototype.$API_BASE_URL + 'education/' + this.username
      const parameters = {data: { id: ed.id }, headers: {token: this.token}}
      axios.delete(path, parameters)
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
    }
  },
  created () {
    this.username_profile = this.$route.path.split('job_seeker/')[1].toLowerCase()
    this.logged = this.$route.query.logged === 'true'
    this.username = this.$route.query.username ? this.$route.query.username : ''
    this.is_jobseeker = this.$route.query.is_jobseeker === 'true'
    this.is_company = this.$route.query.is_company === 'true'
    this.token = this.$route.query.token ? this.$route.query.token : ''
    this.is_admin = this.$route.query.is_admin === 'true'
    this.edit_mode = this.username === this.username_profile
    this.getName()
    this.getWorkExperience()
    this.getEducation()
  }
}

</script>

<style >
.b-navbar{
  font-family: "Work Sans SemiBold", sans-serif;
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
