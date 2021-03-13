[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](http://shields.io/)

![logo](/static/readme-files/nsum.png "nsum logo")

#### Code Institute - Milestone Project 3 
## Cork International Hotel Task Manager
![Am I Responsive](/static/readme-files/responsive.png)
[View the project live here](https://ms3-taskman.herokuapp.com/)
## Introduction
Welcome,
This web app is made as a 3rd Milestone Project with Code Institute.
Initially, my idea for MS3 was a job directory for IT jobs, where job seekers would input programming languages they use,
yrs of experience with each one, links to projects, desired job positions, etc. Then recruiters would be able to search and
filter candidates by certain criteria. But after talking to my colleagues from the hotel where I work,
I decided to make a task manager app because the hotel showed interest and need for an app such as this.
Before project submission, this project was copied to another repo and will be used throughout the hotel group I work in. 
Some of the features included are full CRUD functionality, specific department tasks, personal tasks, shared tasks,
management control, search and task editing...
I tried to use minimum outside help with this project, and for every issue or a new feature, I tried and managed to find a solution myself.
Code Institute's task manager mini-project was used as a sort of "base" for this project, and besides that, select.js & materializecss 
jQuery snippets are the only outside code I used. My code is far from perfect but it serves the purpose and is the best I could do given
my experience and this being my first contact with Python, Flask & MongoDB.

Research, design, development & testing of this project took a total of 85 hrs.

## Table of Contents

1. [User Experience (UX)](#user-experience)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
    - [Design](#design)

2. [Techonologies Used](#technologies-used)
    - [Languages](#languages-used)
    - [Frameworks, Libraries & Tools Used](#frameworks-libraries-tools-used)

3. [Techonologies Used](#technologies-used)
    - [Languages](#languages-used)
    - [Frameworks, Libraries & Tools Used](#frameworks-libraries-tools-used)

4. [Features](#features)
    - [Back-end](#back-end)
    - [Front-end](#front-end):
        - [Navigating The Page](#navigating-the-page)
        - [Creating & Editing Tasks](#creating-and-editing-tasks)
        - [Completing & Deleting a Task](#completing-and-deleting-a-task)
        - [Viewing Task List](#viewing-task-list)
        - [Registering New User](#registering-new-user)
        - [Personal Tasks](#personal-tasks)
        - [Tracking Delegated Tasks](#tracking-delegated-tasks)
        - [Search Bar](#search-bar)
    - [To be included in upcoming versions](#to-be-included-in-upcoming-versions)

5. [Testing](#testing)
    - [Valdators](#validators)
    - [Manual Testing Procedures](#manual-testing-procedures):
        - [Navigating The Site](#navigating-the-site)
        - [Login](#login)
        - [Logout](#log-out)
        - [Register New User](#register-new-user)
        - [Creating new task](#creating-new-task)
        - [Editing tasks](#editing-tasks)
        - [Completing the task](#completing-the-task)
        - [Deleting the task](#deleting-the-task)
        - [Testing the lists](#testing-the-lists)
    - [Unresolved Issues](#unresolved-issues)
    - [Bugs & Fixes](#bugs-and-fixes)
    - [Coding Process](#coding-process)
    - [Testing User Stories from User Experience (UX) Section](#testing-user-stories):

6. [Data Schema](#data-schema)
    - [Tasks Collection](#tasks-collection)
    - [Departments Collection](#departments-collection)
    - [Users Collection](#users-collection)

7. [Credits](#credits)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)
    - [Media](#media)

8. [Deployment](#deployment)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Making a Local Clone](#making-a-local-clone)
    - [How to run this project locally](#how-to-run-this-project-locally)
    - [Heroku Deployment](#heroku-deployment)


# User Experience
+   ### User stories
    1. As someone who would use this task manager regularly, I want tasks and lists to be informative and easily understandable.
    2. As head of the department I want to be able to assign a task that will be visible only to staff in my department and can be completed by anyone in my department.
    3. As a manager I want to be able to create a new task that will be visible to all members.
    4. As head of the department I want to be able to assign a personal task that will be visible only to me and the staff member I assigned the task to.
    5. As head of the department I want to be able to keep track of all the tasks I assigned either to the department or staff member specifically.
    6. As part of management I want to be able to delete any tasks.
    7. As part of management I want to be able to edit and redelegate tasks.
    8. As a normal staff member, I want to be able to add a personal task to myself as a reminder.
    9. As part of management I want to be able to see if someone edited a task I made, and when.
    10. As part of management I want to be able to easily see the tasks that are past due.
    11. As management I want to be able to search through department tasks and see completed tasks too.

+   ### Wireframes
    + [Index Page - Desktop](/static/readme-files/base-prelogin.png) 
    + [Admin Control Panel - Desktop](/static/readme-files/admin-cp.png) 
    + [User Tasks Page - Desktop](/static/readme-files/normal-user-home.png) 
    + [Task Creation - Desktop](/static/readme-files/task-creation.png)
    + [Task List - Desktop](/static/readme-files/tasks-list.png)
    + [User Profile - Desktop](/static/readme-files/user-profile.png)

+   ### Design
    + Colour Scheme: The main colour is purple which is the signature colour of the hotel this app will be used in.
    + MaterializeCSS classes and custom CSS were used to make the app fully responsive on all screen sizes.

# Technologies Used

### Languages Used
+   [HTML5](https://en.wikipedia.org/wiki/HTML5)
+   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
+   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
+   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks Libraries Tools Used
+ [Materializecss:](https://materializecss.com/) was used to assist with the responsiveness and styling of the website.
+ [jQuery:](https://jquery.com/) was used to initialize most of Materializecss's features and a few custom on click & hover events 
+ [Flask:](https://flask.palletsprojects.com/en/1.1.x/) Flask microframework was used for its tools, libraries, and mechanics.
+ [MongoDB:](https://www.mongodb.com/3) was used as a database program.
+ [PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project.
+ [PyMongo](https://api.mongodb.com/python/current/) to make communication between Python and MongoDB possible.
+ [Jinja](http://jinja.pocoo.org/docs/2.10/) to simplify displaying data from the backend of this project smoothly and effectively in HTML.
+ [Heroku:](https://www.heroku.com/) was used as deployment platform
+ [requirements.txt:](requirements.txt) contains list off all dependancies
+ [Randomkeygen:](https://randomkeygen.com/) was used for encrypting vars.
+ [Git:](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
+ [GitHub:](https://github.com/) is used to store the project's code after being pushed from Git.
+ [Font Awesome:](https://fontawesome.com/) was used on all pages throughout the website to add icons for aesthetic and UX purposes.
+ [Imagecompressor.com:](https://imagecompressor.com/) was used to compress images
+ [Am I Responsive:](http://ami.responsivedesign.is/) was used to create the image at the top of README.md

# Features

### Back-end
- Session expiry after set time of inactivity (set time inside set_session_timeout function) - currently at 15 mins.
- Redirects to login page if an unlogged user tries to access any of the pages login is required for by typing directly in the URL bar.
- Redirects to the home page if non-admin or non-mgmt user tries to access admin & mgmt pages by typing directly in the URL bar.
- At the moment admin and mgmt have the same privileges but that will change when the app is put to use and more users and features are added.
- Registering a new user asks to confirm the password for defensive purposes.
- When logging in, the first check performed is to see if the user exists, and if it does it then checks does the password match the one in db.
    - If either username or password us incorrect, a flash message will display saying that username AND/OR password is wrong, to prevent brute force.
- Registering new user first checks does the user already exists in db, then it checks do the two password inputs match.
    - Flash message is displayed if any of the checks fail, notifying the user (e.g. 'Passwords do not match')

### Front-end
#### Navigating The Page
- After logging in, a flash message is displayed greeting the user by name
- User's department is displayed in nav next to the site name
- admin & mgmt have floating action button with links to all important controls 
    (create new user, create department task, track delegated tasks, etc..)
    - For mobile users FAB is hidden and the links are in the side nav 
    - For non-mgmt users FAB is hidden
- Tasks view contains two separate lists. One for shared tasks and one for user's department tasks.
    Both lists are titled accordingly and are click to expand
- Profile view for normal users contains only tasks assigned to that user, while if the user is mgmt
    profile view will have cards will all the links from the floating action button with explanations.
#### Creating and Editing Tasks
- When creating a personal task, non-mgmt user doesn't have the option to choose who to assign the task to, 
    and the task is assigned to a user in session.
- mgmt users and admins can choose the name of the person to assign the personal task to.
- Department tasks can only be created by mgmt & admins. The form is the same as personal tasks, the only difference being 
    choosing department instead of a person.
- Date picker makes it easier and nicer to chose a date and then format it properly
- When a task is created, a flash message appears confirming task creation.
- If "is urgent" switch is on, there will be a yellow triangle displayed next to due date to indicate that the task is urgent.
- Editing task opens the form and sets default values same as the ones the task already had so only the value we wish to change needs to be altered.
- After editing the task new keys/values are inserted logging who and when updated the task
#### Completing and Deleting a Task
- Both Complete & Delete task buttons have modals as defensive programming, asking the user to confirm the action.
- Completing the task doesn't delete it but rather updates it with new key/value pairs indicating the task was completed
- Deleting the task deletes the record completely
- On all actions (edit, delete, complete, create) flash message is displayed confirming that the user's action was completed
#### Viewing Task List
- Every list contains:
    - task name
    - task description
    - created by
    - created on
    - urgency status
- If the task has been edited, additionally there will be:
    - updated by
    - updated on
- Completed tasks will be shown only on all_tasks view which will list all departmental tasks, ongoing and completed.
    Completed tasks will have a green checkmark next to the task name and will have completed by and completed on values.
- If the ongoing task due date is today or in the past, a red triangle will display next to the task name to indicate that the task is due.
#### Registering New User
- Admin and mgmt users can register new user. Username field uses .lower() while first and last name uses .capitalize().
    Repeat password feat is there to confirm inputted password, and then the password is displayed as a flash message after registering.
#### Personal Tasks
- Admins & mgmt can assign personal tasks to other users, while normal users can only assign to themselves.
    Personal tasks are visible only to users who assign the task and to user that task is assigned to.
#### Tracking Delegated Tasks
- track_delegated_tasks is available to admin & mgmt users and it contains a list of both personal and departmental 
    tasks either created or edited by the current user. 
#### Search bar
- Search bar is available on all_tasks view where all completed and uncompleted departmental tasks are.
    It searches for a task name or task description, and any result will show in the task list below the search bar.

### To be included in upcoming versions
- More extensive search option where admin & mgmt users will be able to filter tasks completed by a specific user.
- Table showing "Monthly targets" will be included and visible to front office members to keep track of current months' targets.
- Optional extra key of "complete_note" (text type) will be inserted on completing the task. Users will be prompted to optionally
    write a note before completing the task.
- At the moment after creating or editing a task users are redirected to profile view instead of back where they were.
    I plan to fix that as soon as I find a viable solution. (more info in issues section)
- Recurring tasks functionality, where there will be an option for daily, weekly & monthly tasks. e.g. after the daily task is completed,
    when the user clicks on complete, that task will be marked as finished and a new copy of the task will be created with same values
    except new due date which would be set to day after (weekly would be set to week from now etc..)

# Testing

### Validators
#### Number of validators and services were used to validate pages to ensure there were no syntax errors:
-   [Extend Class - Python Syntax Schecker](https://extendsclass.com/python-tester.html) - [Results](/static/readme-files/validate-python.png)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](/static/readme-files/validate-css.png)
-   [Esprima jQuery Validator](https://esprima.org/demo/validate.html) - [Results](/static/readme-files/validate-jquery.png)
-   [Lighhouse Tool](https://developers.google.com/web/tools/lighthouse) - [Results](/static/readme-files/lighthouse-report.png)
-   [W3C HTML Validator](https://validator.w3.org/nu/):  
        - [Home](/static/readme-files/home.png)  
        - [Login](/static/readme-files/login.png)  
        - [All Tasks](/static/readme-files/all-tasks.png)  
        - [Create Task](/static/readme-files/create-task.png)  
        - [Profile](/static/readme-files/profile.png)  
        - [Register](/static/readme-files/register.png)  
        - [Tasks](/static/readme-files/tasks.png)  
        - [Track Assigned Tasks](/static/readme-files/track-tasks.png)  
        - [Edit Task](/static/readme-files/edit-task.png)  

### Manual Testing Procedures

- #### Navigating The Site
    - Browsing  as an unlogged user:
        - Expected: only home & login links available 
        - Testing: visited site as unlogged user
        - Result: expected results
    - Typing directly in the URL bar as unlogged or non-admin user:
        - Expected: before the user is logged in if he tries to type in views directly in URL bar, he is redirected
            to the login page. If the user is logged in but not part of mgmt or admin and tries to do the same, he will
            be redirected to the home page
        - Testing: Tried to type in directly in URL bar as both logged in and logged out.
        - Result: Expected results on all views except 'search' which returns pymongo error for both logged and unlogged users.
    - Browsing as non-admin user:
        - Expected: floating action buttons, admin controls, and admin mobile controls to be hidden and inaccessible
        - Testing: logged in as normal user and browsed the site 
        - Result: got expected results. None of the controls are visible to normal user
    - Browsing as 'admin' or 'mgmt':
        - Expected: Profile page to have cards with admin controls, desktop size to have floating action buttons, 
            mobile to have those buttons in side nav and FAB hidden.
        - Testing: Logged in as admin on both desktop & mobile and browsed the site
        - Result: got expected results
- #### Login
    - If either username or password is incorrect:
        - Expected: redirect back to login and flash message "Incorrect Username and/or Password"
        - Testing: tried inputting just wrong username, just wrong password, and tried both wrong password and username
        - Result: got expected results on all tries
    - If both username and password are correct:
        - Expected: store a session cookie, redirect to user's profile page and 
            flash message displayed "Welcome, 'user's first name'"
        - Testing: inputted correct username & password
        - Result: got expected results
- #### Log out
    - Log the user out by clicking 'Log Out' button:
        - Expected: redirect back to login page and delete the current session cookie
        - Testing: while logged in, clicking on 'Log Out' button
        - Result: expected result
    - Log out after a set time of inactivity:
        - Expected: redirect back to login page and delete current session cookie, if user
            comes back after set time of inactivity (15 minutes)
        - Testing: logged in and left the page for 15 minutes. After that tried to navigate the page.
        - Result: Got expected result, redirected back to login page.
- #### Register New User
    - Create a new user:
        - Expected: if all inputs are valid, insert a new record in 'users' collection in db, and flash message 
            that user was created successfully and flash message new user's password
        - Testing: input valid information and click register
        - Result: got expected results
    - Passwords do not match:
        - Expected: If 'password' and 'repeat password' do not match exactly, flash 'Passwords Do Not Match'
            and return to the registration page
        - Testing: Input all correct values except input two different passwords and click submit
        - Result: got expected results
    - Any of the fields left blank:
        - Expected: form to warn that field is required and to please fill it in
        - Testing: tried leaving just one field empty at a time, tried leaving all fields empty, tried leaving empty pairs
        - Result: got expected results on each try
    - Min / max chars:
        - Expected: If any of the inputs are to short or too long, form should warn the user
        - Testing: tried inputting less than min chars, tried inputting more than max, on all the fields
        - Result: If user reaches max number of chars set for each field, no more input will be registered.
            If user types less than min number of chars set for each field, the form warns the user to match the requested format.
    - Mobile View Icon:
        - Expected: font awesome icon next to last name field to appear on mobile devices but stay hidden on large
        - Testing: tried creating new user on both mobile & desktop
        - Result: got expected results
    - Capitalization:
        - Expected: username to be saved in all smaller letters & first and last name to be capitalized
        - Testing: input many different variations for all username, first & last name while creating new user
        - Result: got expected result on every try
- #### Creating new task
    - Successful creation of task:
        - Expected: If all the fields are inputted correctly, the task should be inserted into db, 
            user should be redirected and a flash message displayed confirming that task was created
        - Testing: Tried creating both personal & departmental tasks on both mobile & desktop 
        - Result: got expected results
    - If any of the criteria for task creation is not met:
        - Expected: user to be notified and redirected and task not inserted in db
        - Testing: tried inputting less than min char, more than max, leaving fields blank, inputting text/numbers
            into date field
        - Results: got expected results on all tries except when the user tabs from task description to date picker. 
            Date picker doesn't trigger and the user can input anything he wants. I've fixed it by checking if the format is 
            correct, and if it isn't user will be redirected a step back and flash message will warn him to format the date properly.
    - Refreshing the page after creating or editing task:
        - Expected: page to refresh normally
        - Testing: created a task and then refreshed the page
        - Result: at first I was returning users to profile page which prompted browser to resubmit the form on refresh.
            Fixed it by redirecting to tasks view instead of 'return profile(session["user"])'
- #### Editing tasks
    - Task successfully edited:
        - Expected: flash the message that task was successfully edited, update the task in db, show 'updated_by' & 'updated_on' under task description
        - Testing: tried editing both personal and department task
        - Result: got expected results
    - If any of the criteria for task creation is not met:
        - Expected: user to be notified and redirected and task not inserted in db
        - Testing: tried inputting less than min char, more than max, leaving fields blank, inputting text/numbers
            into date field
        - Results: got expected results on all tries except when user tabs from task description to date picker. 
            Date picker doesn't trigger and user can input anything he want's. I've fixed it by checking if the format is 
            correct, and if it isn't user will be redirected a step back and flash message will warn him to format the date properly.
- #### Completing the task
    - Clicking complete the task:
        - Expected: Modal to pop and ask the user to confirm the action. If cancel is clicked, close the modal, but if complete 
            is clicked then flash that task was completed & update the task with new keys/values 
            (completed_on, completed_by, completed_by_label & completed(true))
        - Testing: Tried both cancel and complete task on both personal tasks and department tasks in all views
        - Result: got expected results
    - Refreshing the page before clicking:
        - Expected: Modal to close and page to be refreshed
        - Testing: clicked on 'Done' for modal to open then refreshed the page
        - Result: got expected result
    - Clicking outside modal area:
        - Expected: Modal to be closed as 'cancel' button was pressed
        - Testing: clicked 'done' to open modal then clicked outside modal area
        - Result: got expected results
- #### Deleting the task
     - Clicking delete the task:
        - Expected: modal to open asking user to confirm the action. If canceled close the modal, but if confirmed then 
            flash message that task was deleted and delete the task from db
        - Testing: tried both cancel and delete buttons on personal & department tasks in all views
        - Result: got expected results
- #### Testing the lists
    - Viewing empty task lists:
        - Expected: If any of the lists are empty, display small heading under the task list 
            informing the user that there are no active tasks
        - Testing: Tried completing & deleting tasks to empty the lists
        - Result: Had issues on 'track_delegated_tasks' view so I 
            removed that 'else' jinja statement, and nothing will show if the list is empty

    - Viewing lists as non-admin user:
        - Expected: 
            - Three lists to be visible to users (department, shared, personal). 
            - All lists to be hidden by default until 'Show/Hide' button is clicked
            - If user didn't create the task, then 'edit' & 'delete' buttons for each task should not be visible
            - Lists to contain task name, due date, urgency status (fa icon) & lateness status(fa icon)
            - When clicking on any of the tasks, to expand and show additional information about the task
                (description, created by, created on, etc..)
            - Completed tasks, tasks created for other departments or other people should not be visible
        - Testing: Tested extensively all three lists with multiple usernames
        - Result: got expected results
    - Viewing delegated tasks lists & all departments tasks list as admin:
        - Expected: 
            - To be able to complete, edit, and delete any of the tasks on any of the lists
            - On lists that have mixed personal and department tasks to be able to distinguish between the two
            - On lists that contain completed tasks, fa icon to indicate that task is completed, and to be able to see
                when it was completed and by who.
        - Testing: tested both lists with multiple usernames
        - Result: got expected results 

### Unresolved Issues
- When creating or editing a task sometimes the date picker doesn't trigger on click but rather 
    enables the user to manually input values. It also happens every time when user tabs from task description to due_date. 
    due_date used to be text format so it would save the input, but I changed due_date
    to save as date format so if by any chance wrong format is inputted, the user is redirected back and a flash message is displayed.
- After creating or editing a task user is redirected to view set by a return of performed function instead of being redirected 
    back where he was. I tried including 'onclick="history.go(-1); return false;"' in buttons which worked as far as redirect 
    goes, but it didn't create or update the task. I also tried returning redirect('request.referrer') which did save the task and it
    did in fact redirect but back to task creation or task editing, instead of page before it. 

### Bugs and Fixes
- All html files except base.html throw warning "Doctype must be declared first."
    - It is ignored because all html files are injected into base.html and it's Doctype is declared.
- `edit_dept_task` has two identical `id`'s in switches.
    - It can be ignored because it's in if-else loop and only one id is used.
- `login_required` decorator was throwing an error instead of 
    redirecting when unlogged users tried to access restricted pages,
    because I used `if session["user"] is None`.
    - Fixed by using: `is_logged = session.get("user")` in:
        `if is_logged is None: ...`
- There was a bug on mobile (specifically IOS) where when you click on item in dropdown select list, 
    wrong item gets selected. Also dropdown caret is positioned wrong.
    - Fixed by adding Alvin Wang's `select.js` file to scripts (full credit in 'Credits')
- Date picker sometimes on click doesn't trigger date picker and allows manual entry.
    It also happens every time when user tabs from task description to date picker.
    - Didn't find a way to fix it, but I added try/except where `try` tries to format input as date, and 
    if it fails user is redirected back to task create/edit and flash message is displayed warning that
    date format was wrong.
- Had to refactor tasks list half-way through the project after adding `slideToggle` click event to `ul`.
    Idea was for tasks to be hidden until "show tasks" button was clicked. It would then show 
    collapsable `li` of tasks, but it didn't work until I reorganized divs and li's a lot to make it work.
- Half-way through the project I noticed `created_by` & `created_on` labels changed to editors information 
    after editing tasks. Fixed by using `$set` syntax, which enabled to update just given values. 
    All other non-provided values on editing (like created_by, created_on) stay the same.
- Had a bug with modals just after implementing them to pop to confirm deletion of a task. 
    Modals would open only for first task which I fixed by moving modal structure outside of collapsible body.
    That fixed modals opening for just first item in the list but still if I try to delete e.g. 5th
    task in the list, first task in the list would be deleted. It was because of modals id's so 
    I fixed it by using `#modal1{{ loop.index }}` for first list, `#modal2{{ loop.index }}` for second etc.
- I decided to use Materialize floating action button to show control view links like 'register new user',
    'view all tasks', 'assign personal tasks' etc. It worked fine on desktop but there were minor issues on mobile. 
    Button's tooltips sometime wouldn't dissapear automatically but would stay until refreshed, and it was hard to 
    intuitively know what buttons do without hovering and seeing tooltips text, so I disabled FAB on mobile and 
    put links in mobile side nav instead.
- Near the end of the project I wanted to compare today's date to due_date in order to mark all tasks that are past due.
    Up until then, dates were saved in string format, so I refactored views to save in date format, and then using jinja
    compared today to `due_date`.
- Above changes brought small issue when editing task. If date wasn't changed when editing, there was a formatting issue,
    as time data didn't match the format. Fixed it by adding `.strftime('%d/%b/%Y')` to date values when editing task.
- Had issues on 'track_delegated_tasks' view because of jinja was comparing `task.completed != True`,
    but none of the tasks had `false` because task.completed was created and inserted on task completion. 
    So if the list was empty it should show "All Tasks You Delegated Have Been Completed" div, but it didn't.
    Fixed by adding `completed` key and giving it the value of `false` when task is created.

### Coding Process
- Initially I set up two collections for tasks: `tasks` for department tasks, and `personal` 
    for personal tasks, because I wasn't sure will I be able to manage it in one colelction.
    After learning how to manage it, I refactored code to use one collection `tasks` for 
    both personal and department tasks.
- I decided to use Materialize as a front-end Framework, because it's a new framework for me,
    and wanted to get more familiar with it.
- Towards the end of the project I decided to get rid of `control` view which had it's access limited to admins and mgmt, 
    and contained links for creating new user, creating new tasks, tracking tasks etc.
    I decided to put those links in floating action button on dekstop, and on mobile put it in mobile view side nav.
- Also towards the end of the project, after consulting with my mentor, I decided to use just one collection for tasks. 
    Until then I had `tasks` & `completed_tasks` which I then merged into one collection.



### Testing User Stories
- #### As someone who would use this task manager regurarly, I want tasks and lists to be informative and easily understandable.
    - Task lists contain list items with: task name, due date & urgency status.
On opening specific task: task description, created by, created on are visible, under which is complete button. 
Additionally if someone edits the task, that is also visible in task body.
- #### As head of the department I want to be able to assign a task that will be visible only to staff in my department and can be completed by anyone in my department.
    - Normal users can see and complete tasks assigned to their department on tasks page.
- #### As a manager I want to be able to create a new task that will be visible by all members.
    - "Shared" tasks list contains all tasks that will be visible to every member.
- #### As head of the department I want to be able to assign a personal task that will be visible only to me and staff member I assigned the task to.
    - Normal users can see and complete their own personal tasks assigned to them by management or themselves.
- #### As head of the department I want to be able to keep track of all the tasks I assigned either to department or staff member specifically.
    - All management members can access all tasks from "control panel" page, and additionaly they have a list of all 
tasks assigned by them.
- #### As part of the management I want to be able to delete any tasks.
    - Management can delete any task, while normal users can only delete tasks create by themselves (own personal task)
- #### As part of the management I want to be able to edit and redelegate tasks.
    - All management members can edit all tasks while normal users can only edit tasks they created. When editing they can reassign the task to other staff member or department.
- #### As a normal staff member, I want to be able to add a personal task to myself as a reminder.
    - Normal users can only create personal tasks for themselves, and those tasks are the only tasks they can edit or delete.
- #### As part of the management I want to be able to see if someone edited a task I made, and when.
    - When task is edited new keys (edited by, edited on) are inserted into task and shown in task body after editing so it's easy to keep track of who edited the task and when.
- #### As part of the management I want to be able to easily see the tasks that are past due.
    - All task lists are sorted by due date, and for every task comparison is made to see if due date is in the past. If due date is today or before, red triangle "Task Due!" is displayed next to the task name.
- #### As management I want to be able to search through deparment tasks and see completed tasks too.
    - all_tasks view has search function and it's list contains all department tasks both completed and uncompleted.

# Data Schema 

- #### Tasks Collection
    `_id`: ID,  
    `type`:"personal" or "departmental" depending on the task type  
    `assigned_to`:"username" if task is personal, or "none" if it's departmental  
    `department`:"none" if task is personal, 'department name' if task is departmental  
    `task_name`:"task name",  
    `task_description`:" task description",  
    `is_urgent`:"off" or "on" depending on input,  
    `due_date`:{"$date":{"$numberLong":"1616716800000"}},  
    `created_by`:"username",  
    `creator_label`:"full name",  
    `created_on`:{"$date":{"$numberLong":"1615351083289"}},  
    `completed`:true or false boolean depending on whether is the task completed or not,  
    `updated_by`:"username",  
    `updated_on`:{"$date":{"$numberLong":"1615351131768"}},  
    `updator_label`:"full name",  
    `completed_by`:"username",  
    `completed_by_label`:"full name",  
    `completed_on`:{"$date":{"$numberLong":"1615351139524"}}  

- #### Departments Collection
    `_id`: ID,  
    `department_name`: "department name", e.g. "fo"  
    `department_label`: "full department name" e.g. "Front Office"  

- #### Users Collection
    `_id`: ID,  
    `username`: "username",  
    `password`: "pbkdf2:sha256:password",  
    `first_name`: "Name",  
    `last_name`: "Last name",  
    `department`: "department name",  
    `super_user`: "on" or "off" depending on user privileges,  
    `admin`: "on" or "off" depending on user privileges,  
    `mgmt`: "on" or "off" depending on user privileges,  

# Credits

### Code
+	[Alvin Wang](https://github.com/Dogfalo) - `select.js` which solves the issue with form select on mobile

### Acknowledgements
+   [Spencer Barriball](http://www.5pence.net/) - Huge thank you to my mentor Spencer for all his help and guidance
+   [codeinstitute.net](https://codeinstitute.net/) - Lessons, videos, tutoring & support
+   [Cork International Hotel](https://www.corkinternationalairporthotel.com/) - For showing interest in using this app
+   [Anna Greaves](https://github.com/AJGreaves) - For README.md Heroku deployment section
+   [Code Institute Sample README](https://github.com/Code-Institute-Solutions/SampleREADME) - Readme Template

### Media
+	[Parallax Image 1](https://cf.bstatic.com/images/hotel/max1024x768/653/65346226.jpg)
+	[Parallax Image 2](https://www.corkinternationalairporthotel.com/wp-content/uploads/2019/07/lobby-003.jpg)

# Deployment

### Forking the GitHub Repository
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone
1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) 
    to retrieve pictures for some of the buttons and more detailed explanations of the above process.

### How to run this project locally
To run this project on your own IDE follow the instructions below:
Ensure you have the following tools: 
- An IDE such as [Visual Studio Code](https://code.visualstudio.com/)

The following **must be installed** on your machine:
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
- An account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) or MongoDB running locally on your machine. 
    - How to set up your Mongo Atlas account [here](https://docs.atlas.mongodb.com/).

#### Instructions
1. Save a copy of the github repository located at https://github.com/nsum/ms3-hotel-task-manager by clicking 
the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.
```
git clone https://github.com/nsum/ms3-hotel-task-manager
```

2. If possible open a terminal session in the unzip folder or cd to the correct location.

3. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. Enter the command:
```
python -m .venv venv
```  
_NOTE: Your Python command may differ, such as python3 or py_

4. Activate the .venv with the command:
```
.venv\Scripts\activate 
```
_Again this **command may differ depending on your operating system**, please check the [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html) for further instructions._

4. If needed, Upgrade pip locally with
```
pip install --upgrade pip.
```

5. Install all required modules with the command 
```
pip -r requirements.txt.
```

6. In your local IDE create a file called `.env.py`.

7. Inside the .env file, create a SECRET_KEY variable and a MONGO_URI to link to your own database. 

8. You can now run the application with the command
```
python app.py
```

9. You can visit the website at `http://127.0.0.1:5000`

### Heroku Deployment

To deploy this app to heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`
PORT | 5000
SECRET_KEY | `<your_secret_key>`

- To get you MONGO_URI read the MongoDB Atlas documentation [here](https://docs.atlas.mongodb.com/)

8. In the heroku dashboard, click "Deploy".

9. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

10. The site is now successfully deployed.