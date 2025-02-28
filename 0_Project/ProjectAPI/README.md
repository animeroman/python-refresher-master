# REST APIs with Flask and Python course

In this repo I will be following along the course on REST API development.

The link to the course repo is https://github.com/tecladocode/rest-apis-flask-python/tree/develop



# Notes

### Docker
#### Kernel 
 - an operating system is made up of two main parts: the kernel and files/programs. 
 - It usually interacts with and controls the hardware. 
All linux distributions use the same linux kernel, and then they add different tools and applications, etc

You can run linux containers on mac or windows because that's how you'll deploy them in the cloud, through linux

Don't develop with different local containers and then deploy them to linux


To use linux containers locally we will use docker desktop. It creates a linux VM and run linux containers in that VM


A Docker container runs everything except the kernel. So all the applications, programs, etc. like bash, python, pip, etc

Docker containers are based on images which specify what is inside the container when it runs 

A docker image is a snapshop of source code, libraries, dependencies, tools and everything else (except OS kernel) that a containers needs to run

#### Dockerfile: 
- a definition of docker image
- We use them to build images
- We can then use an image to run more containers
- To create a docker image, run `docker build -t < image name > .` (Don't forget the dot at the end)

#### Volumes: 
 - persistent data stores for containers. Mapping of a directory between your local file system and the container's file system.
 - Only for local development. When deploying, you don't use volumes. 


To run volumes on windows: `docker run -dp 5000:5000 -w //app -v "%cd%://app" < image_name >`

### Flask
#### Flask smorest
A blueprint is to divide an api into multiple segments

- To open the documentation we need to open `localhost:5000/swagger-ui`

### Insomnia
We use Insomnia to test our api

Defining url on Base Environment: 

```
{"url": "http://127.0.0.1:5000"}
```

### SQLAlchemy
We add sqlalchemy and flask-sqlalchemy to the requirements, and pip install them in our local environment

I was getting a ModuleNotFound error for Flask-SQLAlchemy that didn't allow me to run the api, so I deleted all previous images and created a new one with the requirements, and only then it worked.

`docker build -t < image name > .` **Remember to use the dot at the end**

In this first instance, we are using SQLite. Will change to Postgres later on.


#### Many to manny relationships
Each item can have many tags and each tag can have many items.


### User authentication
#### JWT for access password
Add new packager to requirements and re build the docker image

### Database migrations
We will use Alembic to detect changes to the database models.

We install dependencies in local env, run `flask db init` and it will create a folder named "migrations" with other stuff in it, like a versions folder, alembic file to create the migrations, env, .mako file that will work as template for migration.

Before making the migration we need to tell alembic how the models look like.

To migrate:
 - `flask db init`, then delete the existing db
 - `flask db migrate`
 - `flask db update`

### Deployment
We use Render.com to deploy our API

To run Dockerfile locally after modifying it to run with gunicorn: 

`docker run -dp 5000:5000 -w //app -v "%cd%://app" < image_name > sh -c "flask run --host 0.0.0.0"`

To re create docker container:
`docker compose up --build --force-recreate --no-deps web`



