1. pip install Django==2.2.7
2.pip install django-crispy-forms
3.pip install django-crispy-forms
4.pip install django-parler
5.pip install jsonfield2
6.pip install pillow


python manage.py makemgrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
https://www.codementor.io/@jamesezechukwu/how-to-deploy-django-app-on-heroku-dtsee04d4

heroku login:
#########################################################################
(django_env):~/Desktop/djangoherokuapp$ heroku login
Enter your Heroku credentials:
Email: your_email@emailprovider.com
Password: *********
Logged in as jameseze.ca@gmail.com
(django_env):~/Desktop/djangoherokuapp$ 
########################################################################

Procfile.file
///////////////////////////////////////////////////////////////////////
(django_env):~/Desktop/djangoherokuapp$ touch Procfile
Open the Procfile and add the line below.
web: gunicorn djangoherokuapp.wsgi --log-file -
///////////////////////////////////////////////////////////////////////

runtime.txt
#######################################################################
Open the runtime.txt file and add the following line,
or as applicable, to your application.
python-2.7.12
########################################################################
pip install django-heroku
pip install gunicorn dj-database-url whitenoise psycopg2
(django_env):~/Desktop/djangoherokuapp$ pip install gunicorn dj-database-url whitenoise psycopg2
#########################################################################

requirements.txt
(django_env):~/Desktop/djangoherokuapp$ pip freeze > requirements.txt
pip freeze > requirements.txt
########################################################################
Open up settings.py file and make the following changes, preferably at the bottom of the file.

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
PROJECT_ROOT   =   os.path.join(os.path.abspath(__file__))
STATIC_ROOT  =   os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra lookup directories for collectstatic to find static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

#  Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

##############################################################################

Add whitenoise middleware at the top of the middleware list in settings.py

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#############################################################################
import dj_database_url 
prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)
#######################################################################
Create App in Heroku from terminal
heroku create onlineexam1994
https://onlineexam1994.herokuapp.com/ | https://git.heroku.com/onlineexam1994.git
(django_env):~/Desktop/djangoherokuapp$ heroku create herokudjangoapp
Creating ? herokudjangoapp... done
https://herokudjangoapp.herokuapp.com/ | https://git.heroku.com/herokudjangoapp.git
######################################################################


heroku config:set DJANGO_STATIC_HOST=https://d4663kmspf1sqa.cloudfront.net
######################################################################################
Add your app domain name to ALLOWED_HOSTS in settings.py.

ALLOWED_HOSTS = ['herokudjangoapp.herokuapp.com']
ALLOWED_HOSTS = ['onlineshop1994.herokuapp.com']

#########################################################################
git init
heroku git:remote -a onlineexam1994

git add -A
git commit -m 'mkm'
#git push heroku master
heroku config:set     DISABLE_COLLECTSTATIC=1
git push heroku master
#########################################################################

heroku run python manage.py migrate
heroku run python manage.py makemigrations
heroku run python manage.py createsuperuser
heroku run python manage.py runserver
-----------------------------------------------------------------------------
or push an existing repository from the command line
git remote add origin https://github.com/mkmaurya955/E-Commerce.git
git push -u origin master

---------------------------------------------------------------
for again pushing
Install the Heroku CLI
Download and install the Heroku CLI.

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

$ heroku login
Clone the repository
Use Git to clone onlineexam1994's source code to your local machine.

$ heroku git:clone -a onlineexam1994
$ cd onlineexam1994
Deploy your changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.

$ git add .
$ git commit -am "make it better"
$ git push heroku master 