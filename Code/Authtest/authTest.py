import pymongo
import sys
from pymongo import MongoClient

# For testing write username and password to skip input 
# username = ""
# password = ""

# Input for auth
print("Username : ")
username = input()
print("Password : ")
password = input()


cluster_url = "mongodb+srv://" + username + ":" + password + "@cluster0.qk8pnen.mongodb.net/"

# Retriving the company database
try:
    cluster = MongoClient(cluster_url)
    db = cluster["Test"]
    collection = db["dataTest"]
    d = collection.find_one({"CompName": username}).get("Database")
except pymongo.errors.OperationFailure:
    print("Auth fail")
    sys.exit(1)

# Input for new passport
print("Name : ")
ItemName = input()
print("Age : ")
Origin = input()

# Retriving new itemID and insterting new passport to company database
try:
    collection = db[d]
    retrievalDataObject = collection.find_one(sort=[("ItemID", pymongo.DESCENDING)])
    newItemID = retrievalDataObject.get("ItemID") + 1

    post = {"Person":newItemID, "Name":ItemName, "Age":Origin,}
    collection.insert_one(post)
except pymongo.errors.OperationFailure:
    print("Auth fail2")
    sys.exit(1)