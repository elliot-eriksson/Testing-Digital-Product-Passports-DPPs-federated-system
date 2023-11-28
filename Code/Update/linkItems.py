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

def getCollectionAndQuery():
    # print("GetInforDATA", data)
    updateID = ObjectId(data[0])     #Takes the globalID and sets it as updateID
    collection = db["dataTest"]
    getDatabase = collection.find_one({"CompName": data[2]}).get("Database")
    collection = db[getDatabase]
    updateQuery = {"_id":updateID}
    return collection, updateQuery

# Retriving new itemID and insterting new passport to company database
try:
    collection = db[d]
    isNewPassportQuery = {"IsNew":True}
    newValue = {"$set": {"IsNew": False}}
    newPassports = collection.find(isNewPassportQuery)


    for data in newPassports:
        _id = data.get("_id")
        company = data.get("Database/collection")
        itemQuery = {"_id":_id}
        collection = db[company]                       #Sets collection as the one from passportAddress
        newItem = collection.find(itemQuery)
        
        for data in newItem:
            origin = data.get("Origin")
            name = data.get("ItemName")
            #myquery = {"_id":_id}
            madeArray = data.get("LinkMadeFrom")
            
            #Iterate through LinkMadeFrom and Update the linked items
            for data in madeArray:
                if data:
                    collection, updateQuery = getCollectionAndQuery()
                    newarray = [_id, name, company, origin]
                    updateValue = {"$push":{"LinkMakes": newarray}}
                    collection.update_one(updateQuery, updateValue)

            #Delete links in LinkMadeFrom and appends the previous passport links.
            newMadeArray = [item for item in madeArray if item != ""]
            i=0
            for data in madeArray:
                if data:
                    collection, updateQuery = getCollectionAndQuery()
                    madeByItem = collection.find(updateQuery)
                    for data in madeByItem:
                        linkMadeFrom = data.get("LinkMadeFrom")
                    if linkMadeFrom:
                        newMadeArray[i].append(linkMadeFrom)
                        i += 1

            # for data in madeArray:
            #     removeLink = {"$pop":{"LinkMadeFrom": -1}}
            #     collection.update_one(item_query, removeLink)
            
            # Update LinkMadeFrom with the modified list
            collection = db[company]
            insertQuery = {"$push":{"LinkMadeFrom": newMadeArray}}
            collection.update_one(itemQuery, {"$set":{"LinkMadeFrom":newMadeArray}})

        collection = db[d]
        collection.update_one(itemQuery, newValue)
except pymongo.errors.OperationFailure:
    print("Auth fail2")
    sys.exit(1)








