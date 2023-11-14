import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType

from models import Company as CompanyModel

class Item(MongoengineObjectType):
    class Meta:
        description = "Item"
        model = CompanyModel
        interfaces = (Node, )

class Query(graphene.ObjectType):
    node = Node.Field()

    all_item = MongoengineConnectionField(Item)

schema = graphene.Schema(query=Query, types=[Item])
