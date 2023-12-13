import segno
import sys
import json
import pymongo
import os

current_dir = os.path.dirname(os.path.realpath(__file__))

parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

from Authtest.authTest import authentication

db, d, username = authentication()

print("ItemID for QR creation : ")
itemID = int(input())

try:
    collection = db[d]
    retrievalDataObject = collection.find_one({"ItemID":itemID})
    itemName = retrievalDataObject.get("ItemName")
    origin = retrievalDataObject.get("Origin")
    LinkMadeFrom = str(retrievalDataObject.get("LinkMadeFrom"))
    LinkMakes = str(retrievalDataObject.get("LinkMakes"))
    #Det är så här vi vill ha de senare
   # link = retrievalDataObject.get("IPFS")
except pymongo.errors.OperationFailure:
    print("Auth fail2")
    sys.exit(1)

#Dictionary created with data
dataDictionary = {
    "ItemID": itemID,
    "ItemName": itemName,
    "Origin": origin,
    "LinkMadeFrom": LinkMadeFrom,
    "LinkMakes": LinkMakes
    
}
#Kommentera bort när link är implementerad
link = "https://hadea.ec.europa.eu/calls-proposals/digital-product-passport_en"

jsonData = json.dumps(dataDictionary)
qrcode = segno.make_qr(jsonData +"\n"+ link)
qrcode.save("qrcode_" + username + "_" + str(itemID) + ".png", scale = 5)
