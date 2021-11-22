// 03-CompanyList.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('CompanyList resource', () => {
  context('GET companies', () => {
    it('should return the information of the registered companies (now only one company)', () => {
      cy.request({
        method: 'GET',
        url: 'companies'
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body.length).to.eq(1)
        })
    })
  })
})
