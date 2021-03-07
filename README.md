[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](http://shields.io/)

![logo](/static/readme-files/nsum.png "nsum logo")

#### Code Institute - Milestone Project 3 
## Cork International Hotel Task Manager
![Am I Responsive](/static/readme-files/responsive.png)

## Introduction
Welcome,
This web app is made as 3rd Milestone Project with Code Institute.
I decided to make a task manager app because hotel I work in showed interest and need for an app such as this.
Before submission this project will be copied to another repo and then used throughout the hotel group I work in. 
Some of the features included are: full CRUD functionality, specific department tasks, personal tasks, shared tasks,
management control, search and task editing...

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

### Manual Testing:
# insert testing here
=====================

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

## Bugs & Fixes:
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
- Date picker sometimes on click enables manual entry instead of popping up calendar to choose from.
    - Rarely happens and didn't fix
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

## Coding Process / Reasoning:
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

