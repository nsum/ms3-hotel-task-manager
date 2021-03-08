[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](http://shields.io/)

![logo](/static/readme-files/nsum.png "nsum logo")

#### Code Institute - Milestone Project 3 
## Cork International Hotel Task Manager
![Am I Responsive](/static/readme-files/responsive.png)

## Introduction
Welcome,
This web app is made as 3rd Milestone Project with Code Institute.
Initially my idea for MS3 was job directory for IT jobs, where job seekers would input programming languages they use,
yrs of experience with each one, links to projects, desired job positions etc. Then recruiters would be able to search and
filter candidates by certain criterias. But after talking to my colleagues from hotel where I work,
I decided to make a task manager app because hotel showed interest and need for an app such as this.
Before project submission this project was copied to another repo and will be used throughout the hotel group I work in. 
Some of the features included are: full CRUD functionality, specific department tasks, personal tasks, shared tasks,
management control, search and task editing...

Research, design, development & testing of this project took total of 85 hrs.

# User Experience (UX)

+   ### User stories:
1. As someone who would use this task manager regurarly, I want tasks and lists to be informative and easily understandable.
2. As a head of department I want to be able to assign a task that will be visible only to staff in my department and can be completed by anyone in my department.
3. As a manager I want to be able to create a new task that will be visible by all members.
4. As a head of department I want to be able to assign a personal task that will be visible only to me and staff member I assigned the task to.
5. As a head of department I want to be able to keep track of all the tasks I assigned either to department or staff member specifically.
6. As part of management I want to be able to delete any tasks.
7. As a part of management I want to be able to edit and redelegate tasks.
8. As a normal staff member, I want to be able to add a personal task to myself as a reminder.
9. As a part of management I want to be able to see if someone edited a task I made, and when.
10. As a part of management I want to be able to easily see the tasks that are past due.
11. As management I want to be able to search through deparment tasks and see completed tasks too.

+   ### Wireframes:
    + [Index Page - Desktop](/static/readme-files/base-prelogin.png) 
    + [Admin Control Panel - Desktop](/static/readme-files/admin-cp.png) 
    + [User Tasks Page - Desktop](/static/readme-files/normal-user-home.png) 
    + [Task Creation - Desktop](/static/readme-files/task-creation.png)
    + [Task List - Desktop](/static/readme-files/tasks.png)
    + [User Profile - Desktop](/static/readme-files/user-profile.png)

+   ### Design:
    + Colour Scheme: Main colour is purple which is the signature colour of the hotel this app will be used in.
    + MaterializeCSS classes and custom css were used to make app fully responsive on all screen sizes.



# Technologies Used

### Languages Used:
+   [HTML5](https://en.wikipedia.org/wiki/HTML5)
+   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
+   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
+   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used:
+ [Materializecss:](https://materializecss.com/) was used to assist with the responsiveness and styling of the website.
+ [jQuery:](https://jquery.com/) was used to initialize most of Materializecss's features and few custom on click & hover events 
+ [Flask:](https://flask.palletsprojects.com/en/1.1.x/) Flask micro framework was used for it's tools, libraries, and mechanics.
+ [MongoDB:](https://www.mongodb.com/3) was used as a database program.
+ [Heroku:](https://www.heroku.com/) was used as deployment platform
+ [requirements.txt:](requirements.txt) contains list off all dependancies
+ [Randomkeygen:](https://randomkeygen.com/) was used for encrypting vars.
+ [Git:](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
+ [GitHub:](https://github.com/) is used to store the projects code after being pushed from Git.
+ [Font Awesome:](https://fontawesome.com/) was used on all pages throughout the website to add icons for aesthetic and UX purposes.
+ [Imagecompressor.com:](https://imagecompressor.com/) was used to compress images
+ [Am I Responsive:](http://ami.responsivedesign.is/) was used to create image at the top of README.md


# Features

### Back End:
- Session expiry after set time of inactivity (set time inside set_session_timeout function) - currently at 15 mins.
- Redirects to login page if unlogged user tries to access any of the pages login is required for by typing directly in URL bar.
- Redirects to home page if non-admin or non-mgmt user tries to access admin & mgmt pages by typing directly in URL bar.
- At the moment admin and mgmt have same privileges but that will change when app is put to use and more users and features are added.
- Registering new user asks to confirm the password for defensive purposes.
- When logging in, first check performed is to see if the user exists, and if it does it then checks does the password match the one in db.
    - If either username or password are incorrect, flash message will display saying that username AND/OR password is wrong, to prevent brute forcing.
- Registering new user first checks does the user already exist in db, then it checks do the two passwod inputs match.
    - Flash message is displayed if any of the checks fail, notifying the user (e.g. 'Passwords do not match')

### Front End:
#### Navigating The Page:
- After logging in, flash message is displayed greeting user by name
- User's department is displayed in nav next to site name
- admin & mgmt have floating action button with links to all important controls 
    (create new user, create department task, track delegated tasks, etc..)
    - For mobile users FAB is hidden and the links are in the side nav 
    - For non mgmt users FAB is hidden
- Tasks view contains two separate lists. One for shared tasks and one for user's department tasks.
    Both lists are titled accordingly and are click to expand
- Profile view for normal users contains only tasks assigned to that user, while if the user is mgmt
    profile view will have cards will all the links from floating action button with explanations.
#### Creating & Editing Tasks:
- When creating personal task, non mgmt user doesn't have the option to choose who to assign the task to, 
    and the task is assigned to user in session.
- mgmt users and admins can choose the name of the person to assign the personal task to.
- Department tasks can only be created by mgmt & admins. Form is the same as personal tasks, only difference being 
    choosing department instead of person.
- Date picker makes it easier and nicer to chose date and then format it properly
- When task is created, flash message appears confirming task creation.
- If "is urgent" switch is on, there will be yellow triangle displayed next to due date to indicate that task is urgent.
- Editing task opens form and sets default values same as the ones task already had so only value we wish to change needs to be altered.
- After editing the task new keys/values are inserted logging who and when updated the task
#### Completing & Deleting a Task:
- Both Complete & Delete task buttons have modals as defensive programming, asking user to confirm action.
- Completing the task doesn't delete it but rather updates it with new key/value pairs indicating the task was completed
- Deleting the task deletes the record completely
- On all actions (edit, delete, complete, create) flash message is displayed confirming that user's action was completed
#### Viewing Task List:
- Every list contains:
    - task name
    - task description
    - created by
    - created on
    - urgency status
- If the task has been edited, additionaly there will be:
    - updated by
    - updated on
- Completed tasks will be shown only on all_tasks view which will list all departmental tasks, ongoing and completed.
    Completed tasks will have green check mark next to task name and will have completed by and completed on values.
- If the ongoing task due date is today or in the past, red triangle will display next to the task name to indicate that task is due.
#### Registering New User:
- Admin and mgmt users can register new user. Username field uses .lower() while first and last name uses .capitalize().
    Repeat password feat is there to confirm inputed password, and then password is displayed as flash message after registering.
#### Personal Tasks:
- Admins & mgmt are able to assign personal tasks to other users, while normal users can only assign to themselves.
    Personal tasks are visible only to users who assign the task and to user that task is assigned to.
#### Tracking Delegated Tasks:
- track_delegated_tasks is available to admin & mgmt users and it contains a list of both personal and departmental 
    tasks either created or edited by current user. 
#### Search bar:
- Search bar is available on all_tasks view the all completed and uncompleted departmental tasks are.
    It searches for task name or task description, and any result will show in the task list below the search bar.

### To be included in upcoming versions:
- More extensive search option where admin & mgmt users will be able to filter tasks completed by specific user.
- Table showing "Monthly targets" will be included and visible to front office members to keep track of current months targets.
- Optional extra key of "complete_note" (text type) will be inserted on completing the task. Users will be prompted to optionally
    write a note before completing the task.
- At the moment after creating or editing a task users are redirected to profile view instead of back where they were.
    I plan to fix that as soon as I find a viable solution. (more info in issues section)

# Credits

### Code:
+	[Alvin Wang](https://github.com/Dogfalo) - select.js which solves the issue with form select on mobile
+   [Code Institute Sample README](https://github.com/Code-Institute-Solutions/SampleREADME) - Readme Template

### Acknowledgements:
+ [Spencer Barriball](http://www.5pence.net/) - Huge thank you to my mentor Spencer for all his help and guidance
+ [codeinstitute.net](https://codeinstitute.net/) - Lessons, videos, tutoring & support
+ [Cork International Hotel](https://www.corkinternationalairporthotel.com/) - For showing interest in using this app 

### Media:
+	[Parallax Image 1](https://cf.bstatic.com/images/hotel/max1024x768/653/65346226.jpg)
+	[Parallax Image 2](https://www.corkinternationalairporthotel.com/wp-content/uploads/2019/07/lobby-003.jpg)

# Testing

### Number of validators and services were used to validate pages to ensure there were no syntax errors:
-   [Extend Class - Python Syntax Schecker](https://extendsclass.com/python-tester.html) - [Results](/static/readme-files/validate-python.png)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](/static/readme-files/validate-css.png)
-   [Esprima jQuery Validator](https://esprima.org/demo/validate.html) - [Results](/static/readme-files/validate-jquery.png)
-   [Lighhouse Tool](https://developers.google.com/web/tools/lighthouse) - [Results](/static/readme-files/lighthouse-report.png)

### Manual Testing Procedures:

    - TEST:
        - Expected: 
        - Testing: 
        - Result: 

- #### Navigating The Site:
    - Browsing  as unlogged user:
        - Expected: only home & login links available 
        - Testing: visited site as unlogged user
        - Result: expected results
    - Typing directly in URL bar as unlogged or 'normal' user:
        - Expected: before user is logged in, if he tries to type in views directly in URL bar, he is redirected
            to login page. If user is logged in but not part of mgmt or admin and tries to do the same, he will
            be redirected to home page
        - Testing: Tried to type in directly in URL bar as both logged in and logged out.
        - Result: Expected results on all views except 'search' which returns pymongo error for both logged and unlogged users.
    - Browsing as 'normal' user:
        - Expected: floating action buttons, admin controls, and admin mobile controls to be hidden and inaccessible
        - Testing: logged in as normal user and browsed the site 
        - Result: got expected results. None of the controls are visible to normal user
    - Browsing as 'admin' or 'mgmt':
        - Expected: Profile page to have cards with admin controls, desktop size to have floating action buttons, 
            mobile to have those buttons in side nav and FAB hidden.
        - Testing: Logged in as admin on both desktop & mobile and browsed the site
        - Result: got expected results

- #### Login:
    - If either username or password are incorrect:
        - Expected: redirect back to login and flash message "Incorrect Username and/or Password"
        - Testing: tried inputing just wrong username, just wrong password, and tried both wrong password and username
        - Result: got expected results on all tries
    - If both username and password are correct:
        - Expected: store a session cookie, redirect to user's profile page and 
            flash message displayed "Welcome, 'user's first name'"
        - Testing: inputted correct username & password
        - Result: got expected results
- #### Log out:
    - Log the user out by clicking 'Log Out' button:
        - Expected: redirect back to login page and delete current session cookie
        - Testing: while logged in, clicking on 'Log Out' button
        - Result: expected result
    - Log out after set time of inactivity:
        - Expected: redirect back to login page and delete current session cookie, if user
            comes back after set time of inactivity (15 minutes)
        - Testing: logged in and left the page for 15 minutes. After that tried to navigate the page.
        - Result: Got expected result, redirected back to login page.

- #### Register New User:
    - Create new user:
        - Expected: if all inputs are valid, insert new record in 'users' collection in db, and flash message 
            that user was created successfully and flash message new user's password
        - Testing: input valid information and click register
        - Result: got expected results
    - Passwords do not match:
        - Expected: If 'password' and 'repeat password' do not match exactly, flash 'Passwords Do Not Match'
            and return to registration page
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
            If user types less than min number of chars set for each field, form warn the user to match the requested format.
    - Mobile View Icon:
        - Expected: for hidden font awesome icon for last name to appear on mobile devices and stay hidden on large
        - Testing: tried creating new user on both mobile & desktop
        - Result: got expected results
    - Capitalization:
        - Expected: username to be saved in all smaller letters & first and last name to be capitalized
        - Testing: input may different variations for all username, first & last name while creating new user
        - Result: got expected result on every try
- #### Creating new task:
    - Successful creation of task:
        - Expected: If all fields are inputted correctly, task should be inserted into db, 
            user should be redirected and flash message displayed confirming that task was created
        - Testing: Tried creating both personal & departmental tasks on both mobile & desktop 
        - Result: got expected results
    - If any of the criteria for task creation is not met:
        - Expected: user to be notified and redirected and task not inserted in db
        - Testing: tried inputting less than min char, more than max, leaving fields blank, inputting text/numbers
            into date field
        - Results: got expected results on all tries except when user tabs from task description to date picker. 
            Date picker doesn't trigger and user can input anything he want's. I've fixed it by checking if the format is 
            correct, and if it isn't user will be redirected a step back and flash message will warn him to format the date properly.






- TEST:
        - Expected: 
        - Testing: 
        - Result: 
=====================
- changed to redirects after seeing that on refresh it pops form resubmit



### Unresolved Issues:
- When creating or editing task sometimes date picker doesn't trigger on click but rather 
    enables user to manually input values. It also happens every time user tabs from task description to due_date. 
    due_date used to be text format so it would save the input, but I changed due_date
    to save as date format so if by any chance wrong format is inputted, user is redirected back and flash message is displayed.
- After creating or editing a task user is redirected to view set by a return of performed function instead of being redirected 
    back where he was. It tried including 'onclick="history.go(-1); return false;"' in buttons which worked as far as redirect 
    go, but didn't create or update a task. I also tried returning redirect('request.referrer') which did save the task and it
    did in fact redirect but back to task creation or task editing, instead of page before it. 

### Bugs & Fixes:
- All html files except base.html throw warning "Doctype must be declared first."
    - It is ignored because all html files are injected into base.html and it's Doctype is declared.
- edit_dept_task has to identical id's in switches.
    - It can be ignored because it's in if-else loop and only one id is used.
- login_required decorator was throwing an error instead of 
    redirecting when unlogged users tried to access restricted pages,
    because I used 'if session["user"] is None'.
    - Fixed by using: is_logged = session.get("user") in:
        if is_logged is None: ...
- There was a bug on mobile (specifically IOS) where when you click on item in dropdown select list, 
    wrong item gets selected. Also dropdown caret is positioned wrong.
    - Fixed by adding Alvin Wang's select.js file to scripts (full credit in 'Credits')
- Date picker sometimes on click doesn't trigger date picker and allows manual entry.
    It also happens every time user tabs from task description to date picker.
    - Didn't find a way to fix it, but I added try/except where try tries to format input as date, and 
    if it fails user is redirected back to task create/edit and flash message is displayed warning that
    date format was wrong.
- Had to refactor tasks list half-way through the project after adding slideToggle click event to ul.
    Idea was for tasks to be hidden until "show tasks" button was clicked. It would then show 
    collapsable li of tasks, but it didn't work until I reorganized divs and li's a lot to make it work.
- Half-way through the project I noticed created_by & created_on labels changed to editors information 
    after editing tasks. Fixed by using $set syntax, which enabled to update just given values. 
    All other non-provided values on editing (like created_by, created_on) stay the same.
- Had a bug with modals just after implementing them to pop to confirm deletion of a task. 
    Modals would open only for first task which I fixed by moving modal structure outside of collapsible body.
    That fixed modals opening for just first item in the list but still if I try to delete e.g. 5th
    task in the list, first task in the list would be deleted. It was because of modals id's so 
    I fixed it by using #modal1{{ loop.index }} for first list, #modal2{{ loop.index }} for second etc.
- I decided to use Materialize floating action button to show control view links like 'register new user',
    'view all tasks', 'assign personal tasks' etc. It worked fine on desktop but there were minor issues on mobile. 
    Button's tooltips sometime wouldn't dissapear automatically but would stay until refreshed, and it was hard to 
    intuitively know what buttons do without hovering and seeing tooltips text, so I disabled FAB on mobile and 
    put links in mobile side nav instead.
- Near the end of the project I wanted to compare today's date to due_date in order to mark all tasks past due.
    Up until then, dates were saved in string format, so I refactored views to save in date format, and then using jinja
    compared today to due_date.
- Above changes brought small issue when editing task. If date wasn't changed when editing, there was a formatting issue,
    as time data didn't match the format. Fixed it by adding '.strftime('%d/%b/%Y')' to date values when editing task.

### Coding Process / Reasoning:
- Initially I set up two collections for tasks: 'tasks' for department tasks, and 'personal' 
    for personal tasks, because I wasn't sure will I be able to manage it in one colelction.
    After learning how to manage it, I refactored code to use one collection 'tasks' for 
    both personal and department tasks.
- I decided to use Materialize as a front-end Framework, because it's a new framework for me,
    and wanted to get more familiar with it.
- Towards the end of the project I decided to get rid of 'control' view which had it's access limited to admins and mgmt, 
    and contained links for creating new user, creating new tasks, tracking tasks etc.
    I decided to put those links in floating action button on dekstop, and on mobile put it in mobile view side nav.
- Also towards the end of the project, after consulting with my mentor, I decided to use just one collection for tasks. 
    Until then I had tasks & completed_tasks which I then merged into one collection.

### Testing User Stories from User Experience (UX) Section:
- As someone who would use this task manager regurarly, I want tasks and lists to be informative and easily understandable.
    - Task lists contain list items with: task name, due date & urgency status.
    On opening specific task: task description, created by, created on are visible, under which is complete button. 
    Additionally if someone edits the task, that is also visible in task body.
- As a head of department I want to be able to assign a task that will be visible only to staff in my department
    and can be completed by anyone in my department.
    - Normal users can see and complete tasks assigned to their department on tasks page.
- As a manager I want to be able to create a new task that will be visible by all members.
    - "Shared" tasks list contains all tasks that will be visible to every member.
- As a head of department I want to be able to assign a personal task that will be visible only to me and staff member I
    assigned the task to.
    - Normal users can see and complete their own personal tasks assigned to them by management or themselves.
- As a head of department I want to be able to keep track of all the tasks I assigned either to department or staff member specifically.
    - All management members can access all tasks from "control panel" page, and additionaly they have a list of all 
    tasks assigned by them.
- As part of management I want to be able to delete any tasks.
    - Management can delete any task, while normal users can only delete tasks create by themselves (own personal task)
- As a part of management I want to be able to edit and redelegate tasks.
    - All management members can edit all tasks while normal users can only edit tasks they created. When editing they can 
    reassign the task to other staff member or department.
- As a normal staff member, I want to be able to add a personal task to myself as a reminder.
    - Normal users can only create personal tasks for themselves, and those tasks are the only tasks they can edit or delete.
- As a part of management I want to be able to see if someone edited a task I made, and when.
    - When task is edited new keys (edited by, edited on) are inserted into task and shown in task body after editing so 
    it's easy to keep track of who edited the task and when.
- As a part of management I want to be able to easily see the tasks that are past due.
    - All task lists are sorted by due date, and for every task comparison is made to see if due date is in the past.
    If due date is today or before, red triangle "Task Due!" is displayed next to the task name.
- As management I want to be able to search through deparment tasks and see completed tasks too.
    - all_tasks view has search function and it's list contains all department tasks both completed and uncompleted.


# INSERT DEPLOYMENT TO HEROKU
# INSERT DEPLOYMENT TO HEROKU
# INSERT DEPLOYMENT TO HEROKU
# INSERT DEPLOYMENT TO HEROKU
