from mongoengine import Document, EmbeddedDocument
from bson.objectid import ObjectId
from mongoengine.fields import (
    DateTimeField,
    ListField,
    ReferenceField,
    StringField,
    IntField,
)

class Company(Document):
    meta = {"collection": "TestComp1"}
    _id = ObjectId()
    ItemID = IntField()
    ItemName = StringField()
    Origin = StringField()