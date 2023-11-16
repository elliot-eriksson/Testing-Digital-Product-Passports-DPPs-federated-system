import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType

from models import Company as CompanyModel

class Item(MongoengineObjectType):
    class Meta:
        description = "Item"
        model = CompanyModel
        interfaces = (Node, )



class CreateItem(graphene.Mutation):
    class Arguments:
        item_id = graphene.Int(required=True)
        item_name = graphene.String(required=True)
        origin = graphene.String()

    item = graphene.Field(lambda: Item)

    def mutate(self, info, item_id, item_name, origin=None):
        company = CompanyModel(ItemID=item_id, ItemName=item_name, Origin=origin)
        company.save()
        return CreateItem(item=company)

class Mutation(graphene.ObjectType):
    create_item = CreateItem.Field()

class Query(graphene.ObjectType):
    class Mutation(graphene.ObjectType):
        create_item = CreateItem.Field()
    node = Node.Field()

    all_item = MongoengineConnectionField(Item)    

schema = graphene.Schema(query=Query, mutation=Mutation, types=[Item])

    