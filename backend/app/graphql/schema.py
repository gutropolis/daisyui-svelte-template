"""GraphQL Schema combining all modules."""
import strawberry
from typing import Optional

from app.graphql.auth import AuthQuery, AuthMutation
from app.graphql.user import UserQuery, UserMutation
from app.graphql.project import ProjectQuery, ProjectMutation
from app.graphql.plan_feature import PlanFeatureQuery, PlanFeatureMutation
from app.graphql.permission import PermissionQuery, PermissionMutation
from app.graphql.plan import PlanQuery, PlanMutation


@strawberry.type
class Query(AuthQuery, UserQuery, ProjectQuery, PlanFeatureQuery, PermissionQuery, PlanQuery):
    """Root Query type combining all module queries."""

    @strawberry.field
    def hello(self) -> str:
        """Simple hello world query."""
        return "Welcome to DaisyUI Healthcare GraphQL API!"


@strawberry.type
class Mutation(AuthMutation, UserMutation, ProjectMutation, PlanFeatureMutation, PermissionMutation, PlanMutation):
    """Root Mutation type combining all module mutations."""

    @strawberry.mutation
    def ping(self) -> str:
        """Ping endpoint for health check."""
        return "pong"


# Create the schema
schema = strawberry.Schema(query=Query, mutation=Mutation)
