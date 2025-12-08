"""User GraphQL module."""
from app.graphql.user.types import UserType
from app.graphql.user.queries import UserQuery
from app.graphql.user.mutations import UserMutation

__all__ = ["UserType", "UserQuery", "UserMutation"]
