import pymongo
from pymongo import MongoClient

def connection():
    try:
        cluster = MongoClient("Insert connection string here")  #online conneciton with MongoDB atlas
        # cluster = MongoClient("localhost", 27017)         #local connection with MongoDB compass
        db = cluster['Name of database here']         
        print("connected")
        return db
    except:
        raise Exception
    
db = connection()