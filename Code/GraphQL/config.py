def configLogin():
    DATABASE = 'Test'
    print("Company: ")
    COMPANY = input()
    print("Password: ")
    PASSWORD = input()
    return DATABASE, COMPANY, PASSWORD

def configCollection():
    print("Collection: ")
    COLLECTION = input()
    return COLLECTION