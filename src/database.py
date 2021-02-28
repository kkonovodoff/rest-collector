from pymongo import MongoClient

from singletonMeta import SingletonMeta

class Database(metaclass=SingletonMeta):
    def __init__(self, host='localhost', port=27017):
        self.client = MongoClient(host=host, port=port)
        self.database = self.client.rest_collector

    def getDatabase(self):
        return self.database

