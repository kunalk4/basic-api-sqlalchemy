# Introduction
Creating a RESTful API using Flask, FLASK-SQLAlchemy, Flask-Marshmallow and Flask-Migrate

Application allows user to POST data to database and retrieve user data via GET. The database used is a local development sqlite with migration scripts attached. 

POST requests currently require POSTMAN (or alternative) as no frontend built. 

# Environments

The subdirectory should

This project uses <code>pipenv</code> to install packages and associated dependencies. Please <code>pip install pipenv</code>

The environment variables for this proejct can be found in the app/.env folder. Using the <code>dotenv</code> package
