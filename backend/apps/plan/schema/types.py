from graphene_django import DjangoObjectType
import graphene

from ..models import Feature, Permission, Plan
from .utils import deserialize_feature_ids


class PlanType(DjangoObjectType):
	features = graphene.List(graphene.Int)

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
			'created_at',
			'updated_at',
		)

	def resolve_features(self, info):
		return deserialize_feature_ids(self.features)


class FeatureType(DjangoObjectType):
	class Meta:
		model = Feature
		fields = (
			'id',
			'key_name',
			'name',
			'description',
			'created_at',
			'updated_at',
		)


class PermissionType(DjangoObjectType):
	feature_id = graphene.Int()

	class Meta:
		model = Permission
		fields = (
			'id',
			'key_name',
			'name',
			'description',
			'icon',
			'feature_id',
			'created_at',
			'updated_at',
		)

	def resolve_feature_id(self, info):
		return self.feature_id
