from graphene_django import DjangoObjectType

from ..models import Subscription


class SubscriptionType(DjangoObjectType):
	class Meta:
		model = Subscription
		fields = '__all__'
