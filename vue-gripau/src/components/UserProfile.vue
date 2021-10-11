<template>
  <div id="app">
    <!--Navbar -->
    <nav class="mb-1 navbar navbar-expand-lg navbar-light bg-white py-4">
      <a class="navbar-brand">
        <img style="max-width: 150px" :src="require('../assets/logo.svg')">
      </a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent-333"
              aria-controls="navbarSupportedContent-333" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent-333" style="font-size:18px;
       font-family:'Work Sans SemiBold'">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <a class="nav-link" href="#" @click="onHome()">Home
              <span class="sr-only">(current)</span>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Job postings</a>
          </li>
          <li class="nav-item" @click="onAboutUs()">
            <a class="nav-link" href="#">About us</a>
          </li>
        </ul>
        <ul v-if="!logged" class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link" href="#" @click="onLogIn()">Log in</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Sign up</a>
          </li>
        </ul>
        <ul v-if="logged" class="navbar-nav ml-auto">
          <li class="nav-item active">
            <a class="nav-link" href="#">User</a>
          </li>
          <button class="btn btn-outline-danger" @click="onLogOut()"> Log Out </button>
        </ul>
      </div>
    </nav>
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
                <h5 class="card-title">{{work.jobName}}</h5>
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
            <p class="card-text" v-if="!work.currently"><small class="text-muted">{{work.startDate}} - {{work.endDate}}</small></p>
            <p class="card-text" v-if="work.currently"><small class="text-muted">{{work.startDate}} - now</small></p>
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
            <p class="card-text" v-if="!ed.currently"><small class="text-muted">{{ed.startDate}} - {{ed.endDate}}</small></p>
            <p class="card-text" v-if="ed.currently"><small class="text-muted">{{ed.startDate}} - now</small></p>
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

export default {
  data () {
    return {
      name: 'Name Surname',
      logged: true,
      work_experience: [
        {
          'id': 0,
          'jobName': 'Product Owner',
          'company': 'Apple',
          'description': 'I\'m currently enjoying working at Apple as a Product Owner',
          'startDate': '2021',
          'endDate': '2022',
          'currently': true
        },
        {
          'id': 1,
          'jobName': 'Frontend Engineer',
          'company': 'Google',
          'description': 'I worked in the Google Maps team as front end developer and I developed my software\n' +
            '              dev abilities at Google.',
          'startDate': '2020',
          'endDate': '2021',
          'currently': false
        }],
      education: [
        {
          'id': 1,
          'title': ' MSc in Data Science',
          'institution': 'Universitat de Barcelona',
          'startDate': '2019',
          'endDate': '2020',
          'currently': false
        },
        {
          'id': 0,
          'title': ' BSc in Computer Science',
          'institution': 'Universitat de Barcelona',
          'startDate': '2015',
          'endDate': '2019',
          'currently': false
        }],
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
      console.log('LogOut')
    },
    onAboutUs () {
      this.$router.replace({ path: '/about_us' })
    },
    getName () {
      // TODO: GET to API
    },
    getWorkExperience () {
      // TODO: GET to API
    },
    getEducation () {
      // TODO: GET to API
    },
    onAddWork () {
      this.$refs.addWorkModal.show()
    },
    submitAddWork () {
      console.log('Submit ' + this.addWork.jobName)
      // TODO: POST to API
    },
    deleteWork (work) {
      console.log('Delete ' + work.jobName)
      // TODO: DELETE to API
    },
    onAddEducation () {
      this.$refs.addEducationModal.show()
    },
    submitAddEducation () {
      console.log('Submit ' + this.addEducation.title)
      // TODO: POST to API
    },
    deleteEducation (ed) {
      console.log('Delete ' + ed.title)
      // TODO: DELETE to API
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
  }
}

</script>

<style>
.modal-backdrop.show {
  opacity: 0.7;
}
</style>
