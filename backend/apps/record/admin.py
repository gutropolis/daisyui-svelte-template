from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Record,DataValue,FormStatus ,AuditLog 

# Register your models here.

 

admin.site.register(Record ) 
admin.site.register(DataValue ) 
admin.site.register(FormStatus ) 
admin.site.register(AuditLog ) 