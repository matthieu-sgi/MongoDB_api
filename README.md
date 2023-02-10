# MongoDB api project for the Hack and Puzzle course

This project is a simple api for a MongoDB database. It is used to store and retrieve data from a database.

This project uses the following technologies:
- Python
- FastAPI
- MongoDB
- Docker

## Installation and run

To install the project, clone the repository and compose the docker the requirements:

```bash
docker-compose build
```

Then run the docker-compose file:

```bash
docker-compose up
```

The api is now running on `http://localhost:8000/`.

To stop the docker-compose, use `Ctrl+C` and then:

```bash
docker-compose down
```


## Usage

To fill the database with data, I use mongodb-compass. You can download it [here](https://www.mongodb.com/products/compass).

## Architecture

The project is divided into 2 main parts:
- The database
- The api

The database is a MongoDB database. It is running in a docker container. The api is a FastAPI application also running in a docker. It is used to communicate with the database.

In [mongodb_api/](mongodb_api) directory you can find `database_connection` and `db_requests` files. These files are used to connect to the database and to send requests to it.

In [mongodb_api/api.py](mongodb_api/api.py) file you can find the api file. It contains the routes and the functions used to handle the requests.