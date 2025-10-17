from django.contrib import admin
from . models import Student, User,Profile,Book,Course

# creates table format. If this is not done, it will be in object format 
class User_display(admin.ModelAdmin):
    list_display=['name','city']

class Book_title(admin.ModelAdmin):
    list_display=['author','title']

# class student_data(admin.ModelAdmin):
#     list_display=['name','courses']

# class course_data(admin.ModelAdmin):
#     list_display=['course','price']

# Register your models here.
admin.site.register(User,User_display)
admin.site.register(Profile)
admin.site.register(Book,Book_title)
admin.site.register(Student)
admin.site.register(Course)