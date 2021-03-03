## User Stories
- As someone who would use this task manager regurarly, I want to tasks and lists to be informative and easily understandable.
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
- As part of management I want to be able to edit and redelegate tasks.
    - All management members can edit all tasks while normal users can only edit tasks they created. When editing they can 
    reassign the task to other staff member or department.
- As normal staff member, I want to be able to add a personal task to myself as a reminder.
    - Normal users can only create personal tasks for themselves, and those tasks are the only tasks they can edit or delete.
- As part of management I want to be able to see if someone edited a task I made, and when.
    - When task is edited new keys (edited by, edited on) are inserted into task and shown in task body after editing so 
    it's easy to keep track of who edited the task and when.
- 

## Bugs & Fixes
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
    after editing tasks. Fixed by using $set syntax, which enabled to update with just given values. 
    All other non-provided values on editing (like created_by, created_on) stay the same.
- Had a bug with modals just after implementing them to pop to confirm deletion of a task. 
    Modals would open only for first task which I fixed by moving modal structure outside of collapsible body.
    That fixed modals opening for just first item in the list but still if I try to delete e.g. 5th
    task in the list, first task in the list would be deleted. It was because of modals id's so 
    I fixed it by using #modal1{{ loop.index }} for first list, #modal2{{ loop.index }} for second etc.
- 

## Coding Process / Reasoning
- Initially I set up two collections for tasks: 'tasks' for department tasks, and 'personal' 
    for personal tasks, because I wasn't sure will I be able to manage it in one colelction.
    After learning how to manage it, I refactored code to use one collection 'tasks' for 
    both personal and department tasks.
- I decided to use Materialize as a front-end Framework, because it's a new framework for me,
    and wanted to get more familiar with it.
- Towards the end of the project I decided to get rid of 'control' view which had it's access limited to admins and mgmt, 
    and contained links for creating new user, creating new tasks, tracking tasks etc.
    I decided to put those links in floating action button on dekstop, and on mobile put it in mobile view side nav.

## Features
### Back End
- Session expiry after set time of inactivity (set time inside set_session_timeout function)
- Redirects to home page if unlogged user tries to access any of the pages login is required for
- Redirects to task page if non-admin or non-mgmt user tries to access admin & mgmt pages
- 

### Front End
- 



## Credits
- https://randomkeygen.com/ - for generating SECRET_KEY
- https://materializecss.com/ - framework
- jQuery
- font awesome
- Alvin Wang - https://github.com/Dogfalo - select.js fix for select dropdown


# PRESET README


![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome nsum,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use.

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

--------

Happy coding!
