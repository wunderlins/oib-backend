# OIB Tafel Backend

## install
	$ sudo apt-get install python-mysqldb libmysqlclient-dev
	$ virtualenv tafel
	$ source ./tafel/bin/activate
	$ pip install Django # django 1.9.4 used during development
	$ pip install MySQL-pythonCollecting MySQL-python

create an oracle env file to initisialize en vars in the virt environment. I stored this file in `env/bin/ora_env.sh`. Source this file before sourcing 
the virtual env activate. pip installation of the cx_Oracle will only work if the oracle client is already installed (see below)

	export PATH=$PATH:/opt/instantclient_12_1
	export ORACLE_HOME=/opt/instantclient_12_1
	export LD_LIBRARY_PATH=$ORACLE_HOME

Now source the env file and install the python module.

	$ source ./tafel/bin/ora_env.sh
	$ pip install cx_Oracle

## creating the project
	$ django-admin.py startproject oib
	$ cd oib
	$ python manage.py startapp backend

Configure `oib/oib/ssettings.py` to include the appropriate database configuration under 
`DATABASES`.

### create database configuration files
	$ python manage.py inspectdb --database mdsi > models-mdsi.py

This should generate the database definitions in `models-mdsi.py`

## Oracle client installation on debian

	sudo apt-get install python python-dev python-setuptools gcc libaio1 unzip python-pip

### get insta client from here:
http://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html

- instantclient-basic-linux.x64-12.1.0.1.0.zip
- instantclient-sdk-linux.x64-12.1.0.1.0.zip

### unzip both files 

add the following lines to /etc/bash.bashrc or equivalent. in some cases you must create a wrapper bash script setting these variables befiore running your own script. in my case i had to do it for cron (see export.sh)

	export PATH=$PATH:/opt/instantclient_12_1
	export ORACLE_HOME=/opt/instantclient_12_1
	export LD_LIBRARY_PATH=$ORACLE_HOME

	$ cd instantclient_12_1/
	$ ln -s libclntsh.so.12.1 libclntsh.so
	$ sudo pip install cx_Oracle

