import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField

from gql import types


class Query(graphene.ObjectType):
    say_hello = graphene.String(name=graphene.String(default_value="Test Driven"))

    all_users = SQLAlchemyConnectionField(types.UserConnections)
    all_posts = SQLAlchemyConnectionField(types.PostConnections)

    @staticmethod
    def resolve_say_hello(parent, info, name):
        return f"Hello {name}"


schema = graphene.Schema(query=Query)
