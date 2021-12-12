// 14-JobSeekerApplications.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('JobSeekerApplications resource', () => {
  before(() => {
    cy.login_gripau()
    cy.saveLocalStorage()
  })
  beforeEach(() => {
    cy.restoreLocalStorage()
  })
  context('GET applications/username', () => {
    it('should return the applications of gripau', () => {
      cy.request({
        method: 'GET',
        url: 'applications/gripau',
        auth: {username: localStorage.getItem('token')}
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body[0].job_seeker_username).to.eq('gripau')
        })
    })
    it('should return error 401 because we are not logged as lordsergi', () => {
      cy.request({
        method: 'GET',
        url: 'applications/lordsergi',
        auth: {username: localStorage.getItem('token')},
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(401)
        })
    })
  })
})
