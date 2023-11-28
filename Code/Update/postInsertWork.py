import pymongo
import sys
from bson import ObjectId


def postInsertWork(db, d):
   
    # Inserting passport address to PassportAdress collection
    try:
        collection = db[d]
        myquery = {"IsNew":True}
        retrievalDataObject = collection.find(myquery)
        for data in retrievalDataObject:
            _id = data.get("_id")
            linkMadeFrom = data.get("LinkMadeFrom")
            i = 0
            newLinkMadeFrom = []
            # while i < len(linkMadeFrom):
            #     newArray = "".join(linkMadeFrom[i]).replace(" ","").split(",")
            #     newArray[0] = ObjectId(newArray[0])
            #     newLinkMadeFrom.append(newArray)
            #     i += 1
            for item in linkMadeFrom:
                newArray = "".join(item).replace(" ","").split(",")
                newArray[0] = ObjectId(newArray[0])
                newLinkMadeFrom.append(newArray)

            # print(newLinkMadeFrom)
            # print(newLinkMadeFrom2)
            insertQuery = {"$set":{"LinkMadeFrom":newLinkMadeFrom}}
            collection.update_one({"_id":_id}, insertQuery)
    except pymongo.errors.OperationFailure:
        print("Auth fail2")
        sys.exit(1)