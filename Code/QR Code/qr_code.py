import segno
import sys
import pymongo
from pymongo import MongoClient


# # Input for auth
print("Username : ")
username = input()
print("Password : ")
password = input()


cluster_url = "mongodb+srv://" + username + ":" + password + "@cluster0.qk8pnen.mongodb.net/"

try:
    cluster = MongoClient(cluster_url)
    db = cluster["Test"]
    collection = db["dataTest"]
    d = collection.find_one({"CompName": username}).get("Database")
except pymongo.errors.OperationFailure:
    print("Auth fail")
    sys.exit(1)

print("ItemID for QR creation : ")
itemID = int(input())

try:
    collection = db[d]
    retrievalDataObject = collection.find_one({"ItemID":itemID})
    itemName = retrievalDataObject.get("ItemName")
    origin = retrievalDataObject.get("Origin")
except pymongo.errors.OperationFailure:
    print("Auth fail2")
    sys.exit(1)

qrcode = segno.make_qr("ItemID = " + str(itemID) + "\n ItemName = " + itemName + "\n Origin = " + origin)
qrcode.save("qrcode_" + username + "_" + str(itemID) + ".png", scale = 5)
