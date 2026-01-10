# Fastapi-fullstack-task-manager
This project is a simple full-stack task management application that I built while learning FastAPI
The goal was to understand how backend APIs, frontend templates, and a database work together in a real application.
Users can register, log in, and manage their own tasks.
Each user only sees the tasks they created.
Why I Built This
I wanted hands-on experience with:
FastAPI backend routing
Form handling and redirects
Template rendering using Jinja2
User authentication flow
Connecting a backend to a database
Structuring a real-world project (not just single files)
Features
User registration and login
Cookie-based authentication
Add and view personal tasks
Each user has their own task list
Clean separation of routes, templates, and database logic
Simple UI using HTML and CSS
Tech Stack
Backend: FastAPI (Python)
Frontend: HTML, CSS, Jinja2 templates
Database: SQLite
ORM: SQLAlchemy
Server: Uvicorn


# Project FastAPI Full-Stack Task Manager
│
├── main.py              # App entry point
├── database.py          # Database connection
├── models.py            # Database models
├── requirements.txt     # Dependencies
│
├── routers/
│   ├── auth.py          # Login & register routes
│   └── todo.py          # Task related routes
│
├── templates/
│   ├── layout.html
│   ├── login.html
│   ├── register.html
│   ├── home.html
│   └── add_todo.html
│
├── static/
│   └── style.css
# How Authentication Works 
User logs in using a form
Backend checks username and password from the database
If valid, a cookie is set in the browser
Every request checks the cookie to verify the user
If not logged in, user is redirected to the login page
# How Tasks Work
Logged-in users can add tasks
Each task is stored with the username as the owner
When the home page loads, tasks are filtered by the logged-in user
This ensures users only see their own tasks

# HOW TO RUN THE PROJECT

Install dependencies:


pip install -r requirements.txt
Start the server:
uvicorn main:app --reload
Open browser:

http://127.0.0.1:8000

# WHAT I LEARNED FROM THIS PROJECT:

How FastAPI handles requests and responses
Difference between GET and POST routes
How form data flows from frontend to backend
How databases integrate with backend code
Why project structure matters in real applications
Debugging real issues like redirects, cookies, and errors
Future Improvements
Password hashing instead of plain text
Search tasks feature
Edit and delete tasks
JWT-based authentication
Better UI styling

This project helped me understand full-stack development using Python, and gave me confidence to build and debug real applications instead of only writing APIs.
