from mongoengine import Document, EmbeddedDocument
from bson.objectid import ObjectId
from mongoengine.fields import (
    DateTimeField,
    ListField,
    ReferenceField,
    StringField,
    IntField,
    BooleanField,
)

class Company(Document):

    meta = {"collection": "TestComp1"}
    ItemID = IntField()
    ItemName = StringField()
    Origin = StringField()
    IsNew = BooleanField()
    ConnectingTo = ListField(StringField())
    ConnectingFrom = ListField(StringField())
    
