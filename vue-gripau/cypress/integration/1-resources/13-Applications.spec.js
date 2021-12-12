// 13-Applications.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('Applications resource', () => {
  before(() => {
    cy.login_gripau()
    cy.saveLocalStorage()
  })
  beforeEach(() => {
    cy.restoreLocalStorage()
  })
  context('GET application/username/job_offer_id', () => {
    it('should return error 404 because gripau does not have any application', () => {
      cy.request({
        method: 'GET',
        url: 'application/gripau/1',
        auth: {username: localStorage.getItem('token')},
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(404)
        })
    })
  })
  context('POST application/username', () => {
    it('should return error 400 as we are trying to apply with another job seeker name', () => {
      cy.request({
        method: 'POST',
        url: 'application/lordsergi',
        auth: {username: localStorage.getItem('token')},
        failOnStatusCode: false,
        body: {
          job_offer_id: 1,
          info: 'blablablabla'
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(400)
          expect(response.body.message).to.eq('Access denied')
        })
    })
    it('should return the application posted', () => {
      cy.request({
        method: 'POST',
        url: 'application/gripau',
        auth: {username: localStorage.getItem('token')},
        body: {
          job_offer_id: 1,
          info: 'blablablabla'
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
        })
    })
  })
})
