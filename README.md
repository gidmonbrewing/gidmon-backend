# Gidmon-backend

This README outlines the details of collaborating on this Django application.
A short introduction of this app could easily go here.

## Prerequisites

You will need the following things properly installed on your computer.

* [Git](https://git-scm.com/)
* [Python (2.7, 3.2, 3.3, 3.4, 3.5)](https://www.python.org)
* [Django (1.7+, 1.8, 1.9)](https://www.djangoproject.com)
* [Django REST framework](http://www.django-rest-framework.org)
* [Django REST Framework JSON API](http://django-rest-framework-json-api.readthedocs.io/en/v2.0.1)
* [Pillow] (https://python-pillow.org/)

## Installation

* Download and install Python
* `git clone <repository-url>` this repository
* Change into the new directory
* Optional: `virtualenv nameOfEnv` (creates folder "nameOfEnv" in current dir)
* `pip install django`
* `pip install djangorestframework`
* `pip install djangorestframework-jsonapi`
* `pip install pillow`
* Optional: `deactivate` (leave virtual env)

## Getting Started

* Change into the project directory
* Optional: source nameOfEnv/bin/activate (activate virtual environment created in "nameOfEnv")
* `manage.py migrate` (initial setup of database)
* `manage.py createsupereruser`
* Optional: `deactivate`(leave virtual env)


## Update Database with changes to Models

* `manage.py makemigrations` (creates migration files that are submitted and can later be run on production server)
* `manage.py migrate` (apply migrations from migration files)

## Running / Development

* Optional: source nameOfEnv/bin/activate (activate virtual environment created in "nameOfEnv")
`manage.py runserver [--settings=gidmon_backend.settings_development]`
* Optional: `deactivate`(leave virtual env)

## Deploy latest build on live server

* `sudo systemctl stop uwsgi` (stop service, assuming use of systemctl and uwsgi)
* Change into the project directory
* `git pull (--rebase)` (get latest version from git)
* `source ../env/bin/activate` (activate virtual env created in parent directory)
* `manage.py migrate` (apply database migrations from migration files that were pulled down)
* `deactivate` (deactivat virtual env)
* `sudo systemctl start uwsgi` (start service again)
