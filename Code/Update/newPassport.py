import pymongo
import sys
from bson import ObjectId
from pymongo import MongoClient

import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))

parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

from Authtest.authTest import authentication
from Update.postInsertWork import postInsertWork

db, d , username = authentication()



# Inserting passport address to PassportAdress collection
try:
    collection = db[d]
    postInsertWork(db,d)
    myquery = {"IsNew":True}
    retrievalDataObject = collection.find(myquery)
    i=0
    for data in retrievalDataObject:
        _id = data.get("_id")
        post = {"_id":_id, "Database/collection":d, "IsNew":True}
        collection = db["PassportAdress"]
        collection.insert_one(post)
        i += 1
        collection = db[d]
        newValue = {"$set": {"IsNew": False}}
        myquery = {"_id":_id}
        collection.update_one(myquery, newValue)  
except pymongo.errors.OperationFailure:
    print("Auth fail2")
    sys.exit(1)

print("Number of inserts: ", i)