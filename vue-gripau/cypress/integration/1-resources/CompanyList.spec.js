// Companies.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('CompanyList resource', () => {
  context('GET /api/companies', () => {
    it('should return the information of the registered companies (now only one company)', () => {
      cy.request({
        method: 'GET',
        url: 'http://localhost:5000/api/companies'
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body.length).to.eq(1)
        })
    })
  })
})
