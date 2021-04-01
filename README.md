# API ECOMERCE

you need to install python 3.8.7 in https://www.python.org/downloads/release/python-387/

you should be create a virtual environment:

- pip install virtualenv


- virtualenv myenv


- if you are in windows -> cd myenv\Scripts\activate

## EXECUTE THE APPLICATION

- For first time Install the requeriments -> pip install -r requirements.txt


- Edit -env file with your information

- execute -> flask db init

- execute -> flask db migrate -m "start"

- execute -> flask db upgrade

- execute in terminal -> flask run

¡Important¡ 

This API use an ORM, so you must to create a database and put the name in .env file

In creation I used postgresql. If you want to use other database engine so you have to edit config.py appropriately 
