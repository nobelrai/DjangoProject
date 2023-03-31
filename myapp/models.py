from django.db import models


class Student(models.Model):  # Table name
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    department = models.CharField(max_length=50)

    def __str__(self):
        return f"hello I' am {self.name}"


class Staff(models.Model):
    name = models.CharField(max_length=20)
    post = models.CharField(max_length=20)
    salary = models.IntegerField()

