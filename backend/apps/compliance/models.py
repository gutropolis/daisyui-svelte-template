from django.db import models


class FieldReviewStatus(models.Model):
    class ReviewStatus(models.TextChoices):
        UNREVIEWED = 'unreviewed', 'Unreviewed'
        REVIEWED = 'reviewed', 'Reviewed'
        NEEDS_REVIEW = 'needs_review', 'Needs Review'

    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        related_name='field_reviews',
    )
    record = models.ForeignKey(
        'record.Record',
        on_delete=models.CASCADE,
        related_name='field_reviews',
    )
    event = models.ForeignKey(
        'project.Event',
        on_delete=models.CASCADE,
        related_name='field_reviews',
        blank=True,
        null=True,
    )
    field_name = models.CharField(max_length=100)
    instance = models.IntegerField(default=1)
    review_status = models.CharField(
        max_length=15,
        choices=ReviewStatus.choices,
        default=ReviewStatus.UNREVIEWED,
    )
    reviewed_by = models.BigIntegerField(blank=True, null=True)
    reviewed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'FieldReviewStatus'
        verbose_name_plural = 'FieldReviewStatuses'
        db_table = 'proxmed_field_review_status'
        unique_together = (('project', 'record', 'event', 'field_name', 'instance'),)
        indexes = [
            models.Index(fields=['project', 'review_status'], name='idx_review'),
        ]

    def __str__(self) -> str:
        return f"{self.record.record_key} - {self.field_name} [{self.instance}]: {self.review_status}"


class DataQuery(models.Model):
    class QueryStatus(models.TextChoices):
        OPEN = 'open', 'Open'
        ANSWERED = 'answered', 'Answered'
        RESOLVED = 'resolved', 'Resolved'
        CLOSED = 'closed', 'Closed'

    class Priority(models.TextChoices):
        LOW = 'low', 'Low'
        MEDIUM = 'medium', 'Medium'
        HIGH = 'high', 'High'

    query_id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        related_name='data_queries',
    )
    record = models.ForeignKey(
        'record.Record',
        on_delete=models.CASCADE,
        related_name='data_queries',
    )
    event = models.ForeignKey(
        'project.Event',
        on_delete=models.CASCADE,
        related_name='data_queries',
        blank=True,
        null=True,
    )
    field_name = models.CharField(max_length=100)
    instance = models.IntegerField(default=1)
    status = models.CharField(
        max_length=10,
        choices=QueryStatus.choices,
        default=QueryStatus.OPEN,
    )
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM,
    )
    raised_by = models.BigIntegerField()
    assigned_to = models.BigIntegerField(blank=True, null=True)
    raised_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'DataQuery'
        verbose_name_plural = 'DataQueries'
        db_table = 'proxmed_data_queries'
        indexes = [
            models.Index(fields=['project', 'status'], name='idx_query_status'),
        ]

    def __str__(self) -> str:
        return f"Query #{self.query_id} - {self.record.record_key} - {self.field_name} ({self.status})"


class DataQueryMessage(models.Model):
    message_id = models.BigAutoField(primary_key=True)
    query = models.ForeignKey(
        DataQuery,
        on_delete=models.CASCADE,
        related_name='messages',
    )
    user = models.BigIntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'DataQueryMessage'
        verbose_name_plural = 'DataQueryMessages'
        db_table = 'proxmed_data_query_messages'
        ordering = ['created_at']

    def __str__(self) -> str:
        return f"Message #{self.message_id} for Query #{self.query.query_id} at {self.created_at}"


class QueryRule(models.Model):
    rule_id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        related_name='query_rules',
    )
    block_form_completion = models.BooleanField(default=False)
    auto_close_on_change = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'QueryRule'
        verbose_name_plural = 'QueryRules'
        db_table = 'proxmed_query_rules'

    def __str__(self) -> str:
        return f"Query Rules for {self.project.title}"


class FormLock(models.Model):
    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        related_name='form_locks',
    )
    record = models.ForeignKey(
        'record.Record',
        on_delete=models.CASCADE,
        related_name='form_locks',
    )
    event = models.ForeignKey(
        'project.Event',
        on_delete=models.CASCADE,
        related_name='form_locks',
        blank=True,
        null=True,
    )
    form = models.ForeignKey(
        'projectform.Form',
        on_delete=models.CASCADE,
        related_name='locks',
    )
    instance = models.IntegerField(default=1)
    locked_by = models.BigIntegerField()
    locked_at = models.DateTimeField()
    reason = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'FormLock'
        verbose_name_plural = 'FormLocks'
        db_table = 'proxmed_form_locks'
        unique_together = (('project', 'record', 'event', 'form', 'instance'),)

    def __str__(self) -> str:
        return f"{self.record.record_key} - {self.form.form_label} [{self.instance}] locked at {self.locked_at}"


class SignatureMeaning(models.Model):
    meaning_id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        related_name='signature_meanings',
    )
    code = models.CharField(max_length=50)
    label = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'SignatureMeaning'
        verbose_name_plural = 'SignatureMeanings'
        db_table = 'proxmed_signature_meanings'
        unique_together = (('project', 'code'),)

    def __str__(self) -> str:
        return f"{self.project.title} - {self.code}: {self.label}"


class Signature(models.Model):
    class EntityType(models.TextChoices):
        RECORD = 'record', 'Record'
        FORM = 'form', 'Form'
        EVENT = 'event', 'Event'
        QUERY = 'query', 'Query'
        EXPORT = 'export', 'Export'

    class AuthMethod(models.TextChoices):
        PASSWORD = 'password', 'Password'
        OTP = 'otp', 'OTP'
        SSO = 'sso', 'SSO'

    signature_id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        related_name='signatures',
    )
    user = models.BigIntegerField()
    meaning = models.ForeignKey(
        SignatureMeaning,
        on_delete=models.CASCADE,
        related_name='signatures',
    )
    entity_type = models.CharField(max_length=10, choices=EntityType.choices)
    record = models.ForeignKey(
        'record.Record',
        on_delete=models.CASCADE,
        related_name='signatures',
        blank=True,
        null=True,
    )
    event = models.ForeignKey(
        'project.Event',
        on_delete=models.CASCADE,
        related_name='signatures',
        blank=True,
        null=True,
    )
    form = models.ForeignKey(
        'projectform.Form',
        on_delete=models.CASCADE,
        related_name='signatures',
        blank=True,
        null=True,
    )
    instance = models.IntegerField(default=1)
    query = models.ForeignKey(
        DataQuery,
        on_delete=models.CASCADE,
        related_name='signatures',
        blank=True,
        null=True,
    )
    signed_hash = models.CharField(max_length=64)
    signed_at = models.DateTimeField(auto_now_add=True)
    signer_ip = models.CharField(max_length=50, blank=True, null=True)
    signer_agent = models.CharField(max_length=255, blank=True, null=True)
    auth_method = models.CharField(
        max_length=10,
        choices=AuthMethod.choices,
        default=AuthMethod.PASSWORD,
    )
    auth_proof_hash = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        verbose_name = 'Signature'
        verbose_name_plural = 'Signatures'
        db_table = 'proxmed_signatures'
        indexes = [
            models.Index(
                fields=['project', 'entity_type', 'record', 'event', 'form', 'instance'],
                name='idx_sig_lookup'
            ),
        ]

    def __str__(self) -> str:
        return f"Signature #{self.signature_id} - {self.meaning.code} by User {self.user} at {self.signed_at}"
