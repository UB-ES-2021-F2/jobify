import JobPosting from '../../src/components/JobPosting.vue'
import { shallowMount, createLocalVue } from '@vue/test-utils'
import VueRouter from 'vue-router'

const localVue = createLocalVue()
localVue.use(VueRouter)
const router = new VueRouter()

describe('Homepage not logged ', () => {
  let wrapper;

  beforeEach(() => {
    // use this to check the state of anything in the view
    wrapper = shallowMount(JobPosting, {
        mocks: {
          $store: {
            state: {
              logged : false,
              username : null,
              isJobSeeker : false,
              isCompany : false,
              token : null,
              isAdmin : false,
              name : ""
            }
          }
        }
      },
      localVue,
      router)
  });

  it('welcome_message', () => {
    expect(wrapper.vm.welcome_message).toEqual('Welcome to Jobify!')
  })
  it('logged', () => {
    expect(wrapper.vm.logged).toEqual(false)
  })
  it('is_jobseeker', () => {
    expect(wrapper.vm.is_jobseeker).toEqual(false)
  })
  it('is_company', () => {
    expect(wrapper.vm.is_company).toEqual(false)
  })
  it('token', () => {
    expect(wrapper.vm.token).toEqual(null)
  })
  it('is_admin', () => {
    expect(wrapper.vm.is_admin).toEqual(false)
  })
})



describe('Homepage logged jobSeeker ', () => {
  let wrapper;
  beforeEach(() => {
    const $route = {
      path: '/'
    }
    // use this to check the state of anything in the view
    wrapper = shallowMount(JobPosting, {
      mocks: {
        $route,
        $store: {
          state: {
            logged : true,
            username : "sergiger",
            isJobSeeker : true,
            isCompany : false,
            token : "null",
            isAdmin : false,
            name : ""
          }
        }
      },
      localVue,
      router})
  });

  it('logged', () => {
    expect(wrapper.vm.logged).toEqual(true)
  })
  it('is_jobseeker', () => {
    expect(wrapper.vm.is_jobseeker).toEqual(true)
  })
  it('is_company', () => {
    expect(wrapper.vm.is_company).toEqual(false)
  })
  it('token', () => {
    expect(wrapper.vm.token).toEqual("null")
  })
  it('is_admin', () => {
    expect(wrapper.vm.is_admin).toEqual(false)
  })
  it('onProfile()', () => {
    console.log(wrapper.vm.$route.path)
    wrapper.vm.onProfile()
    console.log(wrapper.vm.$route.path)
    expect(wrapper.vm.$route.path).toEqual('/job_seeker/sergiger')
  })
})

describe('Homepage logged company ', () => {
  let wrapper;

  beforeEach(() => {
    const $route = {
      path: '/'
    }
    // use this to check the state of anything in the view
    wrapper = shallowMount(JobPosting, {
      mocks: {
        $route,
        $store: {
          state: {
            logged : true,
            username : "events",
            isJobSeeker : false,
            isCompany : true,
            token : "null",
            isAdmin : false,
            name : ""
          }
        }
      },
      localVue,
      router})
  });

  it('logged', () => {
    expect(wrapper.vm.logged).toEqual(true)
  })
  it('is_jobseeker', () => {
    expect(wrapper.vm.is_jobseeker).toEqual(false)
  })
  it('is_company', () => {
    expect(wrapper.vm.is_company).toEqual(true)
  })
  it('token', () => {
    expect(wrapper.vm.token).toEqual("null")
  })
  it('is_admin', () => {
    expect(wrapper.vm.is_admin).toEqual(false)
  })
  it('onProfile()', () => {
    console.log(wrapper.vm.$route.path)
    wrapper.vm.onProfile()
    console.log(wrapper.vm.$route.path)
    expect(wrapper.vm.$route.path).toEqual('/company/events')
  })
  it('onLogIn()', () => {
    console.log(wrapper.vm.$route.path)
    wrapper.vm.onLogIn()
    console.log(wrapper.vm.$route.path)
    expect(wrapper.vm.$route.path).toEqual('/login')
  })
  it('onCompanies()', () => {
    console.log(wrapper.vm.$route.path)
    wrapper.vm.onCompanies()
    console.log(wrapper.vm.$route.path)
    expect(wrapper.vm.$route.path).toEqual('/companies')
  })
  it('onJobPostings()', () => {
    console.log(wrapper.vm.$route.path)
    wrapper.vm.onJobPostings()
    console.log(wrapper.vm.$route.path)
    expect(wrapper.vm.$route.path).toEqual('/job_postings')
  })
  it('onAboutUs()', () => {
    console.log(wrapper.vm.$route.path)
    wrapper.vm.onAboutUs()
    console.log(wrapper.vm.$route.path)
    expect(wrapper.vm.$route.path).toEqual('/about_us')
  })
  /*it('onLogOut()', () => {
    wrapper.vm.onLogOut()
    expect(wrapper.vm.logged).toEqual(false)
    expect(wrapper.vm.username).toEqual(null)
    expect(wrapper.vm.token).toEqual(null)
    expect(wrapper.vm.is_jobseeker).toEqual(null)
    expect(wrapper.vm.is_company).toEqual(null)
    expect(wrapper.vm.is_admin).toEqual(null)
  })*/
})
