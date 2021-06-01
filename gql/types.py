from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

import models


class Post(SQLAlchemyObjectType):
    class Meta:
        model = models.Post
        interface = (relay.Node,)


class PostConnections(relay.Connection):
    class Meta:
        node = Post


class User(SQLAlchemyObjectType):
    posts = relay.ConnectionField(PostConnections)

    class Meta:
        model = models.User
        interface = (relay.Node,)


class UserConnections(relay.Connection):
    class Meta:
        node = User
