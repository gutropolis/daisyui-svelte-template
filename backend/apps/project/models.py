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


class ProjectSetting(TimestampMixin, AuditMixin):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="settings",
    )
    setting_key = models.CharField(max_length=100)
    setting_value = models.TextField()

    class Meta:
        verbose_name = "ProjectSetting"
        verbose_name_plural = "ProjectSettings" 
        db_table = "proxmed_project_settings"

    def __str__(self) -> str:
        return f"{self.project.title} - {self.setting_key}"


class Arm(TimestampMixin, AuditMixin):
    arm_id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="arms",
    )
    arm_num = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "ProjectArm"
        verbose_name_plural = "ProjectArms" 
        db_table = "proxmed_project_arms" 

    def __str__(self) -> str:
        return f"{self.project.title} - Arm {self.arm_num}"


class Event(TimestampMixin, AuditMixin):
    event_id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="events",
    )
    arm = models.ForeignKey(
        Arm,
        on_delete=models.CASCADE,
        related_name="events",
    )
    event_num = models.IntegerField()
    name = models.CharField(max_length=255)
    offset_days = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "ProjectEvent"
        verbose_name_plural = "ProjectEvents" 
        db_table = "proxmed_project_events"

    def __str__(self) -> str:
        return f"{self.project.title} - Event {self.event_num}"


class ProjectUser(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="project_users",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="project_memberships",
    )
    role_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "ProjectUser"
        verbose_name_plural = "ProjectUsers"
        db_table = "proxmed_project_users"
        unique_together = (('project', 'user'),)

    def __str__(self) -> str:
        return f"{self.project.title} - {self.user} ({self.role_name})"