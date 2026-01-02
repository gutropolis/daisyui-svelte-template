from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.urls import reverse
from django.utils import timezone

from apps.subscription.models import Subscription


INDUSTRY_CHOICES = (
    ('CRO', 'Contract Research Organization'),
    ('SPONSOR', 'Sponsor'),
    ('SITE', 'Clinical Site'),
)


COUNTRY_CHOICES = (
    ('USA', 'United States'),
    ('GBR', 'United Kingdom'),
    ('CAN', 'Canada'),
    ('IND', 'India'),
)


class UserManager(BaseUserManager):
    """Custom manager that uses email as the unique identifier."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        username = extra_fields.get('username')
        if not username:
            username = email.split('@')[0]
            extra_fields['username'] = username
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if not password:
            raise ValueError('Users must have a password')
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('role', self.model.Roles.USER)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', self.model.Roles.ADMIN)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        USER = 'USER', 'User'

    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    company = models.CharField(max_length=250, blank=True, null=True)
    contact_number = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.USER)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_email(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def recent_subscription(self):
        current_date = timezone.now().date()
        return Subscription.objects.filter(
            user=self,
            status=Subscription.Status.ACTIVE,
            paid_status=True,
            end_date__gte=current_date
        ).order_by('-start_date').first()

    @property
    def is_User(self):
        return self.role == self.Roles.USER

    @property
    def is_admin(self):
        return self.role == self.Roles.ADMIN

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    @property
    def get_business(self):
        try:
            return self.business
        except ObjectDoesNotExist:
            return None
         
         
