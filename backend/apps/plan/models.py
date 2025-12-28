from decimal import Decimal

from django.db import models


class Plan(models.Model):
	slug = models.SlugField(max_length=100, unique=True, db_index=True)
	name = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
	duration_days = models.PositiveIntegerField()
	max_users = models.PositiveIntegerField(null=True, blank=True)
	max_studies = models.PositiveIntegerField(null=True, blank=True)
	max_storage_gb = models.PositiveIntegerField(null=True, blank=True)
	features = models.CharField(max_length=500, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'proxmed_plans'
		verbose_name = 'Plan'
		verbose_name_plural = 'Plans'
		ordering = ['-created_at']
		indexes = [models.Index(fields=['slug'], name='ix_plans_slug')]

	def __str__(self) -> str:
		return self.name




class Feature(models.Model):
	key_name = models.CharField(max_length=100, unique=True, db_index=True)
	name = models.CharField(max_length=255)
	description = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'proxmed_plan_features'
		verbose_name = 'Feature'
		verbose_name_plural = 'Features'
		ordering = ['name']
		indexes = [models.Index(fields=['key_name'], name='ix_plan_features_key_name')]

	def __str__(self) -> str:
		return self.name


class Permission(models.Model):
	key_name = models.CharField(max_length=150, unique=True, db_index=True)
	name = models.CharField(max_length=255)
	description = models.TextField(null=True, blank=True)
	icon = models.CharField(max_length=100, null=True, blank=True)
	feature = models.ForeignKey(Feature, on_delete=models.PROTECT, related_name='permissions')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'proxmed_permissions'
		verbose_name = 'Permission'
		verbose_name_plural = 'Permissions'
		ordering = ['name']
		indexes = [
			models.Index(fields=['key_name'], name='ix_permissions_key_name'),
			models.Index(fields=['feature'], name='ix_permissions_feature_id')
		]

	def __str__(self) -> str:
		return self.name
