# Introduction
Creating a RESTful API using Flask, FLASK-SQLAlchemy, Flask-Marshmallow and Flask-Migrate. 

This application allows user to POST data to database and retrieve user data via GET. 

This code is based on the medium article (https://medium.com/@tinuadeadeleke/a-beginners-guide-to-building-rest-apis-flask-flask-sqlalchemy-and-flask-marshmallow-5159d4eb46d8 ). However I have adapted the code to: create a front-end, dockerise, run on AWS EBS, include Swagger docs, run error free and used <code>pipenv</code> to track requirements and dependencies.

POST requests currently require POSTMAN (or alternative) as no front-end application, however this will be updated by 31/01/2022. 

TODO:
Flask-RESTplus /n
Dockerise
AWS EBS
Front-End

# Requirements

This project uses <code>pipenv</code> to install packages and associated dependencies 

The <code>Pipfile</code> contains package requirements for the application. 

The <code>Pipfile.lock</code> informs which specific version of those packages should be used, avoiding the risks of automatically upgrading packages that depend upon each other and breaking your project dependency tree.

Run <code>pipenv shell</code> to activate this virtual environment

In the <code>./app</code> directory, run <code>pip install</code> in the command line. This will create install all dependencies in the <code>Pipfile</code>

# Environments 
  
The environment variables for this proejct can be found in the app/.env folder. 

As the <code>/.env</code> file can contain sensitive information I have incldued a <code>/.env.example</code> file to show you an example of what one should look like. 

The two environment varialbes used are 

<code>FLASK_APP=routes.py</code>
<code>FLASK_DEBUG=1</code>
  
The first environment variable points the <code>flask run<package-name></code> command to the correct entrypoint for the application. 
The second runs the app in debug mode.

Run <code>pip install dotenv</code>. 

This will allow the <code>/.env</code> file to create environment variables whenever this app is run, without having to manually set them.

# Database

The database used is a local development sqlite. The ORM used is SQLalchemy and JSON objects are serialised using Flask-Marshmallow. The application uses Flask-Migrate to generate migration scripts for schema versioning. 
  
Run <code>pipenv install flask-migrate</code> to install the migration package. 

Within the <code>app</code> folder, run <code>flask db init</code> to generate a migration scripts within the  <code>./migration</code> folder

Run <code>flask db migrate</code> to run a migration script once a change to the schema has been made

Finally, run <code>flask db upgrade</code> to update changes to the database. 

# API Doc
TODO (31/12/2022) (Generated via Swagger UI) 

# Running app

To run the app go to the <code>./app<package-name></code> directory and run
  
<code>flask run<package-name></code>
  
The app will serve on local host https://127.0.0.1/5000. The default port is 5000. 
