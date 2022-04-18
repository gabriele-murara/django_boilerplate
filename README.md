# django-boilerplate

This is a starting point for a new Django4 Project with MYSQL database (but 
you can easily configure it with another database engine). 

## Requirements

- python3

## Clone repository

Clone repository

```
git clone git@github.com:gabriele-murara/django_boilerplate.git
```

## Virtual Env

Create your virtual env and activate it

```
python3 -m venv your_virtual_env
cd your_virtual_env
. bin/activate
```

## Dependencies

This boilerplate is meant for MYSQL database, but you can use your favourite 
database engine. If you want to do this, remember to replace the 
'mysqlclient' dependence in requirements.txt with your database client library.

Install dependencies with pip:

```
pip install -r requirements.txt
```

## Configuration

Configuration file is in 

```
settings/default.py
```
it's recommended to overwrite settings via .env file

copy the .env.sample file to .env

```
cp .env.sample .env
```

and populate it with your values

## Logging

Logger is configured in 
```
settings/default.py
```
it's recommended to overwrite logs settings via .env file

## Database

Database is configured in 
```
settings/default.py
```
it's recommended to overwrite database settings via .env file

## Project informations

Project informations are loaded from .env file and are registered in 

```
django_boilerplate/__init__.py
``` 

## Login Boilerplate

This project comes with a generic login app named login_boilerplate that you 
can easily configure via .env file.

Templates configuration is now work in progress


## Install

```
python manage.py migrate
python manage.py collectstatic
```
