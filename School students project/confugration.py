from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://albert:albert9090@todo.58rwtsz.mongodb.net/?appName=todo"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


db =  client.todo
collections = db['school_data']