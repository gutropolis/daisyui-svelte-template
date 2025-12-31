import graphene
from graphql_auth.schema import MeQuery, UserQuery as AuthUserQuery
from .types import UserType


class UserQuery(MeQuery, AuthUserQuery, graphene.ObjectType):
    # Additional user queries can be added here
    # For example, user profile, user list, etc.
    pass