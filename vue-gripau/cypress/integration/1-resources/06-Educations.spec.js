// 06-Educations.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

describe('Educations resource', () => {
  before(() => {
    cy.login_jobseeker()
    cy.saveLocalStorage()
  })
  beforeEach(() => {
    cy.restoreLocalStorage()
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
    it('should return the education added to the user lordsergi', () => {
      cy.request({
        method: 'POST',
        url: 'education/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          title: 'education test cypress',
          institution: 'universitat de barcelona',
          start_date: '2021-04',
          end_date: '2021-05',
          currently: false
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body.education.username).to.eq('lordsergi')
          expect(response.body.education.title).to.eq('education test cypress')
        })
    })
    it('should return error 400 because we are trying to add a education to another user', () => {
      cy.request({
        method: 'POST',
        url: 'education/cytest',
        auth: {username: localStorage.getItem('token')},
        body: {
          title: 'education test cypress',
          institution: 'universitat de barcelona',
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
    it('should return error 400 because we are trying to add start-date in a wrong date format (mm-yyyy)', () => {
      cy.request({
        method: 'POST',
        url: 'education/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          title: 'prova cytest',
          institution: 'universitat de barcelona',
          start_date: '04-2021',
          end_date: '2021-test',
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
    it('should return error 400 because we are trying to add a education with blank title', () => {
      cy.request({
        method: 'POST',
        url: 'education/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          title: ' ',
          institution: 'universitat de barcelona',
          start_date: '2021-04',
          end_date: '2021-05',
          currently: false
        },
        failOnStatusCode: false
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(400)
          expect(response.body.message).to.eq('Title cannot be blank')
        })
    })
    it('should return error 400 because we are trying to add a education with start year bigger than end year', () => {
      cy.request({
        method: 'POST',
        url: 'education/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          title: 'education test cypress',
          institution: 'universitat de barcelona',
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
    it('should return error 400 because we are trying to add a education with start month bigger than end month and same year', () => {
      cy.request({
        method: 'POST',
        url: 'education/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          title: 'education test cypress',
          institution: 'universitat de barcelona',
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
    it('should return error 400 because we are trying to add a education with a month bigger than 12', () => {
      cy.request({
        method: 'POST',
        url: 'education/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          title: 'education test cypress',
          institution: 'universitat de barcelona',
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
    it('should return error 400 because we are trying to add a education with a start year less than 1900 and a end year bigger than 2100', () => {
      cy.request({
        method: 'POST',
        url: 'education/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          title: 'education test cypress',
          institution: 'universitat de barcelona',
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
    it('should return a message confirming that the education with id 2 of the user lordsergi has been deleted', () => {
      cy.request({
        method: 'POST',
        url: 'delete_education/lordsergi',
        auth: {username: localStorage.getItem('token')},
        body: {
          id: 2
        }
      })
        .should((response) => {
          cy.log(JSON.stringify(response.body))
          expect(response.status).to.eq(200)
          expect(response.body.message).to.eq('Education with id [2] deleted')
        })
    })
  })
})
