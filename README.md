# document-API

## How to use:

### Setup and run

Clone this repository with `git clone git@github.com:CAPGAGA/document-API.git`

Setup with docker compose via `docker-compose up -d`

After that, you can access API via `localhost:8000/docs`

## API endpoints and what they do

### User endpoints and requests

This application has simulated token-base access, meaning that all endpoints require a token in url path or body of the request. I don't use HEAD as some of the bots and scripts run in headless mode.

To acquire a token you need to send a `POST` request to the `/user/` endpoint with fields `email` and `password`

example:

```
curl -X 'POST' \
  'http://localhost:8000/user/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "cool@user.com",
  "password": "cooluserpass"
}'
```

success response example:

```
{
  "user": {
    "id": 1,
    "user_token": "rwTyBFXbmxGWoEpI",
    "email": "cool@user.com",
    "hashed_password": "cooluserpassyeahhased"
  },
  "token": "rwTyBFXbmxGWoEpI"
}
```

error response example:

```
{
  "detail": "User already exists"
}
```

After registration, you can view your credit and token via a `GET` request to `/user/mail/{your_email}/{your_password}`

example:

```
curl -X 'GET' \
  'http://localhost:8000/user/mail/cool@user.com/cooluserpass' \
  -H 'accept: application/json'
```

success response example:

```
{
  "id": 1,
  "user_token": "rwTyBFXbmxGWoEpI",
  "email": "cool@user.com",
  "hashed_password": "cooluserpassyeahhased"
}
```

error response example:

```
{
  "detail": "User not found"
}
```

The user profile can be edited (only email and password) via a `PUT` request to the `/user/` endpoint with the token, new email, and password in the body

example:

```
curl -X 'PUT' \
  'http://localhost:8000/user/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "newcool@user.com",
  "password": "newcooluserpass",
  "user_token": "rwTyBFXbmxGWoEpI"
}'
```

success response example:

```
{
  "user": {
    "id": 1,
    "user_token": "rwTyBFXbmxGWoEpI",
    "email": "newcool@user.com",
    "hashed_password": "cooluserpassyeahhased"
  },
}
```

error response example:

```
{
  "detail": "User not found"
}
```

Or deleted via a `DELETE` request to the `/user/` endpoint with your token in the body

example:

```
curl -X 'DELETE' \
  'http://localhost:8000/user/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_token": "rwTyBFXbmxGWoEpI"
}'
```

success response example:

```
null
```

error response example:

```
{
  "detail": "User not found"
}
```

That covers the basic crud process of user profile

### documents endpoints and requests

After user registration and acquiring a token you can access the crud mechanism of documents

To create a new document you need to send a `POST` request to `/document/{user_token}` with the document title and document contents in the body

example:

```
curl -X 'POST' \
  'http://localhost:8000/documents/rwTyBFXbmxGWoEpI' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "cooltitle",
  "contents": "coolcontents"
}'
```

success response example:

```
{
  "id": 1,
  "created_at": "2024-03-14T10:44:34.482090",
  "updated_at": null,
  "title": "cooltitle",
  "contents": "coolcontents",
  "owner_id": 7
}
```

error response example:

```
{
  "detail": "You are not registered"
}
```

You can get all documents via a `GET` request to `/documents/{user_token}`

example:

```
curl -X 'GET' \
  'http://localhost:8000/documents/rwTyBFXbmxGWoEpI' \
  -H 'accept: application/json'
```

success response example:

```
[
  {
    "id": 1,
    "created_at": "2024-03-14T10:44:34.482090",
    "updated_at": null,
    "title": "cooltitle",
    "contents": "coolcontents",
    "owner_id": 7
  }
]
```

error response example:

```
{
  "detail": "User with that token is not found"
}
```

As well as edit the document via a `PUT` request to `/documents/` with the token, document ID, new title, and contents in the body of the request

example:

```
curl -X 'PUT' \
  'http://localhost:8000/documents/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "newcooltitle",
  "contents": "newcoolcontents",
  "document_id": 1,
  "user_token": "rwTyBFXbmxGWoEpI"
}'
```

success response example:

```
{
  "document_id": 1,
  "user_token": "rwTyBFXbmxGWoEpI",
  "id": 1,
  "created_at": "2024-03-14T10:44:34.482090",
  "updated_at": "2024-03-14T10:46:56.992319",
  "title": "newcooltitle",
  "contents": "newcoolcontents",
  "owner_id": 1
}
```

error response example:

```
{
  "status_code": 404,
  "detail": "Document is not found",
  "headers": null
}
```

```
{
  "detail": "User with that token is not found"
}
```

To delete a document send a `DELETE` request to `/documents/` with the token and document ID in the body of the request

example:

```
curl -X 'DELETE' \
  'http://localhost:8000/documents/' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "document_id": 6,
  "user_token": "rwTyBFXbmxGWoEpI"
}'
```

That covers the crud mechanics of documents

## To stop the project

Use `docker-compose stop`

To delete project images, containers, volumes, and networks use `docker-compose down -v`
