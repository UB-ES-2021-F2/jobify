// 08-JobOffers.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('JobOffers resource', () => {
  before(() => {
    cy.login_company()
    cy.saveLocalStorage()
  })
  beforeEach(() => {
    cy.restoreLocalStorage()
  })
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
        url: 'job_offer/1',
        auth: {username: localStorage.getItem('token')}
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
        auth: {username: localStorage.getItem('token')},
        failOnStatusCode: false
      })
        .should((response) => {
          expect(response.status).to.eq(400)
        })
    })
  })
  context('POST job_offer/company', () => {
    it('should return the job offer which added universitat123', () => {
      cy.request({
        method: 'POST',
        url: 'job_offer/universitat123',
        auth: {username: localStorage.getItem('token')},
        body: {
          job_name: 'job offer cypress test',
          description: 'the title is enough',
          salary: '1000',
          location: 'cypress',
          contract_type: 'Temporal',
          working_hours: 4
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(201)
          expect(response.body.company).to.eq('universitat123')
          expect(response.body.job_name).to.eq('job offer cypress test')
        })
    })
    it('should return error 400 because we are trying to add a job offer with another company', () => {
      cy.request({
        method: 'POST',
        url: 'job_offer/cypressuniversity',
        auth: {username: localStorage.getItem('token')},
        body: {
          job_name: 'job offer cypress test',
          description: 'the title is enough',
          salary: '1000',
          location: 'cypress',
          contract_type: 'Temporal',
          working_hours: 4
        },
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(400)
          expect(response.body.message).to.eq('Access denied')
        })
    })
  })
  context('should delete the new job offer and restore the previous one', () => {
    it('should return a message that the job offer with id 1 has been deleted', () => {
      cy.request({
        method: 'DELETE',
        auth: {username: localStorage.getItem('token')},
        url: 'job_offer/1'
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body.message).to.eq('Offer with id [1] deleted')
        })
    })
    it('should restore the original job offer', () => {
      cy.request({
        method: 'POST',
        url: 'job_offer/universitat123',
        auth: {username: localStorage.getItem('token')},
        body: {
          job_name: 'professor',
          description: 'professor de EDS',
          salary: '5000',
          location: 'Barcelona',
          contract_type: 'Indefinite',
          working_hours: 8
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(201)
          expect(response.body.company).to.eq('universitat123')
          expect(response.body.job_name).to.eq('professor')
        })
    })
  })
})
