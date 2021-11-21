// Companies.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('Companies resource', () => {
  before(() => {
    cy.login_company()
    cy.saveLocalStorage()
  })
  beforeEach(() => {
    cy.restoreLocalStorage()
  })
  context('GET company/company_name', () => {
    it('should return the information of the company universitat123', () => {
      cy.request({
        method: 'GET',
        url: 'company/universitat123'
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body.account.company).to.eq('ub')
        })
    })
    it('should return error because the company "universitat333" does not exist', () => {
      cy.request({
        method: 'GET',
        url: 'company/universitat333',
        failOnStatusCode: false
      })
        .should((response) => {
          expect(response.status).to.eq(404)
        })
    })
  })
  context('PUT company/company_name', () => {
    it('should return the modified company account', () => {
      cy.request({
        method: 'PUT',
        url: 'company/universitat123',
        auth: {username: localStorage.getItem('token')},
        body: {
          password: 'CypressTest123',
          email: 'cypress@cypress.com',
          description: 'new description',
          sector: 'testing',
          location: 'cypress'
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(202)
          expect(response.body.username).to.eq('universitat123')
          expect(response.body.email).to.eq('cypress@cypress.com')
          expect(response.body.description).to.eq('new description')
          expect(response.body.sector).to.eq('testing')
          expect(response.body.location).to.eq('cypress')
        })
    })
    it('should return error 400 because we are trying to add a password which does not meet requirements', () => {
      cy.request({
        method: 'PUT',
        url: 'company/universitat123',
        auth: {username: localStorage.getItem('token')},
        failOnStatusCode: false,
        body: {
          password: 'CypressTest',
          email: 'cypress@cypress.com',
          description: 'new description',
          sector: 'testing',
          location: 'cypress'
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(400)
          expect(response.body.message).to.eq('Wrong email format')
        })
    })
    it('should return error 400 because we are trying to add an incorrect email', () => {
      cy.request({
        method: 'PUT',
        url: 'company/universitat123',
        auth: {username: localStorage.getItem('token')},
        failOnStatusCode: false,
        body: {
          password: 'CypressTest123',
          email: 'cypress test',
          description: 'new description',
          sector: 'testing',
          location: 'cypress'
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(400)
          expect(response.body.message).to.eq('Wrong email format')
        })
    })
    it('should return error 400 because we are trying to add too large fields', () => {
      cy.request({
        method: 'PUT',
        url: 'company/universitat123',
        auth: {username: localStorage.getItem('token')},
        failOnStatusCode: false,
        body: {
          password: 'CypressTest123CypressTest123CypressTest123CypressTest123CypressTest123CypressTest123CypressTest123CypressTest123CypressTest123CypressTest123CypressTest123CypressTest123CypressTest123CypressTest123CypressTest123CypressTest123CypressTest123CypressTest123CypressTest123CypressTest123',
          email: 'cypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypress@cypress.com',
          description: 'new descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew descriptionnew description',
          sector: 'testingtestingtestingtestingtestingtestingtestingtestingtestingtestingtestingtestingtestingtestingtestingtestingtestingtestingtestingtestingtestingtestingtestingtestingtestingtestingtestingtestingtestingtestingtestingtestingtesting',
          location: 'cypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypresscypress'
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(405)
          expect(response.body.message).to.eq('Password invalid! Does not meet requirements')
        })
    })
    it('should return the modified company account', () => {
      cy.request({
        method: 'PUT',
        url: 'company/universitat123',
        auth: {username: localStorage.getItem('token')},
        body: {
          password: 'Password12',
          email: 'ub@gmail.com',
          description: 'hola, som la UB',
          sector: '',
          location: ''
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(202)
          expect(response.body.username).to.eq('universitat123')
        })
    })
  })
  context('DELETE company/company_name', () => {
    it('should return error 400 because we are trying to delete another company', () => {
      cy.request({
        method: 'DELETE',
        url: 'company/cypressuniversity',
        auth: {username: localStorage.getItem('token')},
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(400)
          expect(response.body.message).to.eq('Access denied')
        })
    })
    it('should return a message confirming account deleted', () => {
      cy.request({
        method: 'DELETE',
        url: 'company/universitat123',
        auth: {username: localStorage.getItem('token')}
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body.message).to.eq('Account deleted')
        })
    })
    it('should return the new company account created', () => {
      cy.request({
        method: 'POST',
        url: 'register',
        body: {
          username: 'universitat123',
          name: 'cypress',
          surname: 'test',
          password: 'Password12',
          is_job_seeker: 0,
          email: 'cypresscompany@cypress.com',
          description: 'prova description'
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(201)
          expect(response.body.username).to.eq('universitat123')
        })
    })
  }) */
})
