# Grup F2 de ES 2021 - JOBIFY (codename Gripau)
![logo](vue-gripau/src/assets/logo.svg)
## Workflow Guide
### How to start working on a task
1. **Pick one of your assigned tasks** in the current sprint
2. Create a **new issue** In the Github repository.
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
1. **Create a new Pull Request** from your branch *issue#X* to *dev*.
2. **Add at least 1 reviewer** to the pull request (it is recomended that you add a team member that has the same role as you).
3. **Link the pull request to the issue** you created at the begining.
4. **Update the issue's description** with the final amount of time it took to complete it.
5. (OPTIONAL) Assign yourself to the pull request.
6. (OPTIONAL) Label the pull request.
   
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


### Deploy (comming soon)
1. Create a new PR from your changes in *dev* branch to *production* branch
2. After the new changes are added, the new version should be deployed automatically to [ub-jobify.herokuapp.com](ub-jobify.herokuapp.com)

---

## How to test the project (comming soon)