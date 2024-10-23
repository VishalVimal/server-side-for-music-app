# Project Title

## Overview
This project involved creating a virtual environment to manage dependencies, ensuring that they were isolated from other projects.

## 1. Creating a Virtual Environment
- Executed `python3 -m venv venv` to create a new virtual environment in the `venv` folder.
  - `-m venv` runs the venv module.
  - `venv` is the directory name.
- Encountered an error while running `python3`, so used `python -m venv venv` instead.

## 2. Activating the Virtual Environment
- Activated the virtual environment using:
  ```bash
  source ./venv/bin/activate
  ```
  - `source` is the shell command to execute the script.
  - `./venv/bin/activate` is the path to activate the virtual environment.
- Initially attempted to run it using a command that pointed to the `Scripts` folder, but successfully activated the environment from the correct directory.
- Ensured that any installed dependencies were only present in this specific folder.

## 3. Creating an API
- Utilized FastAPI for API development.
- Installed FastAPI with:
  ```bash
  pip3 install fastapi
  ```
- Created a simple API route and ran the app in developer mode using:
  ```bash
  fastapi dev main.py
  ```
- Accessed the application at `127.0.0.1`.
- Noted that anything after a question mark in the URL is treated as a query.

## 4. Signup Validation
- Developed the route for signup validation and installed PostgreSQL.

## 5. Database Connection
- Used SQLAlchemy to connect the backend framework to an external database.
- Installed SQLAlchemy and imported the engine.
- Called the function with a specific URL to create a session.
- Utilized SQLAlchemy's session maker to create a session.
- Initialized the database, created the table structure, and wrote the SQL query.
- Successfully created the API route for signup.

## 6. Code Refactoring
- Refactored the code for improved readability and maintainability.
