// 01-logged_company.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('No logged', () => {
  context('Navigate to job offer description page through job postings component and return to home page', () => {
    it('should go to job postings page through navbar', () => {
      cy.visit('http://localhost:5000').get('[id=jobPostingsNavbarButton]').click()
      cy.url().should('eq', 'http://localhost:5000/#/job_postings')
      cy.get('[id=profileNavbarButton]').should('not.exist')
      cy.get('[id=logInNavbarButton]').should('exist')
      cy.get('[id=addJobOfferCard]').should('not.exist')
      cy.get('[id=jobOfferCard]').should('exist')
    })
    it('should go to the job offer professor ub description page', () => {
      cy.get('[id=jobOfferCard]').first().click()
      cy.url().should('eq', 'http://localhost:5000/#/job_posting/1')
      cy.get('[id=jobOfferJobName]').should('contain', 'professor')
      cy.get('[id=companyNameJobOffer]').should('contain', 'ub')
    })
    it('should return to home page through logo in navbar', () => {
      cy.get('[id=seenButton]').click()
      cy.url().should('eq', 'http://localhost:5000/#/job_postings')
      cy.get('[id=logoNavbar]').click()
      cy.url().should('eq', 'http://localhost:5000/#/')
    })
    it('should go to job postings page through "Find the newest jobs" button', () => {
      cy.get('[id=jobPostingsButton]').click()
      cy.url().should('eq', 'http://localhost:5000/#/job_postings')
      cy.get('[id=profileNavbarButton]').should('not.exist')
      cy.get('[id=logInNavbarButton]').should('exist')
      cy.get('[id=addJobOfferCard]').should('not.exist')
    })
    it('should return to home page through "Home" in navbar', () => {
      cy.get('[id=homeNavbarButton]').click()
      cy.url().should('eq', 'http://localhost:5000/#/')
    })
  })
  context('Navigate to job offer description page inside ub company profile and return to home page', () => {
    it('should go to companies page through navbar', () => {
      cy.get('[id=companiesNavbarButton]').click()
      cy.url().should('eq', 'http://localhost:5000/#/companies')
      cy.get('[id=companyCard]').should('exist')
    })
    it('should go to the company ub profile page', () => {
      cy.get('[id=companyCard]').first().click()
      cy.url().should('eq', 'http://localhost:5000/#/company/universitat123')
      cy.get('[id=nameCompany]').should('contain', 'ub')
    })
    it('should go to the job offer professor ub description page inside ub profile', () => {
      cy.get('[id=jobOfferCard]').first().click()
      cy.url().should('eq', 'http://localhost:5000/#/job_posting/1')
      cy.get('[id=jobOfferJobName]').should('contain', 'professor')
      cy.get('[id=companyNameJobOffer]').should('contain', 'ub')
    })
    it('should return to ub company profile', () => {
      cy.get('[id=seenButton]').click()
      cy.get('[id=nameCompany]').should('contain', 'ub')
      cy.url().should('eq', 'http://localhost:5000/#/company/universitat123')
    })
    it('should return to home page through logo in navbar', () => {
      cy.get('[id=logoNavbar]').click()
      cy.url().should('eq', 'http://localhost:5000/#/')
    })
    it('should go to companies page through "Check our companies" button', () => {
      cy.get('[id=companiesButton]').click()
      cy.url().should('eq', 'http://localhost:5000/#/companies')
      cy.get('[id=profileNavbarButton]').should('not.exist')
      cy.get('[id=logInNavbarButton]').should('exist')
      cy.get('[id=companyCard]').should('exist')
    })
    it('should return to home page through "Home" in navbar', () => {
      cy.get('[id=homeNavbarButton]').click()
      cy.url().should('eq', 'http://localhost:5000/#/')
    })
  })
})
