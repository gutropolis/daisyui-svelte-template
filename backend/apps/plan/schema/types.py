from graphene_django import DjangoObjectType

from ..models import Feature, Permission, Plan


class PlanType(DjangoObjectType):
	class Meta:
		model = Plan
		fields = (
			'id',
			'slug',
			'name',
			'price',
			'duration_days',
			'max_users',
			'max_studies',
			'max_storage_gb',
			'features',
			'created_at',
			'updated_at',
		)


class FeatureType(DjangoObjectType):
	class Meta:
		model = Feature
		fields = '__all__'


class PermissionType(DjangoObjectType):
	class Meta:
		model = Permission
		fields = '__all__'
