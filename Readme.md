#  Overview

This is a DJango project for storing videos. I have decided to use django web framework for this project. 


# Requirements

- Python 3.7 or above
- Django 4.0 or above


Required python modules are given in `requirements.txt`.


# Installation

You can install the required modules using 
`python3 -m pip install -r requirements.txt`

Make sure you are using virtual environment if not you can use 
`python3 -m pipenv install -r requirements.txt`
to install the modules in a new virtual env


# Structure

In a RESTful API, endpoints (URLs) define the structure of the API and how end user accesses data from our application using HTTP methods  - GET, POST, PUT, DELETE.

In our case, we have following endpoints (URLs):


| Endpoints     | Methods       | Result            |
| ------------- |:-------------:| :----------------:|
| api/upload/   | POST          | upload video      |
| api/listvideos| GET           | list all videos   |
| api/search/   | GET           | search using title|
| api/cost      | GET           | calculate cost    |


# Use

We can test the API using curl or httpie, or we can use Postman

Httpie is a user-friendly http client that's written in Python. Let's try and install that.

You can install httpie using pip:

`pip install httpie`

First, we have to deploy the django's development server with necessary migrations

`python manage.py makemigrations`
`python manage.py migrate --run-syncdb`
`python manage.py runserver`

## How to upload videos

`http --form POST http://127.0.0.1:8000/api/upload/ video=@/pathtovideo/video.mp4`

- Video must be in mp4 or mkv format
- It must be less than 10 minutes(600 seconds) in length and 1 GB in size

## View all uploaded videos

`http  http://127.0.0.1:8000/api/listvideos/`

Another way you can view videos is by searching using title

`http  http://127.0.0.1:8000/api/search/?title=foo`


