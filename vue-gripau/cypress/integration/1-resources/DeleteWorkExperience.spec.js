// DeleteWorkExperience.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('DeleteWorkExperience resource', () => {
  before(() => {
    cy.login_jobseeker()
    cy.saveLocalStorage()
  })
  beforeEach(() => {
    cy.restoreLocalStorage()
  })
  context('POST delete_work_experience/username', () => {
    it('should return a message confirming that the work experience with id 1 of the user lordsergi has been deleted', () => {
      cy.request({
        method: 'POST',
        url: 'delete_work_experience/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          id: 1
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body.message).to.eq('Work experience with id [1] deleted')
        })
    })
    it('should return error because the user lordsergi2 can not exist', () => {
      cy.request({
        method: 'POST',
        url: 'delete_work_experience/cypress',
        auth: {username: localStorage.getItem('token')},
        failOnStatusCode: false
      })
        .should((response) => {
          expect(response.status).to.eq(400)
          expect(response.body.message).to.eq('Access denied')
        })
    })
    it('should return error because the work experience with id 0 does not exist', () => {
      cy.request({
        method: 'POST',
        url: 'delete_work_experience/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          id: 0
        },
        failOnStatusCode: false
      })
        .should((response) => {
          expect(response.status).to.eq(400)
          expect(response.body.message).to.eq('Work experience with id [0] don\'t exists')
        })
    })
  })
})
