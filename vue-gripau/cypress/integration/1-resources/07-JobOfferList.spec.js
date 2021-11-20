// 07-JobOfferList.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('JobOfferList resource', () => {
  context('GET offers', () => {
    it('should return the information of all job offers posted by all companies (now only one job offer by ub)', () => {
      cy.request({
        method: 'GET',
        url: 'offers'
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
