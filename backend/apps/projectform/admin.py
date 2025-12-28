from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Form,FormField,FieldChoice ,ProjectEventForm 

# Register your models here.

 

admin.site.register(Form ) 
admin.site.register(FormField ) 
admin.site.register(FieldChoice ) 
admin.site.register(ProjectEventForm ) 