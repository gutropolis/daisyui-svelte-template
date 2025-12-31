import graphene

from apps.plan.schema import PlanMutation, PlanQuery
from apps.subscription.schema import SubscriptionMutation, SubscriptionQuery
from apps.user.schema import UserMutation, UserQuery


class Query(UserQuery, PlanQuery, SubscriptionQuery, graphene.ObjectType):
	"""Root GraphQL query composed from every app-level query plus auth helpers."""


class Mutation(UserMutation, PlanMutation, SubscriptionMutation, graphene.ObjectType):
	"""Root GraphQL mutation composed from every app-level mutation plus auth flows."""


schema = graphene.Schema(query=Query, mutation=Mutation)
