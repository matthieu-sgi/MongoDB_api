'''This module contains the class DBRequests'''

from bson.objectid import ObjectId

import mongodb_api.database_connection as db_connection

class DBRequests:
    '''This class contains the methods to request the database.'''
    def __init__(self, db_name : str) -> None:
        self.database = db_connection.DatabaseConnection(db_name).get_database()

    def get_collection(self, collection_name : str) -> list:
        '''This method is to get the collection.'''
        return self.database[collection_name]


    def get_one_document_by_id(self, collection_name : str, document_id : str) -> dict:
        '''This method is to get one document of a collection.'''
        # Convert string to ObjectId
        document_id = ObjectId(document_id)        
        return self.get_collection(collection_name).find_one({'_id': document_id})

    def get_one_document_by_title(self, collection_name : str, document_title : str) -> dict:
        '''This method is to get the first document of a collection.'''
        return self.get_collection(collection_name).find_one({"primaryTitle": document_title})

if __name__ == '__main__':
    pass