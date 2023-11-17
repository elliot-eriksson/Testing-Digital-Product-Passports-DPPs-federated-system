import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType

from models import Company as CompanyModel

class Item(MongoengineObjectType):
    class Meta:
        description = "Item"
        model = CompanyModel
        interfaces = (Node, )


class UpdateItem(graphene.Mutation):
    class Arguments:
        global_ID = graphene.ID(required = True)
        name =  graphene.String()
        origin = graphene.String()
        
    item = graphene.Field(lambda: Item)

    def mutate(self, info, global_ID, name = None, origin = None):
        company = CompanyModel.objects.get(id=global_ID)
        if name is not None:
            company.ItemName = name
        if origin is not None:
            company.Origin = origin
        
        company.save()
        return UpdateItem(item=company)

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
    update_item = UpdateItem.Field()

class Query(graphene.ObjectType):
    class Mutation(graphene.ObjectType):
        create_item = CreateItem.Field()
        update_item = UpdateItem.Field()
    node = Node.Field()
    all_item = MongoengineConnectionField(Item)    
    item = graphene.Field(Item, item_id=graphene.Int(required=True))

    def resolve_item(self, info, item_id):
        item = CompanyModel.objects(ItemID=item_id).first()
        return item
    
schema = graphene.Schema(query=Query, mutation=Mutation, types=[Item])

    