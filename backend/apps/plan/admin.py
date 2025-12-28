from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Plan,Feature,Permission 

# Register your models here.

 

admin.site.register(Plan ) 
admin.site.register(Feature ) 
admin.site.register(Permission ) 