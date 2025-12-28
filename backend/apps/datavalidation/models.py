from django.db import models


class SDVRule(models.Model):
    project = models.OneToOneField(
        'project.Project',
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='sdv_rule',
    )
    require_sdv_before_lock = models.BooleanField(default=False)
    require_sdv_for_all_fields = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'SDV Rule'
        verbose_name_plural = 'SDV Rules'
        db_table = 'proxmed_sdv_rules'

    def __str__(self) -> str:
        return f"SDV Rules for {self.project.title}"


class SDVFieldStatus(models.Model):
    class SDVStatus(models.TextChoices):
        NOT_REQUIRED = 'not_required', 'Not Required'
        PENDING = 'pending', 'Pending'
        VERIFIED = 'verified', 'Verified'
        NOT_VERIFIED = 'not_verified', 'Not Verified'

    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        related_name='sdv_field_statuses',
    )
    record = models.ForeignKey(
        'record.Record',
        on_delete=models.CASCADE,
        related_name='sdv_field_statuses',
    )
    event = models.ForeignKey(
        'project.Event',
        on_delete=models.CASCADE,
        related_name='sdv_field_statuses',
        blank=True,
        null=True,
    )
    field_name = models.CharField(max_length=100)
    instance = models.IntegerField(default=1)
    sdv_status = models.CharField(
        max_length=15,
        choices=SDVStatus.choices,
        default=SDVStatus.PENDING,
    )
    verified_by = models.BigIntegerField(blank=True, null=True)
    verified_at = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'SDV Field Status'
        verbose_name_plural = 'SDV Field Statuses'
        db_table = 'proxmed_sdv_field_status'
        unique_together = (('project', 'record', 'event', 'field_name', 'instance'),)
        indexes = [
            models.Index(fields=['project', 'sdv_status'], name='idx_sdv'),
        ]

    def __str__(self) -> str:
        return f"{self.record.record_key} - {self.field_name} [{self.instance}]: {self.sdv_status}"


class ValidationRule(models.Model):
    class Severity(models.TextChoices):
        INFO = 'info', 'Info'
        WARNING = 'warning', 'Warning'
        ERROR = 'error', 'Error'

    class Scope(models.TextChoices):
        FIELD = 'field', 'Field'
        FORM = 'form', 'Form'
        EVENT = 'event', 'Event'
        RECORD = 'record', 'Record'

    rule_id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        related_name='validation_rules',
    )
    name = models.CharField(max_length=255)
    severity = models.CharField(
        max_length=10,
        choices=Severity.choices,
        default=Severity.WARNING,
    )
    scope = models.CharField(max_length=10, choices=Scope.choices)
    target_field_name = models.CharField(max_length=100, blank=True, null=True)
    expression = models.TextField()
    message = models.TextField()
    is_active = models.BooleanField(default=True)
    create_query_on_fail = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Validation Rule'
        verbose_name_plural = 'Validation Rules'
        db_table = 'proxmed_validation_rules'
        indexes = [
            models.Index(fields=['project', 'is_active'], name='idx_rule_active'),
        ]

    def __str__(self) -> str:
        return f"{self.project.title} - {self.name} ({self.severity})"


class ValidationResult(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Active'
        RESOLVED = 'resolved', 'Resolved'
        IGNORED = 'ignored', 'Ignored'

    result_id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        related_name='validation_results',
    )
    rule = models.ForeignKey(
        ValidationRule,
        on_delete=models.CASCADE,
        related_name='results',
    )
    record = models.ForeignKey(
        'record.Record',
        on_delete=models.CASCADE,
        related_name='validation_results',
    )
    event = models.ForeignKey(
        'project.Event',
        on_delete=models.CASCADE,
        related_name='validation_results',
        blank=True,
        null=True,
    )
    instance = models.IntegerField(default=1)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.ACTIVE,
    )
    details_json = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)
    resolved_by = models.BigIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Validation Result'
        verbose_name_plural = 'Validation Results'
        db_table = 'proxmed_validation_results'
        indexes = [
            models.Index(fields=['project', 'status'], name='idx_val'),
        ]

    def __str__(self) -> str:
        return f"Validation #{self.result_id} - {self.rule.name} for {self.record.record_key} ({self.status})"
