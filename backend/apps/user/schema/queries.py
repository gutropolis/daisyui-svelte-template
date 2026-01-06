import graphene
from graphql_auth.schema import UserQuery as AuthUserQuery
from .types import UserType


class UserQuery(graphene.ObjectType):
    # Override the me field with custom UserType that includes full_name
    me = graphene.Field(UserType)
    # Inherit user and users from AuthUserQuery
    user = AuthUserQuery.user
    users = AuthUserQuery.users

    def resolve_me(self, info):
        user = info.context.user
        if user.is_authenticated:
            return user
        return None