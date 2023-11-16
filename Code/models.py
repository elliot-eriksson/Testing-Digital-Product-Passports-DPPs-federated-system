from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    DateTimeField,
    ListField,
    ReferenceField,
    StringField,
    IntField,
)

class Company(Document):
    meta = {"collection": "TestComp1"}
    ItemID = IntField()
    ItemName = StringField()
    Origin = StringField()
