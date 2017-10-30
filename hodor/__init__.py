# -*- coding: utf-8 -*-
# app/__init__.py
import os
import sys
import time
from termcolor import colored
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()

from hodor.models import *  # noqa

# TODO: Don't forget to change when in production
config_name = 'development'

application = FlaskAPI(__name__, instance_relative_config=True)
application.config.from_object(app_config[config_name])
application.config.from_pyfile('config.py')
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(application)
application.config['SECRET_KEY'] = 'blehblehbleh'


# Delay the application launch to get the user attention if running in
# testing mode

if config_name != 'production' and not os.getenv('SKIP_COUNT'):
    for x in range(0, 5):
        sys.stdout.write(colored("\rYou are not running the server in production mode. " +
                            "App will run in {} seconds..".format(5-x), 'red'))
        sys.stdout.flush()
        time.sleep(1)

print(colored("\n\nRunning app in {} mode..".format(config_name), 'yellow'))

# This disables the HTML API renderer for flask_api when called through
# browsers.
if config_name == 'production':
    application.config['DEFAULT_RENDERERS'] = [
        'flask.ext.api.renderers.JSONRenderer',
    ]

app = application

from hodor.controllers import *  # noqa
