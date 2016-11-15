from pymongo import MongoClient

mongo = MongoClient("mongodb://localhost:27017/Impactr")
db = mongo.get_default_database()
