# Introduction
Creating a RESTful API using Flask, FLASK-SQLAlchemy, Flask-Marshmallow and Flask-Migrate. 

This application allows user to POST data to database and retrieve user data via GET. 

This code is based on the medium article (https://medium.com/@tinuadeadeleke/a-beginners-guide-to-building-rest-apis-flask-flask-sqlalchemy-and-flask-marshmallow-5159d4eb46d8 ). However I have adapted the code to run error free and used <code>pipenv</code> to track requirements and dependencies.

POST requests currently require POSTMAN (or alternative) as no front-end application, however this will be updated by 31/01/2022. 

# Requirements

This project uses <code>pipenv</code> to install packages and associated dependencies. 

In the <code>./app</code> directory, run <code>pip install pipenv</code> in the command line. 

This will create a virtual environment and two files are generated. The <code>Pipfile</code> contains package requirements for the application. And the <code>Pipfile.lock</code> informs which specific version of those packages should be used, avoiding the risks of automatically upgrading packages that depend upon each other and breaking your project dependency tree.

Run <code>pipenv shell</code> to activate this virtual environment. 

To install a package run <code>pipenv install <package-name></code>.

# Environments 
  
The environment variables for this proejct can be found in the app/.env folder. Run <code>pip install dotenv</code>. This will allow the /.env file to create environment variables whenever this app is run, without having to manually set them. 

# Database

The database used is a local development sqlite. The ORM used is SQLalchemy and JSON objects are serialised using Flask-Marshmallow. The application uses Flask-Migrate to generate migration scripts for schema versioning. 

Within the <code>app</code> folder, run <code>flask db init</code> to generate a migration scripts within the  <code>./migration</code> folder

Run <code>flask db migrate</code> to run a migration script once a change to the schema has been made

Finally, run <code>flask db upgrade</code> to update changes to the database. 

# API Doc
TODO (31/12/2022) (Generated via Swagger UI) 
