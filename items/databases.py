from pymongo import MongoClient


# Connects to the MongoDB database and get the "items" collection in the "pinterest" database
client = MongoClient("mongodb://localhost:27017")
db = client['pinterest']
collection = db['items']
