from decimal import Decimal

import graphene

from ..models import Feature, Permission, Plan
from .types import FeatureType, PermissionType, PlanType
from .utils import serialize_feature_ids


# Input Types
class PlanInput(graphene.InputObjectType):
	slug = graphene.String()
	name = graphene.String(required=True)
	price = graphene.Decimal(required=False)
	duration_days = graphene.Int(required=True)
	max_users = graphene.Int()
	max_studies = graphene.Int()
	max_storage_gb = graphene.Int()
	features = graphene.List(graphene.Int)


class CreatePlanFeatureInput(graphene.InputObjectType):
	key_name = graphene.String(required=True)
	name = graphene.String(required=True)
	description = graphene.String()


class UpdatePlanFeatureInput(graphene.InputObjectType):
	key_name = graphene.String()
	name = graphene.String()
	description = graphene.String()


class CreatePermissionInput(graphene.InputObjectType):
	key_name = graphene.String(required=True)
	name = graphene.String(required=True)
	description = graphene.String()
	icon = graphene.String()
	feature_id = graphene.Int(required=True)


class UpdatePermissionInput(graphene.InputObjectType):
	key_name = graphene.String()
	name = graphene.String()
	description = graphene.String()
	icon = graphene.String()
	feature_id = graphene.Int()


# Response Types
class MutationResponse(graphene.ObjectType):
	success = graphene.Boolean()
	message = graphene.String()


class PlanMutationResponse(graphene.ObjectType):
	success = graphene.Boolean()
	message = graphene.String()
	data = graphene.Field(PlanType)


class FeatureMutationResponse(graphene.ObjectType):
	success = graphene.Boolean()
	message = graphene.String()
	data = graphene.Field(FeatureType)


class PermissionMutationResponse(graphene.ObjectType):
	success = graphene.Boolean()
	message = graphene.String()
	data = graphene.Field(PermissionType)


# Plan Mutations
class CreatePlan(graphene.Mutation):
	success = graphene.Boolean()
	message = graphene.String()
	data = graphene.Field(PlanType)

	class Arguments:
		input = PlanInput(required=True)

	@staticmethod
	def mutate(root, info, input):
		try:
			input_data = {key: value for key, value in input.items()}
			if not input_data.get('slug'):
				return CreatePlan(
					success=False,
					message='Slug is required',
					data=None
				)
			payload = {key: value for key, value in input_data.items() if value is not None}
			payload.setdefault('price', Decimal('0.00'))
			if 'features' in payload:
				payload['features'] = serialize_feature_ids(payload['features'])
			plan = Plan.objects.create(**payload)
			return CreatePlan(
				success=True,
				message='Plan created successfully',
				data=plan
			)
		except Exception as e:
			return CreatePlan(
				success=False,
				message=str(e),
				data=None
			)


class UpdatePlan(graphene.Mutation):
	success = graphene.Boolean()
	message = graphene.String()
	data = graphene.Field(PlanType)

	class Arguments:
		id = graphene.Int(required=True)
		input = PlanInput(required=True)

	@staticmethod
	def mutate(root, info, id, input):
		try:
			plan = Plan.objects.filter(pk=id).first()
			if not plan:
				return UpdatePlan(
					success=False,
					message='Plan not found',
					data=None
				)
			payload = {key: value for key, value in input.items() if value is not None}
			if 'features' in payload:
				payload['features'] = serialize_feature_ids(payload['features'])
			for field, value in payload.items():
				setattr(plan, field, value)
			plan.save()
			return UpdatePlan(
				success=True,
				message='Plan updated successfully',
				data=plan
			)
		except Exception as e:
			return UpdatePlan(
				success=False,
				message=str(e),
				data=None
			)


class DeletePlan(graphene.Mutation):
	success = graphene.Boolean()
	message = graphene.String()

	class Arguments:
		id = graphene.Int(required=True)

	@staticmethod
	def mutate(root, info, id):
		try:
			plan = Plan.objects.filter(pk=id).first()
			if not plan:
				return DeletePlan(
					success=False,
					message='Plan not found'
				)
			plan.delete()
			return DeletePlan(
				success=True,
				message='Plan deleted successfully'
			)
		except Exception as e:
			return DeletePlan(
				success=False,
				message=str(e)
			)


# Feature Mutations
class CreatePlanFeature(graphene.Mutation):
	success = graphene.Boolean()
	message = graphene.String()
	data = graphene.Field(FeatureType)

	class Arguments:
		input = CreatePlanFeatureInput(required=True)

	@staticmethod
	def mutate(root, info, input):
		try:
			feature = Feature.objects.create(
				key_name=input['key_name'],
				name=input['name'],
				description=input.get('description')
			)
			return CreatePlanFeature(
				success=True,
				message='Feature created successfully',
				data=feature
			)
		except Exception as e:
			return CreatePlanFeature(
				success=False,
				message=str(e),
				data=None
			)


class UpdatePlanFeature(graphene.Mutation):
	success = graphene.Boolean()
	message = graphene.String()
	data = graphene.Field(FeatureType)

	class Arguments:
		id = graphene.Int(required=True)
		input = UpdatePlanFeatureInput(required=True)

	@staticmethod
	def mutate(root, info, id, input):
		try:
			feature = Feature.objects.filter(pk=id).first()
			if not feature:
				return UpdatePlanFeature(
					success=False,
					message='Feature not found',
					data=None
				)
			for field, value in input.items():
				if value is not None:
					setattr(feature, field, value)
			feature.save()
			return UpdatePlanFeature(
				success=True,
				message='Feature updated successfully',
				data=feature
			)
		except Exception as e:
			return UpdatePlanFeature(
				success=False,
				message=str(e),
				data=None
			)


class DeletePlanFeature(graphene.Mutation):
	success = graphene.Boolean()
	message = graphene.String()

	class Arguments:
		id = graphene.Int(required=True)

	@staticmethod
	def mutate(root, info, id):
		try:
			feature = Feature.objects.filter(pk=id).first()
			if not feature:
				return DeletePlanFeature(
					success=False,
					message='Feature not found'
				)
			feature.delete()
			return DeletePlanFeature(
				success=True,
				message='Feature deleted successfully'
			)
		except Exception as e:
			return DeletePlanFeature(
				success=False,
				message=str(e)
			)


# Permission Mutations
class CreatePermission(graphene.Mutation):
	success = graphene.Boolean()
	message = graphene.String()
	data = graphene.Field(PermissionType)

	class Arguments:
		input = CreatePermissionInput(required=True)

	@staticmethod
	def mutate(root, info, input):
		try:
			permission = Permission.objects.create(
				key_name=input['key_name'],
				name=input['name'],
				description=input.get('description'),
				icon=input.get('icon'),
				feature_id=input['feature_id']
			)
			return CreatePermission(
				success=True,
				message='Permission created successfully',
				data=permission
			)
		except Exception as e:
			return CreatePermission(
				success=False,
				message=str(e),
				data=None
			)


class UpdatePermission(graphene.Mutation):
	success = graphene.Boolean()
	message = graphene.String()
	data = graphene.Field(PermissionType)

	class Arguments:
		id = graphene.Int(required=True)
		input = UpdatePermissionInput(required=True)

	@staticmethod
	def mutate(root, info, id, input):
		try:
			permission = Permission.objects.filter(pk=id).first()
			if not permission:
				return UpdatePermission(
					success=False,
					message='Permission not found',
					data=None
				)
			for field, value in input.items():
				if value is not None:
					setattr(permission, field, value)
			permission.save()
			return UpdatePermission(
				success=True,
				message='Permission updated successfully',
				data=permission
			)
		except Exception as e:
			return UpdatePermission(
				success=False,
				message=str(e),
				data=None
			)


class DeletePermission(graphene.Mutation):
	success = graphene.Boolean()
	message = graphene.String()

	class Arguments:
		id = graphene.Int(required=True)

	@staticmethod
	def mutate(root, info, id):
		try:
			permission = Permission.objects.filter(pk=id).first()
			if not permission:
				return DeletePermission(
					success=False,
					message='Permission not found'
				)
			permission.delete()
			return DeletePermission(
				success=True,
				message='Permission deleted successfully'
			)
		except Exception as e:
			return DeletePermission(
				success=False,
				message=str(e)
			)


# Main Mutation Object
class PlanMutation(graphene.ObjectType):
	# Plan mutations
	create_plan = CreatePlan.Field()
	update_plan = UpdatePlan.Field()
	delete_plan = DeletePlan.Field()

	# Feature mutations
	create_plan_feature = CreatePlanFeature.Field()
	update_plan_feature = UpdatePlanFeature.Field()
	delete_plan_feature = DeletePlanFeature.Field()

	# Permission mutations
	create_permission = CreatePermission.Field()
	update_permission = UpdatePermission.Field()
	delete_permission = DeletePermission.Field()
