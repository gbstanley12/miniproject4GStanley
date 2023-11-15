# miniproject4GStanley
## INF681 - Advanced Programming with Python
### Gavin Stanley
### Mini Project 4

## Project Description
This Django web application allows users to view, add, and review movies. It features a user authentication system, movie details pages, and the ability to submit and display reviews with ratings.

## Installation
Ensure you have Python and Django installed on your system. Then, install the required dependencies:

```pip install -r requirements```


## Database Initialization
Run the following commands to set up your database:

```python manage.py makemigrations``` (this will create any SQL entries that need to go into the database)

```python manage.py migrate``` (this will apply the migrations)

```python manage.py createsuperuser``` (this will create the administrator login for your /admin side of your project)

## Running the Application
To start the server, run:
```python manage.py runserver```

Navigate to `http://127.0.0.1:8000/` in your web browser to view the application.

## Features
- User Registration and Login
- Movie Listings
- Movie Details with Image Uploads
- Review Submission with Star Ratings
- Admin Panel for Movie and Review Management
