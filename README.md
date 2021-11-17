# Grup F2 de ES 2021 - JOBIFY (codename Gripau)
![logo](vue-gripau/src/assets/logo.svg)
## API documentation
The documentation is built on every push to dev

Link to the documentation: [https://ub-es-2021-f2.github.io/gripau/resources/index.html](https://ub-es-2021-f2.github.io/gripau/resources/index.html) 
## Workflow Guide
### How to start working on a task
1. **Pick one of your assigned tasks** in the current sprint
2. Create a **new issue** in the Github repository.
3. The **title** of the issue has to start with *US#X* where *X* is the user story the task belongs to.
    - Example Title *"US#E.1 Add register validations in backend"*.
4. **Assign yourself** to the issue.
5. **Label the task** (frontend, backend, qa, devops...).
6. **Add the issue to the project** "Tasks".
7. **Add the issue to the milestone** that matches the current sprint (for example Sprint 2).
8. **Add a description** that may contain:
	- Initial time assigned to the task.
	- Detailed explanation of the functionality to implmenent.
	- Criteria for the reviewer/QA to check and verify.
9. **Submit the issue.**
10. Go into the "Tasks" kanban (Github repository -> Projects -> Tasks) and **move your newly created issue to the "In Progress" column**.
11. **Create a new branch from the branch "dev"** and name it "issue#N" where N is the number of the issue you just created.
12. **Checkout the new branch** in your local repository and start working in your task.
### What to do once you are done with your task

1. **Pull changes from the branch *dev*** to your issue branch (*issue#X*) and make sure that the implemented functionality still works
2. **Create a new Pull Request** from your branch *issue#X* to *dev*.
3. **Add at least 1 reviewer** to the pull request (it is recomended that you add a team member that has the same role as you).
4. **Link the pull request to the issue** you created at the begining.
5. **Update the issue's description** with the final amount of time it took to complete it.
6. (OPTIONAL) Assign yourself to the pull request.
7. (OPTIONAL) Label the pull request.
   
**DO NOT ADD THE PULL REQUEST TO THE PROJECT "TASKS" (KANBAN) OR THE SPRINT MILESTONE.**

7. **Wait for the Pull Request to be reviewed**.
8. If the review was satisfactory and there are no additional changes required, **merge the pull request**.
9. (RECOMENDED) Check that after merging the implemented functionalty works fine in the *dev* branch
10. **Close the issue** and make sure that the issue is now in the *Merged* column in the *Tasks* kanban
    
---

## How to execute the project
### Locally
1. Make sure that node packet manager (*npm*) and *python 3.X* are installed on your machine
2. Within a terminal execute the following commands from the directory  `vue-gripau` in order to build the frontend:
   1.  `npm install`
   2.  `npm run build`
3. Within a terminal execute the following commands from the directory `flask-gripau` in order to configure and start the backend server
   1. `pip install -r requirements.txt`
   2. `flask db init`
   3. `flask db migrate`
   4. `flask db upgrade`
   5. `python app.py`
   6. `python add_data.py`


### Deploy
1. Create a new PR from your changes in *dev* branch to *production* branch
2. Merge the PR
3. After the new changes are added, the new version should be deployed automatically to [ub-jobify.herokuapp.com](ub-jobify.herokuapp.com) (it may take a minute), you can check the progress and the outcome on the *Actions* tab of the Github repo

This is what is automatically performed when a commit is submited to the *production* branch.
- Local API URL is replaced by Production API URL on `vue-gripau/src/index.js`.
- The frontend project is built using `npm run build`.
- The project is pushed to heroku.
---

## How to test the project
Tests on the project are run on every PR to dev. You can run this tests manually in Actions > Docs > Manual Dispatch