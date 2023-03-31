from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Student)
admin.site.register(Staff)

#ORM.
# Student.objects.get(id = 1)
# Student.objects.all()
# Student.objects.create(name = "nobel", age = 23, department = "BCA") For creating object
# https://amitness.com/2018/10/django-orm-for-sql-users/
