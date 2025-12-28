from decimal import Decimal

import graphene

from ..models import Plan
from .types import PlanType


class PlanInput(graphene.InputObjectType):
	slug = graphene.String(required=True)
	name = graphene.String(required=True)
	price = graphene.Decimal(required=False)
	duration_days = graphene.Int(required=True)
	max_users = graphene.Int()
	max_studies = graphene.Int()
	max_storage_gb = graphene.Int()
	features = graphene.String()


class CreatePlan(graphene.Mutation):
	plan = graphene.Field(PlanType)

	class Arguments:
		input = PlanInput(required=True)

	@staticmethod
	def mutate(root, info, input):
		payload = {key: value for key, value in input.items() if value is not None}
		payload.setdefault('price', Decimal('0.00'))
		plan = Plan.objects.create(**payload)
		return CreatePlan(plan=plan)


class UpdatePlan(graphene.Mutation):
	plan = graphene.Field(PlanType)

	class Arguments:
		id = graphene.ID(required=True)
		input = PlanInput(required=True)

	@staticmethod
	def mutate(root, info, id, input):
		plan = Plan.objects.filter(pk=id).first()
		if not plan:
			raise ValueError('Plan not found')
		for field, value in input.items():
			if value is not None:
				setattr(plan, field, value)
		plan.save()
		return UpdatePlan(plan=plan)


class PlanMutation(graphene.ObjectType):
	create_plan = CreatePlan.Field()
	update_plan = UpdatePlan.Field()
