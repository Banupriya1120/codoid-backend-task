# codoid-backend-task
python manage.py migrate
Run Server: 
python manage.py runserver

JWT Task:

Registration:
API: http://localhost:8000/api/register
Request:
{
    "name": "banu",
    "email": "banu@gmail.com",
    "password": "banu"
}
Method: POST
---------------------------------
Login:
API: http://localhost:8000/api/login
Request:
{
    "email": "banu@gmail.com",
    "password": "banu"
}
Method: POST
-------------------------------------
Rest API Task:

Create:
API: http://localhost:8000/api/book-create
Request:
{
    "title": "book1",
    "no_of_pages": 300,
    "publish_date": "2021-10-10",
    "quantity": 200
}
Method: POST
---------------------------------------
Book Details:
API: http://localhost:8000/api/book/:id
Method: GET
---------------------------------------
Update:
API: http://localhost:8000/api/book-update/:id
Request:
{
    "title": "book1",
    "no_of_pages": 300,
    "publish_date": "2021-10-10",
    "quantity": 200
}
Method: PUT
-----------------------------------
All Books:
API: http://localhost:8000/api/books
Method: GET
-----------------------------------
All Books:
API: http://localhost:8000/api/book-delete
Method: DELETE
-----------------------------------
