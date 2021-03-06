// 11-Register.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('Register resource', () => {
  context('POST register', () => {
    it('should return the new jobseeker account created', () => {
      cy.request({
        method: 'POST',
        url: 'register',
        body: {
          username: 'cypresstestjobseeker',
          name: 'cypress',
          surname: 'test',
          password: 'Test1234',
          is_job_seeker: 1,
          email: 'cypressjobseeker@cypress.com',
          description: 'prova description'
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(201)
          expect(response.body.username).to.eq('cypresstestjobseeker')
        })
    })
    it('should return an error 409 because the jobseeker already exist ', () => {
      cy.request({
        method: 'POST',
        url: 'register',
        body: {
          username: 'cypresstestjobseeker',
          name: 'cypress',
          surname: 'test',
          password: 'Test1234',
          is_job_seeker: 1,
          email: 'cypressjobseeker@cypress.com',
          description: 'prova description'
        },
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(409)
        })
    })
    it('should return the new company account created', () => {
      cy.request({
        method: 'POST',
        url: 'register',
        body: {
          username: 'cypresstestcompany',
          name: 'cypress',
          surname: 'test',
          password: 'Test1234',
          is_job_seeker: 0,
          email: 'cypresscompany@cypress.com',
          description: 'prova description'
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(201)
          expect(response.body.username).to.eq('cypresstestcompany')
        })
    })
    it('should return an error 409 because the company already exist ', () => {
      cy.request({
        method: 'POST',
        url: 'register',
        body: {
          username: 'cypresstestcompany',
          name: 'cypress',
          surname: 'test',
          password: 'Test1234',
          is_job_seeker: 0,
          email: 'cypresscompany@cypress.com',
          description: 'prova description'
        },
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(409)
        })
    })
    it('should return an error 400 because the username is not alphanumeric ', () => {
      cy.request({
        method: 'POST',
        url: 'register',
        body: {
          username: 'cypresstest_1',
          name: 'cypress',
          surname: 'test',
          password: 'Test1234',
          is_job_seeker: 0,
          email: 'cypresscompany@cypress.com',
          description: 'prova description'
        },
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(400)
        })
    })
    it('should return an error 400 because the name must contain only alphabetic characters or spaces ', () => {
      cy.request({
        method: 'POST',
        url: 'register',
        body: {
          username: 'cypresstest',
          name: 'cypress_1',
          surname: 'test',
          password: 'Test1234',
          is_job_seeker: 0,
          email: 'cypresscompany@cypress.com',
          description: 'prova description'
        },
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(400)
          expect(response.body.message).to.eq('Name must contain only alphabetic characters or spaces')
        })
    })
    it('should return an error 400 because the surname must contain only alphabetic characters', () => {
      cy.request({
        method: 'POST',
        url: 'register',
        body: {
          username: 'cypresstest',
          name: 'cypress',
          surname: 'test test',
          password: 'Test1234',
          is_job_seeker: 0,
          email: 'cypresscompany@cypress.com',
          description: 'prova description'
        },
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(400)
          expect(response.body.message).to.eq('Surname must contain only alphabetic characters')
        })
    })
    it('should return an error 406 because the password does not meet requirements', () => {
      cy.request({
        method: 'POST',
        url: 'register',
        body: {
          username: 'cypresstest',
          name: 'cypress',
          surname: 'test',
          password: 'test',
          is_job_seeker: 0,
          email: 'cypresscompany@cypress.com',
          description: 'prova description'
        },
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(406)
          expect(response.body.message).to.eq('Password invalid! Does not meet requirements')
        })
    })
    it('should return an error 409 because a jobseeker aleady has this email', () => {
      cy.request({
        method: 'POST',
        url: 'register',
        body: {
          username: 'cypresstest1',
          name: 'cypress',
          surname: 'test',
          password: 'Test1234',
          is_job_seeker: 1,
          email: 'cypressjobseeker@cypress.com',
          description: 'prova description'
        },
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(409)
          expect(response.body.message).to.eq('Email already exists')
        })
    })
    it('should return an error 409 because a company aleady has this email', () => {
      cy.request({
        method: 'POST',
        url: 'register',
        body: {
          username: 'cypresstest2',
          name: 'cypress',
          surname: 'test',
          password: 'Test1234',
          is_job_seeker: 1,
          email: 'cypresscompany@cypress.com',
          description: 'prova description'
        },
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(409)
          expect(response.body.message).to.eq('Email already exists')
        })
    })
  })
})
