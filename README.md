# Task Manager

This project is a simple task manager built using Django. It allows users to create, edit, delete, and list tasks. The project includes a basic form to input task details and manage them through the admin interface.

## Installation

To set up this project on your local machine, follow these steps:

1. Install Python and pip if you haven't already.
2. Clone the repository and navigate into the project directory.
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   
## Usage

To run the project locally, follow these steps:
  1. Apply the database migrations:
      python manage.py migrate
      
  2. Start the development server:
      python manage.py runserver

  3. Access the project in your browser at http://127.0.0.1:8000.

## Admin Interface
The project includes an admin interface to manage tasks. To access the admin panel:
    Create a superuser account:
    python manage.py createsuperuser
    Log in to the admin panel at http://127.0.0.1:8000/admin/ with the superuser credentials.

## Features
    Create, update, and delete tasks.
    View tasks in a list format.
    Admin interface for managing tasks.

## Contributing
If you'd like to contribute to this project, feel free to fork the repository, create a new branch, and submit a pull request.
License
This project is open-source and available under the MIT License.


