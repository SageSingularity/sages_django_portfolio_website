# Sages Django Portfolio Website
Built to handle displaying my portfolio, as well as being a portfolio project itself.

# Start Local Dev Server
`python3 manage.py runserver`

# Adding a new App
Apps are ways to logically divide the website into modules.

1. Use `python3 manage.py startapp <app_name>` to create it
2. Add `urls.py` file to new App directory
3. Add a path to this new `urls.py` file in top-level `urls.py`.
4. Add `<app_name>` to `INSTALLED_APPS` inside `settings.py`.

# Working with Views
1. Create the `<view_name>_view.py` file.
2. Add the View to the appropriate App's `urls.py`.

# Adding a new Model

# Working with Templates
Templates are `HTML` files that are served by Django and 
allow variables. In other words, you can dynamically add 
things to a Django Template at runtime.

Django looks for `templates` directories and combines them
into a single large directory. Therefore, you will want to 
separate each Apps Templates via a directory with the App
name. For example, `<app_name>/templates/<app_name>`.

## CSS, JavaScript, and the Static Subfolder
`CSS` and JavaScript are categorized as Static Content
(Not handled dynamically by Python/Django). This is contained
in `<app_directory>/static/<app_name>` subfolder.

Common directories in this subfolder are:
* `images`
* `scripts`
* `styles`

## Add CSS Stylesheet to Template
To utilize a `CSS` Stylesheet in a Template:
1. Add `{% load static %}` to the top of the Template.
2. Add `<link rel="stylesheet" href="{% static 'blog/styles/base.css' %}">`

Note that this maps to `<app_name>/styles/<css_stylesheet_name>.css`.