# Django Command
Add Python Projects.  
Django Python command

--------------------
# Installation:

Python 3—version.  
Virtualenv --verison.  
Sudo pip3 install virtualenv.  
Pip install Django.  

--------------------
# Create and Activate virtualenv:
python3 -m venv logintest(projectname).  
virtualenv venv --python=python3.7.  
python3.7.  
Django 2.2.    
source myproject/bin/activate.  
Deactivate.  

--------------------
# Create project
django-admin startproject myproject.  
python3 manage.py startapp posts(project name).  
python manage.py migrate.  

--------------------
# Create New App:
Python manage.py startapp myapp

--------------------
# Run server (myproject):
1.cd my project.  
2.python3 manage.py runserver.  

--------------------
# Save Model Change
class Feature(models.Model).   
    nane:models.CharField(max_length=20).  
details:models.CharField(max_length=400).  
1.settings INSTALLED_APPS[‘my app’].  
2.Python3 manage.py makemigrations.  
3.python3 manege.py migrate.  
--------------------

# CreateAdmin cd myproject:
python3. Manage.py createsuperuser.  
Settings.  
import os.   
INSTALLED_APPS[‘my app’].  
Templates.  
DIRS': [BASE_DIR,'templates'].  
static=under STATIC_URL.  
STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),).  

--------------------
# Postgressql:
https://www.youtube.com/watch?v=QaZrWIvAFsA&t=245s&ab_channel=Recoding.  
Download postgre app and pgadmin4.  
Settings. 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myproject',
        'USER': 'postgres',
        'PASSWORD': 'ji3cl3gj94',
        'HOST': 'localhost'
    }
}
--------------------
# Cmd in myproject:
(Two command for connect postgresql).  
Pip install psycopg2.  
Pip install pillow.  
Python3 manage.py migrate(for auth….).  
Python 3 manage.py makemigrations(for model).  
Source log app/bin/activate.  
Eb open. 
http://login-test.eba-naa26ch2.us-west-2.elasticbeanstalk.com/.  


