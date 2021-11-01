// CompanyJobOffer.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('CompanyJobOffer resource', () => {
  context('GET offers/companyname', () => {
    it('should return the information of all job offers posted by company universitat123 (now only one job offer)', () => {
      cy.request({
        method: 'GET',
        url: 'offers/universitat123'
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body[0].company).to.eq('universitat123')
          expect(response.body[0].job_name).to.eq('professor')
          expect(response.body.length).to.eq(1)
        })
    })
    it('should return error because the company "universitat333" can not exist', () => {
      cy.request({
        method: 'GET',
        url: 'offers/universitat333',
        failOnStatusCode: false
      })
        .should((response) => {
          expect(response.status).to.eq(404)
        })
    })
  })
})
