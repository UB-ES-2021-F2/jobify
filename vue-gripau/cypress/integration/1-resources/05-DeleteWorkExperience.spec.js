// 05-DeleteWorkExperience.spec.js created with Cypress
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
    it('should return error because we are trying to delete a work experience of another user', () => {
      cy.request({
        method: 'POST',
        url: 'delete_work_experience/cypress',
        auth: {username: localStorage.getItem('token')},
        failOnStatusCode: false
      })
        .should((response) => {
          expect(response.status).to.eq(401)
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
          expect(response.status).to.eq(404)
          expect(response.body.message).to.eq('Work experience with id [0] don\'t exists')
        })
    })
  })
})
