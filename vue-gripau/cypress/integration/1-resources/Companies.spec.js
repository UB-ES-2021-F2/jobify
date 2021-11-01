// Companies.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('Companies resource', () => {
  context('GET company/username', () => {
    it('should return the information of the company UB', () => {
      cy.request({
        method: 'GET',
        url: 'company/ub'
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body.account.company).to.eq('ub')
        })
    })
    it('should return error because the company "ub2" can not exist', () => {
      cy.request({
        method: 'GET',
        url: 'company/ub2',
        failOnStatusCode: false
      })
        .should((response) => {
          expect(response.status).to.eq(404)
        })
    })
  })
})
