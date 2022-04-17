# django-boilerplate

This is a starting point for a new Django4 Project with MYSQL database (but 
you can easily configure it with another database engine). 

## Requirements

- python3

## Install

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

Project's information are in  
```
dango_boilerplate/__init__.py
```
This file is loaded at the starting of the entire project

You can change them with your informations:

- \_\_version__
- \_\_alias__
