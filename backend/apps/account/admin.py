from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.user.models import User
from .models import Profile,Business,BusinessTeamMember

# Register your models here.

 

admin.site.register(User ) 
admin.site.register(Profile ) 
admin.site.register(Business )
admin.site.register(BusinessTeamMember )