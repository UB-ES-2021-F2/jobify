// 09-JobSeekers.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('JobSeekers resource', () => {
  before(() => {
    cy.login_jobseeker()
    cy.saveLocalStorage()
  })
  beforeEach(() => {
    cy.restoreLocalStorage()
  })
  context('GET jobseeker/username', () => {
    it('should return the information of the jobseeker lordsergi', () => {
      cy.request({
        method: 'GET',
        url: 'jobseeker/lordsergi'
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body.account.username).to.eq('lordsergi')
        })
    })
    it('should return error because the jobseeker "lord2" can not exist', () => {
      cy.request({
        method: 'GET',
        url: 'jobseeker/lord2',
        failOnStatusCode: false
      })
        .should((response) => {
          expect(response.status).to.eq(404)
        })
    })
  })
  context('POST jobseeker/username', () => {
    it('should return the modified job seeker account', () => {
      cy.request({
        method: 'PUT',
        url: 'jobseeker/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          password: 'Password12',
          email: 'cytest@cytest.com',
          bio: 'new bio',
          name: 'cypress',
          surname: 'test',
          skills: ['cypress', 'testing'],
          remove_skills: ['python']
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(202)
          expect(response.body.username).to.eq('lordsergi')
          expect(response.body.name).to.eq('cypress')
        })
    })
    it('should return error 401 because we are trying to modify another jobseeker', () => {
      cy.request({
        method: 'PUT',
        url: 'jobseeker/cypresstest',
        auth: {username: localStorage.getItem('token')},
        body: {
          password: 'CypressTest12',
          email: 'cytest@cytest.com',
          bio: 'new bio',
          name: 'cypress',
          surname: 'test',
          skills: ['cypress', 'testing'],
          remove_skills: ['python']
        },
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(401)
          expect(response.body.message).to.eq('Access denied')
        })
    })
    it('should return error 405 because the new password does not meet requirements', () => {
      cy.request({
        method: 'PUT',
        url: 'jobseeker/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          password: 'CypressTest',
          email: 'cytest@cytest.com',
          bio: 'new bio',
          name: 'cypress',
          surname: 'test',
          skills: ['cypress', 'testing']
        },
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(405)
          expect(response.body.message).to.eq('Password invalid! Does not meet requirements')
        })
    })
    it('should return 202 because if we are trying to remove an inexisting skill, we do not want any error', () => {
      cy.request({
        method: 'PUT',
        url: 'jobseeker/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          password: 'Password12',
          email: 'cytest@cytest.com',
          bio: 'new bio',
          name: 'cypress',
          surname: 'test',
          skills: ['cypress', 'testing'],
          remove_skills: ['pokemon']
        },
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(202)
        })
    })
    it('should return error 400 because the new fields are too long', () => {
      cy.request({
        method: 'PUT',
        url: 'jobseeker/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          password: 'CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12CypressTest12',
          email: 'cytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytestcytest@cytest.com',
          bio: 'new bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bionew bio',
          name: 'cypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypress',
          surname: 'testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttest',
          skills: ['cypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypress', 'testing']
        },
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(405)
          expect(response.body.message).to.eq('Password invalid! Does not meet requirements')
        })
    })
    it('should return the modified job seeker account', () => {
      cy.request({
        method: 'PUT',
        url: 'jobseeker/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          password: 'Password12',
          email: 'sergi@gmail.com',
          bio: 'hola, soc estudiant',
          name: 'Sergi',
          surname: 'Bech',
          skills: ['python'],
          remove_skills: ['cypress', 'testing']
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(202)
          expect(response.body.username).to.eq('lordsergi')
        })
    })
  })
  context('DELETE jobseeker/username', () => {
    it('should return error 400 because we are trying to delete another jobseeker', () => {
      cy.request({
        method: 'DELETE',
        url: 'jobseeker/cypressjobseeker',
        auth: {username: localStorage.getItem('token')},
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(400)
          expect(response.body.message).to.eq('Access denied')
        })
    })
    it('should return a message confirming account deleted', () => {
      cy.request({
        method: 'DELETE',
        url: 'jobseeker/lordsergi',
        auth: {username: localStorage.getItem('token')}
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body.message).to.eq('Account deleted')
        })
    })
    it('should return the new jobseeker account created', () => {
      cy.request({
        method: 'POST',
        url: 'register',
        body: {
          username: 'lordsergi',
          name: 'Sergi',
          surname: 'Bech',
          password: 'Password12',
          is_job_seeker: 1,
          email: 'sergi@gmail.com',
          description: 'hola, soc estudiant'
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(201)
          expect(response.body.username).to.eq('lordsergi')
        })
    })
    it('should return the education added to the user lordsergi', () => {
      cy.request({
        method: 'POST',
        url: 'education/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          title: 'professor',
          institution: 'universitat de barcelona',
          start_date: '2021-04',
          end_date: '2021-05',
          currently: false
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body.education.username).to.eq('lordsergi')
          expect(response.body.education.title).to.eq('professor')
        })
    })
    it('should return the work experience added to the user lordsergi', () => {
      cy.request({
        method: 'POST',
        url: 'work_experience/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          job_name: 'professor',
          description: 'professor de EDS',
          company: 'cypress',
          start_date: '2021-04',
          end_date: '2021-05',
          currently: false
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body.work_experience.username).to.eq('lordsergi')
          expect(response.body.work_experience.job_name).to.eq('professor')
        })
    })
    it('should return the modified job seeker account', () => {
      cy.request({
        method: 'PUT',
        url: 'jobseeker/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          skills: ['python']
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(202)
          expect(response.body.username).to.eq('lordsergi')
        })
    })
  })
})
