# Chronos Task Manager

## Overview

Chronos Task Manager is a web-based task management application designed to help users organize and keep track of their tasks efficiently. The application is built using Django, a high-level Python web framework, and leverages Bootstrap for a clean and responsive user interface.

## Features

- **Task Management:** Create, edit, and delete tasks with details such as description, due date, status, and priority.
- **User Assignment:** Assign tasks to specific users for collaboration.
- **User Authentication:** Secure user authentication with customizable user profiles.
- **Project Integration:** Organize tasks within projects for better project management.
- **Responsive Design:** The application is designed to be responsive, providing a seamless experience on various devices.

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/chronos-task-manager.git
   cd chronos-task-manager
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Migration:**
   ```bash
   python manage.py migrate
   ```

4. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

   The application should be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

5. **Create an Admin User:**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin user, which you can use to access the Django admin interface at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Usage

1. **Login:**
   Access the application by navigating to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and log in using your credentials.

2. **Task Management:**
   - Create tasks with descriptions, due dates, statuses, and priorities.
   - Assign tasks to users for collaboration.

3. **Project Management:**
   - Organize tasks within projects for better project management.

4. **Admin Interface:**
   - Access the Django admin interface at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to manage users, tasks, and projects.
