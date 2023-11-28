from mongoengine import Document
from config import configCollection
from mongoengine.fields import (
    DateTimeField,
    ListField,
    StringField,
    IntField,
    BooleanField
)
COLLECTION = configCollection()

class Company(Document):

    # print("Collecion: ")
    # col = input()

    meta = {"collection": COLLECTION}
    ItemID = IntField()
    ItemName = StringField()
    Origin = StringField()
    IsNew = BooleanField()
    LinkMadeFrom = ListField(StringField())
    LinkMakes = ListField(StringField())
    