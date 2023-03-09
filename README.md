# product-catalogue-api
A Product Catalog API that:
* Registers users.
* Verifies users accounts.
* Provides user login.
* Resets passwords of users.
* Possesses a Product Catalogue.
* Provides CRUD functionality to Product Catalog.

## Postman Documentation Link
Below is the documentation link for the API
https://documenter.getpostman.com/view/17582384/2s93Jru4Lk

## Running Locally?
To run this project locally:
* Pull or fork this repository.
* Change directory into product_catalogue_api -> `cd product_catalogue_api`
* Create a virtual enviroment -> `python -m venv .venv`
* Install neccessary dependencies -> `pip install -r requirements.txt`
* Check the env-template file to determine the ENVIROMENT VARIABLES you will need to get the project running and have them set up.
* Make migrations to the database -> `python manage.py makemigrations`
* Migrate -> `python manage.py makemigrations`
* Run server -> `python manage.py runserver`

##Dockerized Image
* `UPCOMING`
