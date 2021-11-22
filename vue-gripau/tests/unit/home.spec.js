import Home from '../../src/components/Home.vue'
import { shallowMount, createLocalVue } from '@vue/test-utils'
import VueRouter from 'vue-router'

const localVue = createLocalVue()
localVue.use(VueRouter)
const router = new VueRouter()

describe('Homepage not logged ', () => {
  let wrapper;

  beforeEach(() => {
    // use this to check the state of anything in the view
    wrapper = shallowMount(Home, {
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
