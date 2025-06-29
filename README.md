## :trophy: Challenge proposed by [Back-End Brasil](https://github.com/backend-br)
Link: https://github.com/backend-br/desafios/tree/master/cryptography
## 💻 Technologies:
Python
Django
Django Rest Framework
Cryptography Library (Symmetric encryption using Fernet)
SQLite3

## ❕ About:
REST API with CRUD operations for user information. The document and credit card token are encrypted before being stored in the database and decrypted when retrieved.

To create an user

```bash
POST /users/create
{
	"userDocument": "123456",
	"creditCardToken": "7654321",
	"value": 123123
}
```
To retrieve a list of all users registered

```bash
GET /users/list
```

To retrieve a user by an ID

```bash
GET /users/list/{id}
```

To update user information

```bash
PUT / PATCH /users/update/{id}
{
	"userDocument": "7890",
	"creditCardToken": "123456789",
	"value": 55555
}
```
To delete an user

```bash
DELETE /users/delete/{id}
```




## :gear: How to Run:
First, clone the project:
```bash
git clone https://github.com/gabrielzj/cryptography_challenge
``` 

Then, install the dependencies:
```bash
pip install -r requirements.txt
```
Apply migrations:
```bash
python manage.py migrate
```

Run the server:
```bash
python manage.py runserver
```
