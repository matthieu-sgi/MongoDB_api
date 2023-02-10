'''This module is to create an object to connect to the database.'''
from pymongo import MongoClient, errors

class DatabaseConnection:
    '''This class is to create an object to connect to the database.'''
    def __init__(self, database_name, address : str = 'localhost', port : int = 27017):
        try:
            self.client = MongoClient(f'mongodb://{address}:{port}/')
            self.database = self.client[database_name]
        except errors.ConnectionFailure as error:
            print(error)

    def get_database(self):
        '''This method is to get the database.'''
        return self.database
