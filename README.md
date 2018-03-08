AEC History Prototype
=====================

How to run:

1. Install `pipenv`
#. To install the requirements run `pipenv install --three`
#. make a new superuser `pipenv run django-admin createsuperuser`
#. Migrate the database `pipenv run django-admin migrate`
#. Load the data `pipenv run ./scripts/load_data.sh`
#. To start the server run `pipenv run honcho start`
