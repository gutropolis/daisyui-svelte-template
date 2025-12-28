import graphene

from ..models import Subscription
from .types import SubscriptionType


class SubscriptionQuery(graphene.ObjectType):
	subscriptions = graphene.List(
		SubscriptionType,
		user_id=graphene.ID(required=False),
		status=graphene.String(required=False),
	)
	subscription = graphene.Field(SubscriptionType, id=graphene.ID(required=True))

	def resolve_subscriptions(self, info, user_id=None, status=None):
		qs = Subscription.objects.select_related('user', 'plan').all()
		if user_id is not None:
			qs = qs.filter(user_id=user_id)
		if status is not None:
			qs = qs.filter(status=status)
		return qs

	def resolve_subscription(self, info, id):
		return Subscription.objects.select_related('user', 'plan').filter(pk=id).first()
