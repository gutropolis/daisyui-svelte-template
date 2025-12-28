from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Profile,Business,BusinessTeamMember

# Register your models here.

 

admin.site.register(User ) 
admin.site.register(Profile ) 
admin.site.register(Business )
admin.site.register(BusinessTeamMember )