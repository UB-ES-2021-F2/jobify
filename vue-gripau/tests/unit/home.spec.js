import { shallowMount, mount } from '@vue/test-utils'
import Home from '../../src/components/Home.vue'

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
            is_jobseeker : false,
            is_company : false,
            token : null,
            is_admin : false,
            name : ""
          }
        }
      }
    })
  });

  it('welcome_message', () => {
    expect(wrapper.vm.welcome_message).toEqual('Welcome to Jobify!')
  })
  it('logged', () => {
    expect(wrapper.vm.logged).toEqual(false)
  })
  it('isJobseeker', () => {
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
  it('name', () => {
    expect(wrapper.vm.name).toEqual("")
  })

  /*it('renders a value from $store.state', () => {
    console.log(wrapper.vm.welcome_message)
    expect(wrapper.find('logged').name().trim()).toEqual('false')
  })*/
  /*it('renders a $store.state value return from computed', () => {
    const wrapper = shallow(State, {
      computed: {
        value_2: () => 'value_2'
      },
      localVue
    })
    expect(wrapper.find('.state-2')
      .text().trim()).toEqual('value_2')
  })
  it('renders a $store.state value return from mapState', () => {
    const wrapper = shallow(State, {
      computed: {
        value_3: () => 'value_3'
      },
      localVue
    })
    expect(wrapper.find('.state-3')
      .text().trim()).toEqual('value_3')
  })*/
})
