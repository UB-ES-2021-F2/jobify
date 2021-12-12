// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add('login', (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add('drag', { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add('dismiss', { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite('visit', (originalFn, url, options) => { ... })
import 'cypress-localstorage-commands'

Cypress.Commands.add('login_jobseeker', () => {
  cy.request({
    method: 'POST',
    url: 'login',
    body: {
      username: 'lordsergi',
      password: 'Password12'
    }
  })
    .its('body')
    .then(body => {
      cy.setLocalStorage('token', body.token)
    })
})
Cypress.Commands.add('login_gripau', () => {
  cy.request({
    method: 'POST',
    url: 'login',
    body: {
      username: 'gripau',
      password: 'Password12'
    }
  })
    .its('body')
    .then(body => {
      cy.setLocalStorage('token', body.token)
    })
})
Cypress.Commands.add('login_company', () => {
  cy.request({
    method: 'POST',
    url: 'login',
    body: {
      username: 'universitat123',
      password: 'Password12'
    }
  })
    .its('body')
    .then(body => {
      cy.setLocalStorage('token', body.token)
    })
})
