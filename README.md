# Hodor WebApp

The web application for the Hodor Project

## Quickstart
* Install postgresql database. The installation will depend on your operating system and distribution.
* Clone the repo using `git clone https://git.amrita.edu/hodorsec/hodor-webapp`
* Create a virtualenv (see below for instructions) and activate it.
* After activating it, `pip install --user -r requirements.txt` to
install dependencies.
* To initialize the database, run the following:
```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```
This will create a folder called `migrations` in the working environment. In most cases, you do not need to care about what's in there. 

* `./runserver.py` to run the app.
* Navigate to `http://127.0.0.1:8080` to watch it in action!

## Virtualenv instructions
* To create a virtual environment, type in `virtualenv <env_name>`.
* After it initializes, execute `source <env_name>/bin/activate` to activate the virtualenv.
