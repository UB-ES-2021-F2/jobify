// 04-DeleteEducation.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('DeleteEducation resource', () => {
  before(() => {
    cy.login_jobseeker()
    cy.saveLocalStorage()
  })
  beforeEach(() => {
    cy.restoreLocalStorage()
  })
  context('POST delete_education/username', () => {
    it('should return a message confirming that the education with id 1 of the user lordsergi has been deleted', () => {
      cy.request({
        method: 'POST',
        url: 'delete_education/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          id: 1
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body.message).to.eq('Education with id [1] deleted')
        })
    })
    it('should return error because the user lordsergi2 can not exist', () => {
      cy.request({
        method: 'POST',
        url: 'delete_education/cypress',
        auth: {username: localStorage.getItem('token')},
        failOnStatusCode: false
      })
        .should((response) => {
          expect(response.status).to.eq(401)
          expect(response.body.message).to.eq('Access denied')
        })
    })
    it('should return error because the education with id 0 does not exist', () => {
      cy.request({
        method: 'POST',
        url: 'delete_education/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          id: 0
        },
        failOnStatusCode: false
      })
        .should((response) => {
          expect(response.status).to.eq(404)
          expect(response.body.message).to.eq('Education with id [0] doesn\'t exist')
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
  })
})
