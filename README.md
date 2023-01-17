# Introduction
Creating a RESTful API using Flask, FLASK-SQLAlchemy, Flask-Marshmallow and Flask-Migrate. This application allows user to POST data to database and retrieve user data via GET. 

This code is based on the medium article (https://medium.com/@tinuadeadeleke/a-beginners-guide-to-building-rest-apis-flask-flask-sqlalchemy-and-flask-marshmallow-5159d4eb46d8 ). However I have adapted the code to run error free and used <code>pipenv</code> to track requirements and dependencies.

POST requests currently require POSTMAN (or alternative) as no front-end application, however this will be updated by 31/01/2022. 

# Environments

This project uses <code>pipenv</code> to install packages and associated dependencies. Run <code>pip install pipenv</code> into the command line when in the <code>app</code> directory. This will create a virtual environment. Run <code>pipenv shell</code> to activate this virtual environment. 

To install a package run <code>pipenv install <package-name></code>.

The environment variables for this proejct can be found in the app/.env folder. Run <code>pip install dotenv</code>. This will allow the /.env file to create environment variables whenever this app is run, without having to manually set them. 

# Database

The database used is a local development sqlite. The ORM used is SQLalchemy and JSON objects are serialised using Flask-Marshmallow. The application uses Flask-Migrate to generate migration scripts. 

Within the <code>app</code> folder, run <code>flask db init</code> to intialise 
<code>app</code>
<code>app</code>
<code>app</code>

Please run 

# API Doc
TODO (31/12/2022) (Generated via Swagger UI) 
