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

class LinkMadeFromModel(Document):
    name = "test"
    field1 = StringField()
    field2 = StringField()
    field3 = StringField()

class LinkMakesModel(Document):
    name = "test2"
    field1 = StringField()
    field2 = StringField()
    field3 = StringField()

class Company(Document):

    meta = {"collection": "TestComp1"}
    ItemID = IntField()
    ItemName = StringField()
    Origin = StringField()
    IsNew = BooleanField()
    LinkMadeFrom = ListField(StringField())
    LinkMakes = ListField(StringField())

    # LinkMadeFrom = EmbeddedDocumentListField(LinkMadeFromModel)
    # LinkMakes = EmbeddedDocumentListField(LinkMakesModel)

    # LinkMadeFrom = LinkMadeFromModel()
    # LinkMakes = LinkMakesModel()

    # LinkMadeFrom = ListField(ListField(StringField()))
    # LinkMakes = ListField(ListField(StringField()))
    
    
