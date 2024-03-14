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

```

success response example:

```

```

error response example:

```

```

After registration, you can view your credit and token via a `GET` request to `/user/{your_email}/{your_password}`

example:

```

```

success response example:

```

```

error response example:

```

```

The user profile can be edited (only email and password) via a `PUT` request to the `/user/` endpoint with the token, new email, and password in the body

example:

```

```

success response example:

```

```

error response example:

```

```

Or deleted via a `DELETE` request to the `/user/` endpoint with your token in the body

example:

```

```

success response example:

```

```

error response example:

```

```

That covers the basic crud process of user profile

### documents endpoints and requests

After user registration and acquiring a token you can access the crud mechanism of documents

To create a new document you need to send a `POST` request to `/document/{user_token}` with the document title and document contents in the body

example:

```

```

success response example:

```

```

error response example:

```

```

You can get all documents via a `GET` request to `/documents/{user_token}`

example:

```

```

success response example:

```

```

error response example:

```

```

As well as edit the document via a `PUT` request to `/documents/` with the token, document ID, new title, and contents in the body of the request

example:

```

```

success response example:

```

```

error response example:

```

```

To delete a document send a `DELETE` request to `/documents/` with the token and document ID in the body of the request

example:

```

```

success response example:

```

```

error response example:

```

```

That covers the crud mechanics of documents

## To stop the project

Use `docker-compose stop`

To delete project images, containers, volumes, and networks use `docker-compose down -v`
