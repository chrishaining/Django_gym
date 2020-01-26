<img src="/static/images/weightlifting.jpg" width="80%" height="200">


# My Django Gym

This is my first attempt at creating a gym app using Django. The scenario is an app that is used by members of gym staff to view and add members, sessions^ and instructors. There's also an admin facility that allows an admin-level user to edit and delete members, sessions and instructors.
^ A session is the name used for a fitness class. I didn't use the word "class" in the app since it is a reserved word in Python.


## The main features I wanted to work on are:
* Create an admin function
* Give users the ability to add new instances of the three main classes (Member, Instructor, Session) using forms
* Display lists of names and titles (the name/title properties of my class instances)
* Use a navbar to navigate between different parts of the app, including between the admin function and main app
* Creating a responsive navbar that shows the hamburger on mobile devices (but on larger devices still shows a normal list). 

## Languages/packages
* Python 3
* pip
* Django (built with version 3.0)
* Bootstrap 4.0

## To download and run the app
* Set up a virtual environment: `python -m venv .env`
* Open the virtual environment: `source .env/bin/activate`
* install Django: `pip3 install django`
* Clear any existing data in the database: `python manage.py flush`. When prompted, type `yes`
* Populate the database: `python manage.py loaddata seeds.json`
* To run the app: `python manage.py runserver`. Use the local port advised in the script.
* To gain access to the admin function, create a user from the command line: `python manage.py createsuperuser`

