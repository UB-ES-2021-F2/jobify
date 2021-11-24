import Login from '../../src/components/Login.vue'
import { shallowMount, createLocalVue } from '@vue/test-utils'
import VueRouter from 'vue-router'

const localVue = createLocalVue()
localVue.use(VueRouter)
const router = new VueRouter()

describe('Homepage not logged ', () => {
  let wrapper;

  beforeEach(() => {
    const $route = {
      path: '/'
    }
    // use this to check the state of anything in the view
    wrapper = shallowMount(Login, {
        mocks: {
          $route,
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
    expect(wrapper.vm.token).toEqual("")
  })
  it('is_admin', () => {
    expect(wrapper.vm.is_admin).toEqual(false)
  })
  /*
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
  })*/
})
