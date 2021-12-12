// 15-JobOfferApplicants.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('JobOfferApplicants resource', () => {
  before(() => {
    cy.login_company()
    cy.saveLocalStorage()
  })
  beforeEach(() => {
    cy.restoreLocalStorage()
  })
  context('GET offer_applicants/job_offer_id', () => {
    it('should return the list of all applicants to job offer professor', () => {
      cy.request({
        method: 'GET',
        url: 'offer_applicants/1',
        auth: {username: localStorage.getItem('token')}
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body[0].username).to.eq('gripau')
        })
    })
    it('should return error 404 because there are no job offers with that id', () => {
      cy.request({
        method: 'GET',
        url: 'offer_applicants/0',
        auth: {username: localStorage.getItem('token')},
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(404)
        })
    })
  })
})
