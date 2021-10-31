// Companies.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('CompanyJobOffer resource', () => {
  context('GET /api/offers/companyname', () => {
    it('should return the information of all job offers posted by company UB (now only one job offer)', () => {
      cy.request({
        method: 'GET',
        url: 'http://localhost:5000/api/offers/ub'
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body[0].company).to.eq('ub')
          expect(response.body[0].job_name).to.eq('professor')
          expect(response.body.length).to.eq(1)
        })
    })
    it('should return error because the company "ub2" can not exist', () => {
      cy.request({
        method: 'GET',
        url: 'http://localhost:5000/api/offers/ub2',
        failOnStatusCode: false
      })
        .should((response) => {
          expect(response.status).to.eq(404)
        })
    })
  })
})
