<template>
  <div id="app">
    <!--Navbar -->
    <b-navbar sticky="true" toggleable="lg" type="light" variant="light">
      <b-navbar-brand href="#" @click="onHome()">
        <img style="max-width: 150px" :src="require('../assets/logo.svg')">
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="#" @click="onHome()">Home</b-nav-item>
          <b-nav-item href="#">Job postings</b-nav-item>
          <b-nav-item href="#" @click="onAboutUs()">About Us</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="!logged" class="ml-auto">
          <b-nav-item href="#" @click="onLogIn()">Log in</b-nav-item>
          <b-nav-item href="#">Sign up</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if="logged" class="ml-auto">
          <b-nav-item active href="#">{{ this.name }}</b-nav-item>
          <button class="btn btn-outline-danger" @click="onLogOut()"> Log Out </button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <!--/.Navbar -->

    <h1 style="font-family: 'Vollkorn"> {{ name }} </h1>

    <div class="m-5">
      <div class="p-3 text-left">
        <h3 style="font-family: 'Vollkorn'; display:inline-block"> Work experience </h3>
        <button class="btn btn-sm" style="margin-bottom: 5px; margin-left: 20px" @click="onAddWork()">Add work experience</button>
        <div class="card mb-3" style="max-width: 700px"  v-for="work in work_experience" :key="work.id">
          <div class="card-header align-items-center">
            <div class="row align-items-center">
              <div class="col">
                <h5 class="card-title">{{work.job_name}}</h5>
              </div>
              <div class="d-flex flex-row-reverse">
                <button class="btn btn-sm btn-danger m-1" @click="deleteWork(work)">Delete</button>
                <!-- <button class="btn btn-sm m-1">Edit</button> -->
              </div>
            </div>
          </div>
          <div class="card-body">
            <h5 class="card-title">{{work.company}}</h5>
            <p class="card-text">{{work.description}}</p>
            <p class="card-text" v-if="!work.currently"><small class="text-muted">{{work.start_date}} - {{work.end_date}}</small></p>
            <p class="card-text" v-if="work.currently"><small class="text-muted">{{work.start_date}} - now</small></p>
          </div>
        </div>
      </div>

      <div class="p-3 text-left">
        <h3 style="font-family: 'Vollkorn'; display:inline-block"> Education </h3>
        <button class="btn btn-sm" style="margin-bottom: 5px; margin-left: 20px" @click="onAddEducation()">Add education</button>
        <div class="card mb-3" style="max-width: 700px"  v-for="ed in education" :key="ed.id">
          <div class="card-body">
            <div class="row align-items-center">
              <div class="col">
                <h5 class="card-title">{{ed.title}}</h5>
              </div>
              <div class="d-flex flex-row-reverse">
                <button class="btn btn-sm btn-danger m-1" @click="deleteEducation(ed)">Delete</button>
                <!-- <button class="btn btn-sm m-1">Edit</button> -->
              </div>
            </div>
            <h6 class="card-title">{{ed.institution}}</h6>
            <p class="card-text" v-if="!ed.currently"><small class="text-muted">{{ed.start_date}} - {{ed.end_date}}</small></p>
            <p class="card-text" v-if="ed.currently"><small class="text-muted">{{ed.start_date}} - now</small></p>
          </div>
        </div>
      </div>

      <div class="p-3 text-left">
        <h3 style="font-family: 'Vollkorn'; display:inline-block"> Skills </h3>
        <button class="btn btn-sm" style="margin-bottom: 5px; margin-left: 20px">Add skills</button>
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
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      name: 'Name Surname',
      username: 'sergi',
      logged: true,
      work_experience: [],
      education: [],
      skills: ['Python', 'Java', 'SQL'],
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
      this.logged = true
    },
    onLogOut () {
      this.logged = false
    },
    onAboutUs () {
      this.$router.replace({ path: '/about_us' })
    },
    getName () {
      // TODO: GET to API
    },
    getWorkExperience () {
      const path = 'http://localhost:5000/work_experience/' + this.username
      axios.get(path)
        .then((res) => {
          this.work_experience = res.data
        })
        .catch((error) => {
          console.error(error)
        })
    },
    getEducation () {
      const path = 'http://localhost:5000/education/' + this.username
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
      const path = 'http://localhost:5000/work_experience/' + this.username
      const parameters = {
        job_name: this.addWork.jobName,
        company: this.addWork.company,
        start_date: this.addWork.startDate,
        end_date: this.addWork.endDate,
        description: this.addWork.description,
        currently: this.addWork.currently
      }
      axios.post(path, parameters) // TODO: add token
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
          console.error(error)
          alert('Error adding work experience')
        })
    },
    deleteWork (work) {
      console.log('Delete ' + work.id)
      const path = 'http://localhost:5000/work_experience/' + this.username
      const parameters = {data: { id: work.id }}
      axios.delete(path, parameters) // TODO: add token
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
      const path = 'http://localhost:5000/education/' + this.username
      const parameters = {
        title: this.addEducation.title,
        institution: this.addEducation.institution,
        start_date: this.addEducation.startDate,
        end_date: this.addEducation.endDate,
        currently: this.addEducation.currently
      }
      axios.post(path, parameters) // TODO: add token
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
      const path = 'http://localhost:5000/education/' + this.username
      const parameters = {data: { id: ed.id }}
      axios.delete(path, parameters) // TODO: add token
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
    }
  },
  created () {
    this.getWorkExperience()
    this.getEducation()
  }
}

</script>

<style >
.navbar.navbar-light{
  font-family: "Work Sans SemiBold";
  font-size: 18px;
  padding: 20px;
  margin-bottom: 20px;
}
</style>
