# Flaznov Config file
import os
script_dir = os.path.dirname(os.path.abspath('flazov'))

class Config(object):
    # Your project name
    APP_NAME="myapp"

    # Databse engine like, Postgres, Mysql
    # Default is sqlite3
    DB_PATH='sqlite:////tmp/test.db'

    # Home Page
    FILENAME="base.html"

    # Requirements for your application
    # These are the main flask
    REQUIREMENTS = [
        'flask', 
        'flask_script', 
        'flask_migrate', 
        'flask_debugtoolbar', 
        'flask_sqlalchemy',
        'flask_bootstrap',
        'flask_moment',
        'flask_login', 
        'flask_wtf'
    ]

    # Main folders that you need in your app
    FRONT_END_FOLDERS = [
        'templates',
        'static'
    ]

    CONTROLLERS = [
        'main', 
        'auth'
    ]

    INSIDE_CONTROLLERS = [
        '__init__.py', 
        'views.py', 
        'forms.py'
    ]