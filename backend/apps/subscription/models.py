from django.conf import settings
from django.db import models

from apps.plan.models import Plan


class Subscription(models.Model):
	class Status(models.TextChoices):
		ACTIVE = 'ACTIVE', 'Active'
		CANCELED = 'CANCELED', 'Canceled'
		EXPIRED = 'EXPIRED', 'Expired'

	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscriptions')
	plan = models.ForeignKey(Plan, on_delete=models.PROTECT, related_name='subscriptions')
	start_date = models.DateField()
	end_date = models.DateField()
	status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
	paid_status = models.BooleanField(default=False)
	auto_renew = models.BooleanField(default=True)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

	class Meta:
		db_table = 'proxmed_subscriptions'
		verbose_name = 'Subscription'
		verbose_name_plural = 'Subscriptions'
		ordering = ['-created_at']
		indexes = [
			models.Index(fields=['user'], name='ix_subscriptions_user_id'),
			models.Index(fields=['plan'], name='ix_subscriptions_plan_id'),
		]

	def __str__(self) -> str:
		return f"{self.user} → {self.plan} ({self.status})"
