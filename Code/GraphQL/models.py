from mongoengine import Document, EmbeddedDocument
from bson.objectid import ObjectId
from mongoengine.fields import (
    DateTimeField,
    ListField,
    ReferenceField,
    StringField,
    IntField,
    BooleanField,
    EmbeddedDocumentListField,
    EmbeddedDocument
)


class Company(Document):

    meta = {"collection": "TestComp1"}
    ItemID = IntField()
    ItemName = StringField()
    Origin = StringField()
    IsNew = BooleanField()
    LinkMadeFrom = ListField(StringField())
    LinkMakes = ListField(StringField())
    