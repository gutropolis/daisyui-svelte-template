import graphene
from django.contrib.auth import get_user_model

from apps.plan.models import Plan
from ..models import Subscription
from .types import SubscriptionType

User = get_user_model()
SubscriptionStatusEnum = graphene.Enum.from_enum(Subscription.Status)


class SubscriptionInput(graphene.InputObjectType):
	user_id = graphene.ID(required=True)
	plan_id = graphene.ID(required=True)
	start_date = graphene.Date(required=True)
	end_date = graphene.Date(required=True)
	status = SubscriptionStatusEnum(required=False)
	paid_status = graphene.Boolean(required=False)
	auto_renew = graphene.Boolean(required=False)


class CreateSubscription(graphene.Mutation):
	subscription = graphene.Field(SubscriptionType)

	class Arguments:
		input = SubscriptionInput(required=True)

	@staticmethod
	def mutate(root, info, input):
		user = User.objects.get(pk=input.user_id)
		plan = Plan.objects.get(pk=input.plan_id)
		payload = {key: value for key, value in input.items() if key not in {'user_id', 'plan_id'} and value is not None}
		subscription = Subscription.objects.create(user=user, plan=plan, **payload)
		return CreateSubscription(subscription=subscription)


class UpdateSubscriptionStatus(graphene.Mutation):
	subscription = graphene.Field(SubscriptionType)

	class Arguments:
		id = graphene.ID(required=True)
		status = SubscriptionStatusEnum(required=True)
		paid_status = graphene.Boolean(required=False)
		auto_renew = graphene.Boolean(required=False)

	@staticmethod
	def mutate(root, info, id, status, paid_status=None, auto_renew=None):
		subscription = Subscription.objects.filter(pk=id).first()
		if not subscription:
			raise ValueError('Subscription not found')
		subscription.status = status
		if paid_status is not None:
			subscription.paid_status = paid_status
		if auto_renew is not None:
			subscription.auto_renew = auto_renew
		subscription.save(update_fields=['status', 'paid_status', 'auto_renew', 'updated_at'])
		return UpdateSubscriptionStatus(subscription=subscription)


class SubscriptionMutation(graphene.ObjectType):
	create_subscription = CreateSubscription.Field()
	update_subscription_status = UpdateSubscriptionStatus.Field()
