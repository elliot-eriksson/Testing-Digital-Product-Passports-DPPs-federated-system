import pymongo
import sys
from pymongo import MongoClient

print("Username : ")
username = input()
print("Password : ")
password = input()

cluster_url = "mongodb+srv://" + username + ":" + password + "@cluster0.qk8pnen.mongodb.net/"
print("mongodb+srv://TestComp1:TestComp1@cluster0.qk8pnen.mongodb.net/ \n" + cluster_url)
maxSevSelDelay = 1

try:
    cluster = MongoClient(cluster_url)
    db = cluster["Test"]
    collection = db["dataTest"]
    #collection = db["TestComp1"]
    cluster.admin.command('ismaster')
except pymongo.errors.OperationFailure:
    print("Auth fail")
    sys.exit(1)

retrievalDataObject = collection.find({},{'_id':0, 'CompID':0, 'CompName':0})

for data in retrievalDataObject:
    s = data['Database']
    print(s)

    #retrievalData = s[13:len(data)-2]
    
try:
    collection = db[s]
    post = {"ItemID":1, "ItemName":"Item1", "Origin":"Sweden",}
    collection.insert_one(post)

except pymongo.errors.OperationFailure:
    print("Auth fail2")
    sys.exit(1)

