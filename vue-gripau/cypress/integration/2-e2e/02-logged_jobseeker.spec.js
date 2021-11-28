// 02-logged_jobseeker.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('Logged jobseeker', () => {
  context('Login as a jobseeker', () => {
    it('Should go to login page of jobify', () => {
      cy.visit('http://localhost:5000').get('li[id=logInNavbarButton]').click()
      cy.url().should('eq', 'http://localhost:5000/login')
      cy.get('[id=username-input]').should('exist')
    })
    it('should login as a jobseeker (lordsergi) and go to home page', () => {
      cy.get('[id=username-input]').type('lordsergi')
      cy.get('[id=password-input').type('Password12')
      cy.get('[id=logInButton').click()
      cy.url().should('eq', 'http://localhost:5000/')
    })
  })
  context('Navigate to job offer description page through job postings component, apply to that job offer and return to home page', () => {
    it('should go to job postings page through navbar', () => {
      cy.get('[id=jobPostingsNavbarButton]').click()
      cy.url().should('eq', 'http://localhost:5000/job_postings')
      cy.get('[id=profileNavbarButton]').should('exist')
      cy.get('[id=addJobOfferCard]').should('not.exist')
      cy.get('[id=jobOfferCard]').should('exist')
    })
    it('should go to the job offer professor ub description page', () => {
      cy.get('[id=jobOfferCard]').first().click()
      cy.url().should('eq', 'http://localhost:5000/job_posting/1')
      cy.get('[id=jobOfferJobName]').should('contain', 'professor')
      cy.get('[id=companyNameJobOffer]').should('contain', 'ub')
    })
    it('should apply to the job offer professor ub', () => {
      cy.get('[id=applyButton]').should('exist')
      cy.get('[id=appliedButton]').should('not.exist')
      cy.get('[id=applyButton]').click()
      cy.get('[id=applyMessageInput]').type('Prova')
      cy.get('button:contains(OK)').click()
      cy.get('[id=applyButton]').should('not.exist')
      cy.get('[id=appliedButton]').should('exist')
    })
    it('should return to home page through logo in navbar', () => {
      cy.get('[id=seenButton]').click()
      cy.url().should('eq', 'http://localhost:5000/job_postings')
      cy.get('[id=logoNavbar]').click()
      cy.url().should('eq', 'http://localhost:5000/')
    })
    it('should go to job postings page through "Find the newest jobs" button', () => {
      cy.get('[id=jobPostingsButton]').click()
      cy.url().should('eq', 'http://localhost:5000/job_postings')
      cy.get('[id=profileNavbarButton]').should('exist')
      cy.get('[id=addJobOfferCard]').should('not.exist')
    })
    it('should return to home page through "Home" in navbar', () => {
      cy.get('[id=homeNavbarButton]').click()
      cy.url().should('eq', 'http://localhost:5000/')
    })
  })
  context('Navigate to job offer description page inside a Company profile and return to home page', () => {
    it('should go to companies page through navbar', () => {
      cy.get('[id=companiesNavbarButton]').click()
      cy.url().should('eq', 'http://localhost:5000/companies')
      cy.get('[id=companyCard]').should('exist')
    })
    it('should go to the company ub profile page', () => {
      cy.get('[id=companyCard]').first().click()
      cy.url().should('eq', 'http://localhost:5000/company/universitat123')
      cy.get('[id=nameCompany]').should('contain', 'ub')
      cy.get('[id=jobOfferCard]').should('exist')
    })
    it('should go to the job offer professor ub description page inside ub profile', () => {
      cy.get('[id=jobOfferCard]').first().click()
      cy.url().should('eq', 'http://localhost:5000/job_posting/1')
      cy.get('[id=jobOfferJobName]').should('contain', 'professor')
      cy.get('[id=companyNameJobOffer]').should('contain', 'ub')
      cy.get('[id=applyButton]').should('not.exist')
      cy.get('[id=appliedButton]').should('exist')
    })
    it('should return to company ub profile', () => {
      cy.get('[id=seenButton]').click()
      cy.get('[id=jobOfferCard]').should('exist')
      cy.get('[id=nameCompany]').should('contain', 'ub')
    })
    it('should return to home page through logo in navbar', () => {
      cy.get('[id=logoNavbar]').click()
      cy.url().should('eq', 'http://localhost:5000/')
    })
    it('should go to companies page through "Check our companies" button', () => {
      cy.get('[id=companiesButton]').click()
      cy.url().should('eq', 'http://localhost:5000/companies')
      cy.get('[id=profileNavbarButton]').should('exist')
      cy.get('[id=companyCard]').should('exist')
    })
    it('should return to home page through "Home" in navbar', () => {
      cy.get('[id=homeNavbarButton]').click()
      cy.url().should('eq', 'http://localhost:5000/')
    })
  })
  context('Navigate to about us page', () => {
    it('should go to about us page through navbar', () => {
      cy.get('[id=aboutUsNavbarButton]').click()
      cy.url().should('eq', 'http://localhost:5000/about_us')
      cy.get('[id=profileNavbarButton]').should('exist')
      cy.get('[id=aboutUsTitle').should('contain', 'About Us')
    })
    it('should return to home page through logo in navbar', () => {
      cy.get('[id=logoNavbar]').click()
      cy.url().should('eq', 'http://localhost:5000/')
    })
  })
  context('Navigate to jobseeker profile page', () => {
    it('should go to jobseeker profile page through navbar', () => {
      cy.get('[id=profileNavbarButton]').click()
      cy.url().should('eq', 'http://localhost:5000/job_seeker/lordsergi')
      cy.get('[id=activeProfileNavbarButton]').should('exist')
      cy.get('[id=profileNavbarButton]').should('not.exist')
      cy.get('[id=nameSurnameFields]').should('contain', 'Sergi Bech')
    })
    it('should edit bio', () => {
      cy.get('[id=bioField1]').should('contain', 'hola, soc estudiant')
      cy.get('[id=bioField2]').should('not.exist')
      cy.get('[id=enableEditBioButton]').click()
      cy.get('[id=editBioField]').should('exist')
      cy.get('[id=bioInput]').clear()
      cy.get('[id=submitEditBioButton]').click()
      cy.get('[id=bioField2]').should('contain', 'Write about yourself!')
      cy.get('[id=enableEditBioButton]').click()
      cy.get('[id=bioInput]').type('hola, soc estudiant')
      cy.get('[id=submitEditBioButton]').click()
      cy.get('[id=bioField1]').should('contain', 'hola, soc estudiant')
    })
    it('should delete a work experience', () => {
      cy.get('[id=jobNameWorkExperience]').should('exist')
      cy.get('[id=deleteWorkButton]').click()
      cy.get('[id=jobNameWorkExperience]').should('not.exist')
    })
    it('should add a work experience', () => {
      cy.get('[id=addWorkButton]').click()
      cy.get('[id=addWorkModal]').should('exist')
      cy.get('[id=jobNameInput]').type('professor')
      cy.get('[id=companyInput]').type('ub')
      cy.get('[id=descriptionInput]').type('professor de EDS')
      cy.get('[id=startDateWorkExperienceInput]').type('2020-03')
      cy.get('[id=endDateWorkExperienceInput]').type('2020-06')
      cy.get('[id=submitWorkExperienceButton]').click()
      cy.get('[id=jobNameWorkExperience]').should('exist')
      cy.get('[id=descriptionWorkExperience]').should('contain', 'professor de EDS')
    })
    it('should delete an education', () => {
      cy.get('[id=titleEducation]').should('exist')
      cy.get('[id=deleteEducationButton]').click()
      cy.get('[id=titleEducation]').should('not.exist')
    })
    it('should add an education', () => {
      cy.get('[id=addEducationButton]').click()
      cy.get('[id=addEducationModal]').should('exist')
      cy.get('[id=titleInput]').type('Maths phd')
      cy.get('[id=institutionInput]').type('UB')
      cy.get('[id=startDateEducationInput]').type('2021-09')
      cy.get('[id=endDateEducationInput]').type('2021-10')
      cy.get('[id=submitEducationButton]').click()
      cy.get('[id=titleEducation]').should('exist')
      cy.get('[id=titleEducation]').should('contain', 'Maths phd')
    })
    it('should delete a skill', () => {
      cy.get('[id=nameSkill]').should('exist')
      cy.get('[id=deleteSkillButton]').click()
      cy.get('[id=nameSkill]').should('not.exist')
    })
    it('should add a skill', () => {
      cy.get('[id=addSkillButton]').click()
      cy.get('[id=addSkillModal]').should('exist')
      cy.get('[id=nameSkillInput]').type('cypress')
      cy.get('[id=submitSkillButton]').click()
      cy.get('[id=nameSkill]').should('exist')
      cy.get('[id=nameSkill]').should('contain', 'cypress')
    })
    it('should return to home page through logo in navbar', () => {
      cy.get('[id=logoNavbar]').click()
      cy.url().should('eq', 'http://localhost:5000/')
    })
  })
  context('LogOut as jobseeker and register a new jobseeker', () => {
    it('should logout and return to home page', () => {
      cy.get('[id=logOutNavbarButton]').click()
      cy.get('[id=profileNavbarButton]').should('not.exist')
    })
    it('should go to logIn page and show signUp Form', () => {
      cy.get('[id=logInNavbarButton]').click()
      cy.url().should('eq', 'http://localhost:5000/login')
      cy.get('[id=signUpButton]').click()
      cy.get('[id=register-modal]').should('exist')
      cy.get('[id=jobSeekerTab]').should('exist')
    })
    it('should register a new jobseeker', () => {
      cy.get('[id=firstNameJobseekerInput]').type('cyfirst')
      cy.get('[id=lastNameJobseekerInput]').type('cylast')
      cy.get('[id=usernameJobseekerInput]').type('cyusername')
      cy.get('[id=emailJobseekerInput]').type('cypress@cypress.com')
      cy.get('[id=passwordJobseekerInput]').type('Cypress123')
      cy.get('[id=confirmationJobseekerInput]').type('Cypress123')
      cy.get('[id=submitJobseeker]').click()
    })
    it('should login as the new jobseeker created and go to home page', () => {
      cy.get('[id=username-input]').type('cyusername')
      cy.get('[id=password-input').type('Cypress123')
      cy.get('[id=logInButton').click()
      cy.url().should('eq', 'http://localhost:5000/')
      cy.get('[id=profileNavbarButton]').should('contain', 'cyusername')
    })
  })
})
