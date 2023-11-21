import segno
import sys
import pymongo
from authTest import authentication

db, d, username = authentication()

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

qrcode = segno.make_qr("ItemID = " + str(itemID) + "\nItemName = " + itemName + "\nOrigin = " + origin)
qrcode.save("qrcode_" + username + "_" + str(itemID) + ".png", scale = 5)
