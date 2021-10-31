// Companies.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('JobOfferList resource', () => {
  context('GET /api/offers', () => {
    it('should return the information of all job offers posted by all companies (now only one job offer by UB)', () => {
      cy.request({
        method: 'GET',
        url: 'http://localhost:5000/api/offers'
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body.OfferList.length).to.eq(1)
          expect(response.body.OfferList[0].job_name).to.eq('professor')
        })
    })
  })
})
