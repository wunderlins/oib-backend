# OIB Tafel Backend

## install
    $ sudo apt-get install python-mysqldb libmysqlclient-dev
    $ virtualenv tafel
    $ source ./tafel/bin/activate
    $ pip install Django # django 1.9.4 used during development
    $ pip install MySQL-pythonCollecting MySQL-python

## creating the project
    $ django-admin.py startproject oib
    $ cd oib
    $ python manage.py startapp backend

Configure `oib/oib/ssettings.py` to include the appropriate database configuration under 
`DATABASES`.

### create database configuration files
    $ python manage.py inspectdb > models-mdsi.py

This should generate the database definitions in `models-mdsi.py`
