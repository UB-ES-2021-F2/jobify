// WorkExperience.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('WorkExperience resource', () => {
  before(() => {
    cy.login_jobseeker()
    cy.saveLocalStorage()
  })
  beforeEach(() => {
    cy.restoreLocalStorage()
  })
  context('GET work_experience/username', () => {
    it('should return the work experience of lordsergi', () => {
      cy.request({
        method: 'GET',
        url: 'work_experience/lordsergi'
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body[0].username).to.eq('lordsergi')
        })
    })
    it('should return error 404 because jobseeker lordsergi2 does not exist', () => {
      cy.request({
        method: 'GET',
        url: 'work_experience/lordsergi2',
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(404)
        })
    })
  })
  context('POST work_experience/username', () => {
    it('should return the work experience added to the user lordsergi', () => {
      cy.request({
        method: 'POST',
        url: 'work_experience/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          job_name: 'work experience test cypress',
          description: 'nothing more to say here',
          company: 'cypress',
          start_date: '2021-04',
          end_date: '2021-05',
          currently: false
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body.work_experience.username).to.eq('lordsergi')
          expect(response.body.work_experience.job_name).to.eq('work experience test cypress')
        })
    })
    it('should return error 400 because we are trying to add a work experience to another user', () => {
      cy.request({
        method: 'POST',
        url: 'work_experience/cytest',
        auth: {username: localStorage.getItem('token')},
        body: {
          job_name: 'work experience test cypress',
          description: 'nothing more to say here',
          company: 'cypress',
          start_date: '2021-04',
          end_date: '2021-05',
          currently: false
        },
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(400)
          expect(response.body.message).to.eq('Access denied')
        })
    })
    it('should return error 400 because we are trying to add dates in a wrong format', () => {
      cy.request({
        method: 'POST',
        url: 'work_experience/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          job_name: 'work experience test cypress',
          description: 'nothing more to say here',
          company: 'cypress',
          start_date: '04-2020',
          end_date: '2021-test',
          currently: false
        },
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(400)
          expect(response.body.message).to.eq('Date format is wrong, try (yyyy-mm)')
        })
    })
    it('should return error 400 because we are trying to add a work experience with blank job name', () => {
      cy.request({
        method: 'POST',
        url: 'work_experience/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          job_name: ' ',
          description: 'nothing more to say here',
          company: 'cypress',
          start_date: '2021-04',
          end_date: '2021-05',
          currently: false
        },
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(400)
          expect(response.body.message).to.eq('Job name cannot be blank')
        })
    })
    it('should return error 400 because we are trying to add a work experience with start year bigger than end year', () => {
      cy.request({
        method: 'POST',
        url: 'work_experience/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          job_name: 'cypress test',
          description: 'nothing more to say here',
          company: 'cypress',
          start_date: '2021-04',
          end_date: '2020-05',
          currently: false
        },
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(400)
          expect(response.body.message).to.eq('Start date cannot be posterior than end date')
        })
    })
    it('should return error 400 because we are trying to add a work experience with start month bigger than end month and same year', () => {
      cy.request({
        method: 'POST',
        url: 'work_experience/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          job_name: 'cypress test',
          description: 'nothing more to say here',
          company: 'cypress',
          start_date: '2021-05',
          end_date: '2021-04',
          currently: false
        },
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(400)
          expect(response.body.message).to.eq('Start date cannot be posterior than end date')
        })
    })
    it('should return error 400 because we are trying to add a work_experience with a month bigger than 12', () => {
      cy.request({
        method: 'POST',
        url: 'work_experience/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          job_name: 'cypress test',
          description: 'nothing more to say here',
          company: 'cypress',
          start_date: '2021-13',
          end_date: '2021-23',
          currently: false
        },
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(400)
          expect(response.body.message).to.eq('Dates need to be between months 1 and 12')
        })
    })
    it('should return error 400 because we are trying to add a work experience with a start year less than 1900 and a end year bigger than 2100', () => {
      cy.request({
        method: 'POST',
        url: 'work_experience/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          job_name: 'cypress test',
          description: 'nothing more to say here',
          company: 'cypress',
          start_date: '1750-04',
          end_date: '2100-12',
          currently: false
        },
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(400)
          expect(response.body.message).to.eq('Dates need to be between years 1900 and 2100')
        })
    })
    it('should return a message confirming that the work experience with id 2 of the user lordsergi has been deleted', () => {
      cy.request({
        method: 'POST',
        url: 'delete_work_experience/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          id: 2
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body.message).to.eq('Work experience with id [2] deleted')
        })
    })
  })
})
