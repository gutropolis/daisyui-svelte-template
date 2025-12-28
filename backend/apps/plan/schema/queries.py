import graphene

from ..models import Feature, Permission, Plan
from .types import FeatureType, PermissionType, PlanType


class PlanQuery(graphene.ObjectType):
	plans = graphene.List(PlanType, order=graphene.String(default_value='-created_at'))
	plan = graphene.Field(PlanType, id=graphene.ID(), slug=graphene.String())
	features = graphene.List(FeatureType)
	permissions = graphene.List(PermissionType, feature_id=graphene.ID())

	def resolve_plans(self, info, order):
		return Plan.objects.all().order_by(order)

	def resolve_plan(self, info, id=None, slug=None):
		if id is not None:
			return Plan.objects.filter(pk=id).first()
		if slug is not None:
			return Plan.objects.filter(slug=slug).first()
		return None

	def resolve_features(self, info):
		return Feature.objects.all()

	def resolve_permissions(self, info, feature_id=None):
		qs = Permission.objects.select_related('feature').all()
		if feature_id is not None:
			qs = qs.filter(feature_id=feature_id)
		return qs
