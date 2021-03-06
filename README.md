# 
		 _____ _                            
		|  ___| | __ _ _____ __   _____   __
		| |_  | |/ _` |_  / '_ \ / _ \ \ / /
		|  _| | | (_| |/ /| | | | (_) \ V / 
		|_|   |_|\__,_/___|_| |_|\___/ \_/  

		Version: v0.1
		Author: reznov11
		Blog: http://xakepu.blogspot.com
		Github: https://github.com/reznov11
		Twitter: @pentester11
		
Flaznov
============

Project to generate a dynamic Flask application.

**Note:** The project is assuming that you have installed pip and virtualenv on your machine , so please if you dont have them, install them before you use it , in later versions i'll make a function that installs them if they are not exists .

Quick Start
-----------

`Please read instructions before you generate your application`

- First of all, take a look at config

- If you want to use another packages with your app, you can add them to [REQUIREMENTS] in config and the project will generate them inside requirements.txt later .

- If you want to add another controllers to your application, add them to [CONTROLLERS] in config .

- This project will generate an application with two routes and it will register them to blueprint by default, so if you added another controllers, please, don't forget to register there routes to blueprint .

- In snippets you can find the structure of your models and __init__.py, so feel free to change them as you like

- The project using Sqlite3 as back-end database, also ive included another postgresql URI, so if you want to use it just uncomment these lines in config.py and create your database if not exist

	`DB_USERNAME = ''`
	
	`DB_PASSWORD = ''`
	
	`DB_DATABASE = ''`
	
	`SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@localhost:5432/%s'%(DB_USERNAME, DB_PASSWORD, DB_DATABASE)`


How to use
-----------

Lets consider that you already configured your config file and you ready to generate the application .

Step 1: generate application:

	python build.py generate
	

Step 2: active virtual environment:

	source myapp/venv/bin/activate
	
Step 3: installing requirements.txt:

	pip install -r myapp/requirements.txt
	
Step 4: migrate database:

	python manage.py db init
	python manage.py db migrate
	python manage.py db upgrade
	python manage.py inituser
	
Step 5: run the application:

	python manage.py runserver -h 0.0.0.0 -p 3333 # you can just type runserver without any arguments
	 * Running on http://0.0.0.0:3333/ (Press CTRL+C to quit)
	 * Restarting with inotify reloader
	 * Debugger is active!
	 * Debugger PIN: 106-265-028


Video on Youtube:
-----------

I've also created a video on youtube, check it out [Flaznov - A project to generate a dynamic flask application.](https://youtu.be/OWX-C7giNJo).
