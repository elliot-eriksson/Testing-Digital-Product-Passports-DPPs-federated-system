import segno
import pymongo
import sys
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
except pymongo.errors.OperationFailure:
    print("Auth fail2")
    sys.exit(1)

qrcode = segno.make_qr("ItemID = " + str(itemID) + "\nItemName = " + itemName + "\nOrigin = " + origin)
qrcode.save("qrcode_" + username + "_" + str(itemID) + ".png", scale = 5)
