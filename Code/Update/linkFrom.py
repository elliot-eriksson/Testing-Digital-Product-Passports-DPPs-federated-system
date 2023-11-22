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

db, d , username = authentication()
print(db)
print(d)


# Retriving new itemID and insterting new passport to company database
try:
    collection = db[d]
    myquery = {"IsNew":True}
    retrievalDataObject = collection.find(myquery)
    for data in retrievalDataObject:
        # print(data)
        _id = data.get("_id")
        company = "TestComp1"
        origin = data.get("Origin")
        name = data.get("ItemName")
        newValue = {"$set": {"IsNew": False}}
        myquery = {"_id":_id}
        # print(myquery)
        madeArray = data.get("ConnectingTo")
        # print("testprint ", madeArray)
        for data in madeArray:
            # print(data)
            if data != "":
                updateID = ObjectId(data[0])     #Takes the globalID and sets it as updateID
                collection = db["dataTest"]
                getDatabase = collection.find_one({"CompName": data[2]}).get("Database")
                collection = db[getDatabase]
                updateQuery = {"_id":updateID}
                newarray = [_id, name, company, origin]
                updateValue = {"$push":{"ConnectingFrom": newarray}}
                collection.update_one(updateQuery, updateValue)
            collection = db[d]
        # collection.update_one(myquery, newValue)

except pymongo.errors.OperationFailure:
    print("Auth fail2")
    sys.exit(1)








