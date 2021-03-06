// 01-logged_company.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('Logged company', () => {
  context('Login as a company', () => {
    it('Should go to login page of jobify', () => {
      cy.visit('http://localhost:5000').get('li[id=logInNavbarButton]').click()
      cy.url().should('eq', 'http://localhost:5000/#/login')
      cy.get('[id=username-input]').should('exist')
    })
    it('should login as a company (universitat12) and go to home page', () => {
      cy.get('[id=username-input]').type('universitat123')
      cy.get('[id=password-input').type('Password12')
      cy.get('[id=logInButton').click()
      cy.url().should('eq', 'http://localhost:5000/#/')
    })
  })
  context('Navigate to a job seeker profile of a job seeker that has applied to a one of our job offers', () => {
    it('should go to our company (ub) profile page through navbar profile button', () => {
      cy.get('[id=profileNavbarButton]').click()
      cy.url().should('eq', 'http://localhost:5000/#/company/universitat123')
      cy.get('[id=activeProfileNavbarButton]').should('exist')
      cy.get('[id=profileNavbarButton]').should('not.exist')
      cy.get('[id=nameCompany]').should('contain', 'ub')
    })
    it('should go to the job offer professor ub description page inside our profile', () => {
      cy.get('[id=jobOfferCard]').first().click()
      cy.url().should('eq', 'http://localhost:5000/#/job_posting/1')
      cy.get('h2[id=jobOfferJobName]').should('contain', 'professor')
      cy.get('[id=companyNameJobOffer]').should('contain', 'ub')
    })
    it('should go to the job seeker profile', () => {
      cy.get('[id=applicantsTable]').should('exist')
      cy.get('[id=jobSeekerProfileLink]').click()
      cy.url().should('eq', 'http://localhost:5000/#/job_seeker/gripau')
    })
    it('should return to home page through logo in navbar', () => {
      cy.get('[id=logoNavbar]').click()
      cy.url().should('eq', 'http://localhost:5000/#/')
    })
  })
  context('Navigate to job offer description page through job postings component, post an offer and return to home page', () => {
    it('should go to job postings page through navbar', () => {
      cy.get('[id=jobPostingsNavbarButton]').click()
      cy.url().should('eq', 'http://localhost:5000/#/job_postings')
      cy.get('[id=profileNavbarButton]').should('exist')
      cy.get('[id=showJobOfferModal]').should('exist')
      cy.get('[id=jobOfferCard]').should('exist')
    })
    it('should go to the job offer professor ub description page', () => {
      cy.get('[id=jobOfferButton]').click()
      cy.url().should('eq', 'http://localhost:5000/#/job_posting/1')
      cy.get('h2[id=jobOfferJobName]').should('contain', 'professor')
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
      cy.get('[id=profileNavbarButton]').should('exist')
      cy.get('[id=showJobOfferModal]').should('exist')
    })
    it('should delete a job offer', () => {
      cy.get('[id=jobOfferCard]').should('exist')
      cy.get('[id=jobOfferButton]').click()
      cy.get('[id=deleteButton]').click()
      cy.get('[id=jobOfferCard]').should('not.exist')
    })
    it('should post a new job offer from job postings page', () => {
      cy.get('[id=jobOfferCard]').should('not.exist')
      cy.get('[id=showJobOfferModal]').click()
      cy.get('[id=job-offer-modal]').should('exist')
      cy.get('[id=jobNameInput]').type('professor')
      cy.get('[id=salaryInput]').type('5000')
      cy.get('[id=locationInput]').type('Barcelona')
      cy.get('[id=contractTypeInput]').select('Full-time')
      cy.get('[id=workingHoursInput]').type('8')
      cy.get('[id=descriptionInput]').type('professor de EDS')
      cy.get('[id=postJobOfferButton]').click()
      cy.get('[id=jobOfferCard]').should('exist')
    })
    it('should return to home page through "Home" in navbar', () => {
      cy.get('[id=homeNavbarButton]').click()
      cy.url().should('eq', 'http://localhost:5000/#/')
    })
  })
  context('Navigate to job offer description page inside our company profile and return to home page', () => {
    it('should go to companies page through navbar', () => {
      cy.get('[id=companiesNavbarButton]').click()
      cy.url().should('eq', 'http://localhost:5000/#/companies')
      cy.get('[id=companyCard]').should('exist')
    })
    it('should go to the company ub profile page', () => {
      cy.get('[id=companyCard]').first().click()
      cy.url().should('eq', 'http://localhost:5000/#/company/universitat123')
      cy.get('[id=nameCompany]').should('contain', 'ub')
      cy.get('[id=jobOfferCard]').should('exist')
    })
    it('should go to the job offer professor ub description page inside our profile', () => {
      cy.get('[id=jobOfferCard]').first().click()
      cy.url().should('eq', 'http://localhost:5000/#/job_posting/1')
      cy.get('h2[id=jobOfferJobName]').should('contain', 'professor')
      cy.get('[id=companyNameJobOffer]').should('contain', 'ub')
    })
    it('should return to our company profile', () => {
      cy.get('[id=seenButton]').click()
      cy.get('[id=jobOfferCard]').should('exist')
      cy.get('[id=nameCompany]').should('contain', 'ub')
    })
    it('should return to home page through logo in navbar', () => {
      cy.get('[id=logoNavbar]').click()
      cy.url().should('eq', 'http://localhost:5000/#/')
    })
    it('should go to companies page through "Check our companies" button', () => {
      cy.get('[id=companiesButton]').click()
      cy.url().should('eq', 'http://localhost:5000/#/companies')
      cy.get('[id=profileNavbarButton]').should('exist')
      cy.get('[id=companyCard]').should('exist')
    })
    it('should return to home page through "Home" in navbar', () => {
      cy.get('[id=homeNavbarButton]').click()
      cy.url().should('eq', 'http://localhost:5000/#/')
    })
  })
  context('Navigate to our company profile page through profile button', () => {
    it('should go to our company (ub) profile page through navbar profile button', () => {
      cy.get('[id=profileNavbarButton]').click()
      cy.url().should('eq', 'http://localhost:5000/#/company/universitat123')
      cy.get('[id=activeProfileNavbarButton]').should('exist')
      cy.get('[id=profileNavbarButton]').should('not.exist')
      cy.get('[id=nameCompany]').should('contain', 'ub')
    })
    it('should edit description', () => {
      cy.get('[id=descriptionCompany1]').should('contain', 'hola, som la UB')
      cy.get('[id=descriptionCompany2]').should('not.exist')
      cy.get('[id=enableEditDescriptionButton]').click()
      cy.get('[id=editDescriptionField]').should('exist')
      cy.get('[id=editDescriptionField]').should('exist')
      cy.get('[id=descriptionInput]').clear()
      cy.get('[id=submitEditDescriptionButton]').click()
      cy.get('[id=descriptionCompany2]').should('contain', 'Write about your company!')
      cy.get('[id=enableEditDescriptionButton]').click()
      cy.get('[id=descriptionInput]').type('hola, som la UB')
      cy.get('[id=submitEditDescriptionButton]').click()
      cy.get('[id=descriptionCompany1]').should('contain', 'hola, som la UB')
    })
    it('should edit email', () => {
      cy.get('[id=enableEditEmailButton]').click()
      cy.get('[id=editEmailField]').should('exist')
      cy.get('[id=emailInput]').clear().type('cypress@cypress.com')
      cy.get('[id=submitEditEmailButton]').click()
      cy.get('[id=emailCompany]').should('contain', 'cypress@cypress.com')
      cy.get('[id=enableEditEmailButton]').click()
      cy.get('[id=emailInput]').clear().type('ub@gmail.com')
      cy.get('[id=submitEditEmailButton]').click()
      cy.get('[id=emailCompany]').should('contain', 'ub@gmail.com')
    })
    it('should edit sector', () => {
      cy.get('[id=sectorCompany]').should('contain', 'Unknown')
      cy.get('[id=enableEditSectorButton]').click()
      cy.get('[id=editSectorField]').should('exist')
      cy.get('[id=sectorInput]').clear().type('testing')
      cy.get('[id=submitEditSectorButton]').click()
      cy.get('[id=sectorCompany]').should('contain', 'testing')
      cy.get('[id=enableEditSectorButton]').click()
      cy.get('[id=sectorInput]').clear()
      cy.get('[id=submitEditSectorButton]').click()
      cy.get('[id=sectorCompany]').should('contain', 'Unknown')
    })
    it('should edit location', () => {
      cy.get('[id=locationCompany]').should('contain', 'Unknown')
      cy.get('[id=enableEditLocationButton]').click()
      cy.get('[id=editLocationField]').should('exist')
      cy.get('[id=locationInput]').clear().type('testing')
      cy.get('[id=submitEditLocationButton]').click()
      cy.get('[id=locationCompany]').should('contain', 'testing')
      cy.get('[id=enableEditLocationButton]').click()
      cy.get('[id=locationInput]').clear()
      cy.get('[id=submitEditLocationButton]').click()
      cy.get('[id=locationCompany]').should('contain', 'Unknown')
    })
    it('should return to home page through logo in navbar', () => {
      cy.get('[id=logoNavbar]').click()
      cy.url().should('eq', 'http://localhost:5000/#/')
    })
  })
  context('LogOut as company and register a new company', () => {
    it('should logout and return to home page', () => {
      cy.get('[id=logOutNavbarButton]').click()
      cy.get('[id=profileNavbarButton]').should('not.exist')
    })
    it('should go to logIn page and show signUp Form with Company Tab', () => {
      cy.get('[id=logInNavbarButton]').click()
      cy.url().should('eq', 'http://localhost:5000/#/login')
      cy.get('[id=signUpButton]').click()
      cy.get('[id=register-modal]').should('exist')
      cy.get('[id=jobSeekerTab___BV_tab_button__]').should('have.class', 'nav-link active')
      cy.get('[id=companyTab___BV_tab_button__]').should('have.class', 'nav-link')
      cy.get('ul li').last().click()
      cy.get('[id=jobSeekerTab___BV_tab_button__]').should('have.class', 'nav-link')
      cy.get('[id=companyTab___BV_tab_button__]').should('have.class', 'nav-link active')
    })
    it('should register a new company', () => {
      cy.get('[id=usernameCompanyInput]').type('cycompany')
      cy.get('[id=nameCompanyInput]').type('cypresscompany')
      cy.get('[id=emailCompanyInput]').type('cycompany@cypress.com')
      cy.get('[id=passwordCompanyInput]').type('Cypress123')
      cy.get('[id=confirmationCompanyInput]').type('Cypress123')
      cy.get('[id=submitCompany]').click()
    })
    it('should login as the new company created and go to home page', () => {
      cy.get('[id=username-input]').type('cycompany')
      cy.get('[id=password-input]').type('Cypress123')
      cy.get('[id=logInButton]').click()
      cy.url().should('eq', 'http://localhost:5000/#/')
      cy.get('[id=profileNavbarButton]').should('contain', 'cycompany')
    })
  })
})
