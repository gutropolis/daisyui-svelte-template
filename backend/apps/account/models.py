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
    company = models.CharField(max_length=250, blank=True)
    contact_number = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.USER)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [  'first_name', 'last_name', 'contact_number', 'role', 'company']

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
         
         
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(
        upload_to='users/%Y/%m/%d/',
        blank=True
    )
    
    # billing_address = models.ForeignKey(
    #     Address, related_name='account_billing_address', on_delete=models.CASCADE, blank=True, null=True)
    # shipping_address = models.ForeignKey(
    #     Address, related_name='account_shipping_address', on_delete=models.CASCADE, blank=True, null=True)
    
    
    def get_absolute_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.user_id})

    def get_profile_update_url(self):
        return reverse('accounts:profile-update', kwargs={'pk': self.user_id})

    def __str__(self):
        return f'Profile of {self.user.email}'
    
    
class Business(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    business_type = models.CharField(
        "Business Type",
        max_length=255,
        choices=INDUSTRY_CHOICES,
        blank=True,
        null=True
    )
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100) 
    billing_address_line = models.CharField("Address", max_length=255, blank=True, null=True
    )
    billing_street = models.CharField("Street", max_length=55, blank=True, null=True)
    billing_city = models.CharField("City", max_length=255, blank=True, null=True)
    billing_state = models.CharField("State", max_length=255, blank=True, null=True)
    billing_postcode = models.CharField("Post/Zip-code", max_length=64, blank=True, null=True
    )
    billing_country = models.CharField(
        max_length=3,
        choices=COUNTRY_CHOICES,
        blank=True,
        null=True
    )
    website = models.URLField("Website", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Business" 
        db_table = "proxmed_business" 
        
    def __str__(self):
        return self.user.email

class BusinessTeamMember(models.Model):
    business = models.ForeignKey(Business, on_delete=models.PROTECT)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "BusinessTeamMember"
        verbose_name_plural = "BusinessTeamMembers"
        db_table = "proxmed_business_team_members" 

    def __str__(self):
        return f"{self.business.name} :: {self.user.email}"