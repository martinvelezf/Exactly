
First check if your system has 

*Python 3.6
*pipenv --install using (pip3 install pipenv)

*sqlite3
if you dont have sqlite you can use on linux
    sudo apt-get install sqlite3 libsqlite3-dev


To start the app
Run 
>>pipenv install
>>pipenv run python manage.py runserver

Test url

CRUD incident
http://127.0.0.1:8000/admin/app/incident/

CRUD updates
http://127.0.0.1:8000/admin/app/updates/

Admin Panel 
http://127.0.0.1:8000/admin

See list of incident
http://127.0.0.1:8000

Create admin user
>>pipenv run python manage.py createsuperuser

The database file has one aviable 
username: martin
password: 1234
