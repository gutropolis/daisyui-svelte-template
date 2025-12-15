from django.conf import settings
from django.db import models
from django.utils import timezone
from config.mixins import TimestampMixin, AuditMixin


class Project(TimestampMixin, AuditMixin):
    class Purpose(models.TextChoices):
        PRACTICE = "practice", "Practice"
        RESEARCH = "research", "Research"
        QUALITY = "quality", "Quality"
        OTHER = "other", "Other"

    class Status(models.TextChoices):
        DEVELOPMENT = "development", "Development"
        PRODUCTION = "production", "Production"
        INACTIVE = "inactive", "Inactive"

    title = models.CharField(max_length=250)
    code = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    purpose = models.CharField(
        max_length=20,
        choices=Purpose.choices,
        default=Purpose.OTHER,
    )
    is_longitudinal = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices=Status,
        default=Status.DEVELOPMENT,
    )
   
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        db_table = "proxmed_project"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["-publish"]),
        ]

    def __str__(self) -> str:
        return self.title