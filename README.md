# Django Tasks CRUD Project

This Django project implements a CRUD (Create, Read, Update, Delete) functionality for tasks, along with user authentication and route protections. It was developed using Python 3.11.7 and Django 4.1.

## Requirements

- Python 3.11.7
- Django 4.1

## Installation

1. Clone this repository:

    ```
    git clone <repository-url>
    ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Run the Django migrations:

    ```
    python manage.py migrate
    ```

4. Start the development server:

    ```
    python manage.py runserver
    ```

5. Access the application at `http://localhost:8000/`.

## Routes

- `/home/`: Displays the home view.
- `/createTasks/`: Allows creating a new task.
- `/editTask/<int:task_id>/`: Allows editing a specific task identified by its ID.
- `/deleteTask/<int:task_id>/`: Allows deleting a specific task identified by its ID.

- `/`: Landing page for user login.
- `/signin/`: Sign-in view for users.
- `/dosignup/`: Endpoint for user sign-up functionality.
- `/dologin/`: Endpoint for user login functionality.
- `/dologout/`: Endpoint for user logout functionality.

## Usage

1. Navigate to `http://localhost:8000/` in your web browser.
2. If you're not logged in, you'll be redirected to the login page.
3. Sign in using your credentials or create a new account if you haven't already.
4. Once logged in, you can navigate to the tasks section to manage your tasks.
