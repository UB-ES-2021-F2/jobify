import Comapnies from '../../src/components/Companies.vue'
import { shallowMount, createLocalVue } from '@vue/test-utils'
import VueRouter from 'vue-router'

const localVue = createLocalVue()
localVue.use(VueRouter)
const router = new VueRouter()

describe('Homepage not logged ', () => {
  let wrapper;

  beforeEach(() => {
    // use this to check the state of anything in the view
    wrapper = shallowMount(Comapnies, {
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

})
