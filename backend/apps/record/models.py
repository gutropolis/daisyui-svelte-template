from django.db import models
from config.mixins import TimestampMixin, AuditMixin


class Record(TimestampMixin, AuditMixin):
    record_id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        related_name='records',
    )
    record_key = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Records'
        db_table = 'proxmed_records'
        unique_together = (('project', 'record_key'),)

    def __str__(self) -> str:
        return f"{self.project.title} - {self.record_key}"


class DataValue(models.Model):
    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        related_name='data_values',
    )
    record = models.ForeignKey(
        Record,
        on_delete=models.CASCADE,
        related_name='data_values',
    )
    event = models.ForeignKey(
        'project.Event',
        on_delete=models.CASCADE,
        related_name='data_values',
        blank=True,
        null=True,
    )
    field_name = models.CharField(max_length=100)
    instance = models.IntegerField(default=1)
    value_long = models.TextField(blank=True, null=True)
    updated_by = models.BigIntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'DataValue'
        verbose_name_plural = 'DataValues'
        db_table = 'proxmed_data_values'
        unique_together = (('project', 'record', 'event', 'field_name', 'instance'),)
        indexes = [
            models.Index(fields=['project', 'field_name'], name='idx_field'),
            models.Index(fields=['project', 'record', 'event'], name='idx_record'),
        ]

    def __str__(self) -> str:
        return f"{self.record.record_key} - {self.field_name} [{self.instance}]"


class FormStatus(models.Model):
    class Status(models.TextChoices):
        INCOMPLETE = 'incomplete', 'Incomplete'
        UNVERIFIED = 'unverified', 'Unverified'
        COMPLETE = 'complete', 'Complete'

    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        related_name='form_statuses',
    )
    record = models.ForeignKey(
        Record,
        on_delete=models.CASCADE,
        related_name='form_statuses',
    )
    event = models.ForeignKey(
        'project.Event',
        on_delete=models.CASCADE,
        related_name='form_statuses',
        blank=True,
        null=True,
    )
    form = models.ForeignKey(
        'projectform.Form',
        on_delete=models.CASCADE,
        related_name='statuses',
    )
    instance = models.IntegerField(default=1)
    status = models.CharField(
        max_length=12,
        choices=Status.choices,
        default=Status.INCOMPLETE,
    )
    updated_by = models.BigIntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'FormStatus'
        verbose_name_plural = 'FormStatuses'
        db_table = 'proxmed_form_status'
        unique_together = (('project', 'record', 'event', 'form', 'instance'),)

    def __str__(self) -> str:
        return f"{self.record.record_key} - {self.form.form_label} [{self.instance}]: {self.status}"


class AuditLog(models.Model):
    log_id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        related_name='audit_logs',
        blank=True,
        null=True,
    )
    user = models.BigIntegerField(blank=True, null=True)
    record = models.ForeignKey(
        Record,
        on_delete=models.CASCADE,
        related_name='audit_logs',
        blank=True,
        null=True,
    )
    event = models.ForeignKey(
        'project.Event',
        on_delete=models.CASCADE,
        related_name='audit_logs',
        blank=True,
        null=True,
    )
    action = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    old_value = models.TextField(blank=True, null=True)
    new_value = models.TextField(blank=True, null=True)
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'AuditLog'
        verbose_name_plural = 'AuditLogs'
        db_table = 'proxmed_audit_logs'
        indexes = [
            models.Index(fields=['project', 'created_at'], name='idx_project_time'),
        ]

    def __str__(self) -> str:
        return f"{self.action} - {self.created_at}"


