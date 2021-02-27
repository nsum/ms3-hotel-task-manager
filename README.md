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
- There is a bug on mobile (specifically IOS) where when you click on item in dropdown select list, 
    wrong item gets selected. Also dropdown caret is positioned wrong

- Had to refactor tasks list half-way through the project after adding slideToggle click event to ul.
    Idea was for tasks to be hidden until "show tasks" button was clicked. It would then show 
    collapsable li of tasks, but it didn't work until I reorganized divs and li's a lot to make it work.



- don't forget to add confirmation for completing the task

## Coding Process
- Initially I set up two collections for tasks 'tasks' for department tasks, and 'personal' 
    for personal tasks, because I wasn't sure will I be able to manage it in one colelction.
    After learning how to manage it, I refactored code to use one collection 'tasks' for 
    both personal and department tasks.

## Features
### Back End
- Session expiry after set time of inactivity (set time inside set_session_timeout function)
- Redirects to home page if unlogged user tries to access any of the pages login is required for
- Redirects to task page if non-admin or non-mgmt user tries to access admin & mgmt pages


### Front End
- 



## Credits
- https://randomkeygen.com/ - for generating SECRET_KEY
- https://materializecss.com/ - framework
- jQuery
- font awesome
- 


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
