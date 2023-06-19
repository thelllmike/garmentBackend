from pymongo import MongoClient

client= MongoClient("mongodb+srv://sachinharshitha971:6OejzKCjbhuLOUQL@cluster0.1hdmgbm.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_db

collection_name = db["todo_collection"]