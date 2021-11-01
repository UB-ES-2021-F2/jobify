// Companies.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('Companies resource', () => {
  context('GET work_experience/username', () => {
    it('should return the work experience of lordsergi', () => {
      cy.request({
        method: 'GET',
        url: 'work_experience/lordsergi'
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body[0].username).to.eq('lordsergi')
        })
    })
    it('should return error 404 because jobseeker lordsergi2 does not exist', () => {
      cy.request({
        method: 'GET',
        url: 'work_experience/lordsergi2',
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(404)
        })
    })
  })
})
