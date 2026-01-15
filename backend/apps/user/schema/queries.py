import graphene
from django.contrib.auth import get_user_model
from django.db.models import Q
from graphql_auth.schema import UserQuery as AuthUserQuery
from .types import UserType

User = get_user_model()


class UserQuery(graphene.ObjectType):
    # Override the me field with custom UserType that includes full_name
    me = graphene.Field(UserType)
    # Inherit user and users from AuthUserQuery
    user = AuthUserQuery.user
    users = AuthUserQuery.users
    all_users = graphene.List(UserType, search=graphene.String(), is_active=graphene.Boolean())

    def resolve_me(self, info):
        user = info.context.user
        if user.is_authenticated:
            return user
        return None

    def resolve_all_users(self, info, search=None, is_active=True):
        qs = User.objects.all()
        if is_active is True:
            qs = qs.filter(is_active=True)
        if search:
            qs = qs.filter(
                Q(first_name__icontains=search)
                | Q(last_name__icontains=search)
                | Q(email__icontains=search)
                | Q(username__icontains=search)
            )
        return qs.order_by('first_name', 'last_name', 'email')