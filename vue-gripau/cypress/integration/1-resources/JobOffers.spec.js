// Companies.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('JobOffers resource', () => {
  context('GET job_offer/id', () => {
    it('should return the information of the job offer with id 1', () => {
      cy.request({
        method: 'GET',
        url: 'job_offer/1'
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body.offer.id).to.eq(1)
        })
    })
    it('should return error 404 because there is no offer with id 0', () => {
      cy.request({
        method: 'GET',
        url: 'job_offer/0',
        failOnStatusCode: false
      })
        .should((response) => {
          expect(response.status).to.eq(404)
        })
    })
  })
  context('DELETE job_offer/id', () => {
    it('should return a message that the job offer with id 1 has been deleted', () => {
      cy.request({
        method: 'DELETE',
        url: 'job_offer/1'
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body.message).to.eq('Offer with id [1] deleted')
        })
    })
    it('should return error 400 because there is no offer with id 0', () => {
      cy.request({
        method: 'DELETE',
        url: 'job_offer/0',
        failOnStatusCode: false
      })
        .should((response) => {
          expect(response.status).to.eq(400)
        })
    })
  })
})
