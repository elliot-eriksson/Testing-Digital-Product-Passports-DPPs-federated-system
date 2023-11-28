import pymongo
import sys
from pymongo import MongoClient

# For testing write username and password to skip input 

# username = ""
# password = ""


def authentication():
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
            if username == "sunlar3":
                d = "PassportAdress"
            else:
                d = collection.find_one({"CompName": username}).get("Database")
           
        except pymongo.errors.OperationFailure:
            print("Auth fail")
            sys.exit(1)
        return db, d, username
    