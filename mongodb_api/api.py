'''This module contains the API class that is used to interact with the MongoDB database.'''

from fastapi import FastAPI
from mongodb_api.db_requests import DBRequests
from pydantic import BaseModel

import json

app = FastAPI()

db_name = 'IMDB_database'
db_collection_title = 'basic.title'


class Item(BaseModel):
    '''This class is to create the model of the item.'''
    _id : str
    tconst: str
    titleType: str
    primaryTitle: str
    originalTitle: str
    isAdult: str
    startYear: str
    endYear: str
    runtimeMinutes: str
    genres: str


@app.get('/')
async def root():
    '''This method is to get the root of the API.'''
    return {'message': 'Welcome to the API'}


def db_dumps(entry : dict) -> json :
    '''This method is to convert the input to json.'''
    entry['_id'] = str(entry['_id'])
    return json.dumps(entry)


@app.get('/api/v1/id={document_id}')
async def get_one_document_by_id(document_id : str):
    '''This method is to get one document by id of the title.basic collection.'''
    db = DBRequests(db_name)

    res = db.get_one_document_by_id(db_collection_title, document_id)
    # Convert ObjectId to string
    return db_dumps(res)

@app.get('/api/v1/title={document_title}')
async def get_one_document_by_name(document_title : str):
    '''This method is to get the first document of a collection.'''
    res = DBRequests(db_name).get_one_document_by_title(db_collection_title, document_title)
    # Convert ObjectId to string
    res['_id'] = str(res['_id'])
    return json.dumps(res)