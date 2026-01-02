from django.db import models
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

# Create your models here.
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