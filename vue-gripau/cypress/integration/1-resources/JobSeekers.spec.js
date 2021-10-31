// Companies.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('JobSeekers resource', () => {
  context('GET /api/jobseeker/username', () => {
    it('should return the information of the jobseeker lordsergi', () => {
      cy.request({
        method: 'GET',
        url: 'http://localhost:5000/api/jobseeker/lordsergi'
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
        url: 'http://localhost:5000/api/jobseeker/lord2',
        failOnStatusCode: false
      })
        .should((response) => {
          expect(response.status).to.eq(404)
        })
    })
  })
})
