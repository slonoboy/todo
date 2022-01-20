# Django TODO app
### Installation 
Download files to your project folder. Create virtual environment and use requirements to install required packages (you can use pip install -r /path/to/requirements.txt command).  Raise postgresql database server and change database configurations in setting.py. Change the following rows in settings.py:
``` python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<database name>',
        'USER': '<username>',
        'PASSWORD': '<user password>',
        'HOST': 'localhost',
        'PORT': '',
    }
}

```
###  Usage
Locate your command line location to folder with manage.py file and type python manage.py runserver. Now you can open web browser and connect to your local web server by typing http://127.0.0.1:8000/ in address bar. By default you will need to create an account and log in. Then on the main page you can add a task by writing it in and clicking + button. A task can be completed by clicking on "complete" button and it will nove to completed tasks section, then you can delete any task if you want to.

Overall there are 4 addresses:
- /registration
- /login
- / (only for logged in users)
- /admin (for staff only users)

You can interract with database by importing Todo model from models.py or by going to admin panel. But firstly your need to create super user. Type python manage.py createsuperuser. Now you have a super user who can use admin panel and edit database data.

### Examples
