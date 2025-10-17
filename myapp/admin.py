from django.contrib import admin
from . models import User,Profile

# creates table format. If this is not done, it will be in object format 
class User_display(admin.ModelAdmin):
    list_display=['name','city']

# Register your models here.
admin.site.register(User,User_display)
admin.site.register(Profile)