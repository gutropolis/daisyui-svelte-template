from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Project,ProjectSetting,Arm ,Event,ProjectUser

# Register your models here.

 

admin.site.register(Project ) 
admin.site.register(ProjectUser ) 
admin.site.register(Event ) 
admin.site.register(ProjectSetting ) 
admin.site.register(Arm ) 