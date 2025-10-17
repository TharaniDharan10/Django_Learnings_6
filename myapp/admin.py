from django.contrib import admin
from . models import User,Profile,Book

# creates table format. If this is not done, it will be in object format 
class User_display(admin.ModelAdmin):
    list_display=['name','city']

class Book_title(admin.ModelAdmin):
    list_display=['author','title']

# Register your models here.
admin.site.register(User,User_display)
admin.site.register(Profile)
admin.site.register(Book,Book_title)