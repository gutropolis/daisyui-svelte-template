import graphene

from ..models import Feature, Permission, Plan
from .types import FeatureType, PermissionType, PlanType


class FilterPlansInput(graphene.InputObjectType):
	slug = graphene.String()
	name = graphene.String()


class FilterPermissionsInput(graphene.InputObjectType):
	key_name = graphene.String()
	name = graphene.String()
	feature_id = graphene.Int()


class PaginationType(graphene.ObjectType):
	page = graphene.Int()
	limit = graphene.Int()
	total = graphene.Int()
	total_pages = graphene.Int()
	has_next = graphene.Boolean()
	has_prev = graphene.Boolean()


class PaginatedPlansResponse(graphene.ObjectType):
	success = graphene.Boolean()
	message = graphene.String()
	data = graphene.List(PlanType)
	pagination = graphene.Field(PaginationType)


class PaginatedPermissionsResponse(graphene.ObjectType):
	success = graphene.Boolean()
	message = graphene.String()
	data = graphene.List(PermissionType)
	pagination = graphene.Field(PaginationType)


class FeatureListResponse(graphene.ObjectType):
	success = graphene.Boolean()
	message = graphene.String()
	data = graphene.List(FeatureType)


class PlanDetailResponse(graphene.ObjectType):
	success = graphene.Boolean()
	message = graphene.String()
	data = graphene.Field(PlanType)


class PlanQuery(graphene.ObjectType):
	# Plans queries
	plans = graphene.Field(
		PaginatedPlansResponse,
		page=graphene.Int(default_value=1),
		limit=graphene.Int(default_value=10),
		filter_input=FilterPlansInput()
	)
	plan = graphene.Field(PlanDetailResponse, id=graphene.Int())

	# Features queries
	plan_features = graphene.Field(FeatureListResponse)

	# Permissions queries
	permissions = graphene.Field(
		PaginatedPermissionsResponse,
		page=graphene.Int(default_value=1),
		limit=graphene.Int(default_value=10),
		filter_input=FilterPermissionsInput()
	)

	def resolve_plans(self, info, page=1, limit=10, filter_input=None):
		qs = Plan.objects.all().order_by('-created_at')

		if filter_input:
			if filter_input.get('slug'):
				qs = qs.filter(slug__icontains=filter_input['slug'])
			if filter_input.get('name'):
				qs = qs.filter(name__icontains=filter_input['name'])

		total = qs.count()
		start = (page - 1) * limit
		end = start + limit
		data = qs[start:end]

		return PaginatedPlansResponse(
			success=True,
			message='Plans retrieved successfully',
			data=data,
			pagination=PaginationType(
				page=page,
				limit=limit,
				total=total,
				total_pages=(total + limit - 1) // limit,
				has_next=end < total,
				has_prev=page > 1
			)
		)

	def resolve_plan(self, info, id):
		try:
			plan = Plan.objects.get(pk=id)
			return PlanDetailResponse(
				success=True,
				message='Plan retrieved successfully',
				data=plan
			)
		except Plan.DoesNotExist:
			return PlanDetailResponse(
				success=False,
				message='Plan not found',
				data=None
			)

	def resolve_plan_features(self, info):
		features = Feature.objects.all().order_by('name')
		return FeatureListResponse(
			success=True,
			message='Features retrieved successfully',
			data=features
		)

	def resolve_permissions(self, info, page=1, limit=10, filter_input=None):
		qs = Permission.objects.select_related('feature').all().order_by('name')

		if filter_input:
			if filter_input.get('key_name'):
				qs = qs.filter(key_name__icontains=filter_input['key_name'])
			if filter_input.get('name'):
				qs = qs.filter(name__icontains=filter_input['name'])
			if filter_input.get('feature_id'):
				qs = qs.filter(feature_id=filter_input['feature_id'])

		total = qs.count()
		start = (page - 1) * limit
		end = start + limit
		data = qs[start:end]

		return PaginatedPermissionsResponse(
			success=True,
			message='Permissions retrieved successfully',
			data=data,
			pagination=PaginationType(
				page=page,
				limit=limit,
				total=total,
				total_pages=(total + limit - 1) // limit,
				has_next=end < total,
				has_prev=page > 1
			)
		)
