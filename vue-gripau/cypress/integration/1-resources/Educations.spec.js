// Companies.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('Companies resource', () => {
  beforeEach(() => {
    cy.login_jobseeker()
  })
  context('GET education/username', () => {
    it('should return the education of the user lordsergi', () => {
      cy.request({
        method: 'GET',
        url: 'education/lordsergi'
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body.length).to.eq(1)
          expect(response.body[0].username).to.eq('lordsergi')
        })
    })
    it('should return error because the user lordsergi2 can not exist', () => {
      cy.request({
        method: 'GET',
        url: 'education/lordsergi2',
        failOnStatusCode: false
      })
        .should((response) => {
          expect(response.status).to.eq(404)
        })
    })
  })
  context('POST education/username', () => {
    it('should print token', () => {
      cy.log(this.token)
    })
    it('should return the education added to the user lordsergi', () => {
      cy.request({
        method: 'POST',
        url: 'education/lordsergi',
        auth: {username: '@token'}
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
        })
    })
  })
})
