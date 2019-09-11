
## **Django osw4l boilerplate** ##
## is a django project, that provides some settings to help to developers to start a new django project with the least effort, so simple how clone a repository ##

## About the project ##

 - project structure defined
 - script for run **[local server](https://github.com/0sw4l/django-simple-started-kit/blob/master/runserver.sh)**
 - script for migrate **[local](https://github.com/0sw4l/django-simple-started-kit/blob/master/local_db.sh)** and **[server](https://github.com/0sw4l/django-simple-started-kit/blob/master/server_db.sh)** db
 - containts **[.gitignore](https://github.com/0sw4l/django-simple-started-kit/blob/master/.gitignore)**  for **.idea/**, **db.sqlite3**, **pyc**, **.pyo** and **pycache dir**
 - **python** 3 by default
 - two server environments configured **(local and production)**
 - templates dir configured
 - statics and media files configured
 - ready to deploy in **heroku**
 - contains [utils](https://github.com/0sw4l/django-simple-started-kit/tree/master/apps/utils) for [views](https://github.com/0sw4l/django-simple-started-kit/blob/master/apps/utils/views.py), [print colors](https://github.com/0sw4l/django-simple-started-kit/blob/master/apps/utils/print_colors.py), [shortcuts](https://github.com/0sw4l/django-simple-started-kit/blob/master/apps/utils/shortcuts.py) and [error views](https://github.com/0sw4l/django-simple-started-kit/blob/master/apps/utils/errors.py)
 - apps structure defined
 - api structure defined
 - **django channels settings** [(read more...)](https://channels.readthedocs.io/en/stable/)
 - **django rest framework** [(read more...)](http://www.django-rest-framework.org/)
 - **django rest framework token authentication** [(read more...)](http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)
 - **django rest auth** (login and registration) [(read more...)](http://django-rest-auth.readthedocs.io/en/latest/introduction.html)
 - **cors headers free** [(read more...)](https://github.com/ottoyiu/django-cors-headers/blob/master/README.rst)
 - firebase cloud messaging **(fcm)**  support [(read more...)](https://firebase.google.com/docs/cloud-messaging/server)

Mode of use

> The first step you have to do to start using this beautiful started kit is to give permissions to all the sh files that it contains, as follows

     sudo chmod u+x runserver.sh
     sudo chmod u+x local_db.sh

> The next step is to do a migration with our migration script to the db once you are granted the required permissions

    ./local_db.sh

> To run the server you simply run the **runserver.sh** script, as follows

    ./runserver.sh

fcm settings
> for configure fcm with django go to **[here](https://github.com/0sw4l/django-simple-started-kit/blob/master/apps/fcm/settings.py#L6)** , and change this `API_KEY = "YOUR FCM KEY".` , read about the endpoints api [here](https://github.com/naviens/django-fcm#docs).

This was done with much love and dedication to make the configuration and development of your projects faster❤️, Thank you for being wonderful ❤️ 😄.



