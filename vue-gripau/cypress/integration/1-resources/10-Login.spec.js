// 10-Login.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('Login resource', () => {
  context('POST login', () => {
    it('should return the token of the user lordsergi', () => {
      cy.request({
        method: 'POST',
        url: 'login',
        body: {
          username: 'lordsergi',
          password: 'Password12'
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body.token.length).to.gt(100)
        })
    })
    it('should return the token of the company universitat123', () => {
      cy.request({
        method: 'POST',
        url: 'login',
        body: {
          username: 'universitat123',
          password: 'Password12'
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body.token.length).to.gt(100)
        })
    })
    it('should return error 404 because user lordsergi2 does not exist', () => {
      cy.request({
        method: 'POST',
        url: 'login',
        failOnStatusCode: false,
        body: {
          username: 'lordsergi2',
          password: 'password'
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(404)
        })
    })
    it('should return error 400 because user lordsergi does not have password "provacypress', () => {
      cy.request({
        method: 'POST',
        url: 'login',
        failOnStatusCode: false,
        body: {
          username: 'lordsergi',
          password: 'provacypress'
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(400)
        })
    })
    it('should return error 400 because company universitat123 does not have password "provacypress', () => {
      cy.request({
        method: 'POST',
        url: 'login',
        failOnStatusCode: false,
        body: {
          username: 'universitat123',
          password: 'provacypress'
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(400)
        })
    })
  })
})
