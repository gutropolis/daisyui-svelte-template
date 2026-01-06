import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

User = get_user_model()


class UserType(DjangoObjectType):
    full_name = graphene.String()

    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "is_active", "date_joined", "role")

    def resolve_full_name(self, info):
        first = self.first_name or ""
        last = self.last_name or ""
        return f"{first} {last}".strip() or self.username