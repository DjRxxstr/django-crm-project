# Customer Relationship Management (CRM) Web App

A simple Customer Relationship Management (CRM) web application built with Django and Python. This app allows users to manage customer records with full CRUD functionality. It includes secure user authentication, role-based access control, CSV export support, and a responsive UI for an improved user experience.

## Features
- User login and registration functionality.
- Add, update, view, and delete customer records.
- Role-based access control with Admin, Staff, and Viewer roles.
- Admin-only CSV export of customer records.
- Redirect to a custom "Access Denied" page for unauthorized actions.
- Form validation and error handling.
- User-friendly UI built with Bootstrap for responsiveness.
- Secure user authentication with Django’s built-in user system.

## Technologies Used
- **Backend**: Django, Python
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: PostgreSQL

## Setup Instructions

### Prerequisites
Ensure you have Python 3.x and PostgreSQL installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/crm-web-app.git
   cd crm-web-app
   ```

2. **Set up a virtual environment**:

   - **For Mac/Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - **For Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure PostgreSQL database**:
   Update the `DATABASES` setting in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_db_name',
           'USER': 'your_username',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser to access the admin page** (optional):
   ```bash
   python manage.py createsuperuser
   ```
   Follow the instructions to create the superuser.

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the app**: 
   Open your browser and go to `http://127.0.0.1:8000/` to access the app.
   - For the admin page, visit `http://127.0.0.1:8000/admin/` and log in with the superuser credentials.

### Environment Variables
There are no specific environment variables required for running the app in a local development environment. 

### Static Files
This project uses static files (CSS, JavaScript) to enhance the frontend. Ensure to collect static files if deploying the app in production:
```bash
python manage.py collectstatic
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
