from mongoengine import Document
from mongoengine.fields import (
    DateTimeField,
    ListField,
    StringField,
    IntField,
    BooleanField
)




class Company(Document):

    meta = {"collection": "VOLVO"}
    ItemID = IntField()
    ItemName = StringField()
    Origin = StringField()
    IsNew = BooleanField()
    LinkMadeFrom = ListField(StringField())
    LinkMakes = ListField(StringField())
    