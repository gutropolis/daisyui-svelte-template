from django.db import models
from config.mixins import TimestampMixin, AuditMixin


class Form(TimestampMixin, AuditMixin):
    form_id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        related_name='forms',
    )
    form_name = models.CharField(max_length=255)
    form_label = models.CharField(max_length=255)
    form_order = models.IntegerField()

    class Meta:
        verbose_name = 'ProjectForm'
        verbose_name_plural = 'ProjectForms'
        db_table = 'proxmed_project_forms'
        ordering = ['form_order']
        indexes = [
            models.Index(fields=['form_order']),
        ]

    def __str__(self) -> str:
        return f"{self.project.title} - {self.form_label}"


class FormField(models.Model):
    class FieldType(models.TextChoices):
        TEXT = 'text', 'Text'
        NOTES = 'notes', 'Notes'
        CALC = 'calc', 'Calculated'
        RADIO = 'radio', 'Radio'
        CHECKBOX = 'checkbox', 'Checkbox'
        DROPDOWN = 'dropdown', 'Dropdown'
        YESNO = 'yesno', 'Yes / No'
        TRUEFALSE = 'truefalse', 'True / False'
        DATE = 'date', 'Date'
        DATETIME = 'datetime', 'Date & Time'
        FILE = 'file', 'File Upload'
        SLIDER = 'slider', 'Slider'

    field_id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )
    form = models.ForeignKey(
        Form,
        on_delete=models.CASCADE,
        related_name='fields',
    )
    field_name = models.CharField(max_length=100)
    field_label = models.TextField()
    field_type = models.CharField(max_length=16, choices=FieldType.choices)
    validation_type = models.CharField(max_length=50, blank=True, null=True)
    min_value = models.CharField(max_length=50, blank=True, null=True)
    max_value = models.CharField(max_length=50, blank=True, null=True)
    is_required = models.BooleanField(default=False)
    branching_logic = models.TextField(blank=True, null=True)
    calc_equation = models.TextField(blank=True, null=True)
    field_order = models.IntegerField()
    section_header = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'ProjectFormField'
        verbose_name_plural = 'ProjectFormFields'
        db_table = 'project_form_fields'
        ordering = ['field_order']
        unique_together = (('project', 'field_name'),)
        indexes = [
            models.Index(fields=['field_order']),
        ]

    def __str__(self) -> str:
        return f"{self.project.title} - {self.form.form_label} - {self.field_name}"


class FieldChoice(models.Model):
    choice_id = models.BigAutoField(primary_key=True)
    field = models.ForeignKey(
        FormField,
        on_delete=models.CASCADE,
        related_name='choices',
    )
    coded_value = models.CharField(max_length=50)
    label = models.TextField()
    choice_order = models.IntegerField()

    class Meta:
        verbose_name = 'FieldChoice'
        verbose_name_plural = 'FieldChoices'
        db_table = 'field_choices'
        ordering = ['choice_order']

    def __str__(self) -> str:
        return f"{self.field.form.project.title} - {self.field.field_name}: {self.label}"



class ProjectEventForm(models.Model):
    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        related_name='event_forms',
    )
    event = models.ForeignKey(
        'project.Event',
        on_delete=models.CASCADE,
        related_name='forms',
    )
    form = models.ForeignKey(
        Form,
        on_delete=models.CASCADE,
        related_name='event_assignments',
    )

    class Meta:
        verbose_name = 'ProjectEventForm'
        verbose_name_plural = 'ProjectForms'
        db_table = 'project_event_forms'
        unique_together = (('event', 'form'),)

    def __str__(self) -> str:
        return f"{self.project.title} - Event {self.event.event_num} / Form {self.form.form_label}"
    

