from django.db import models

# Create your models here.

class StudentModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    school = models.CharField(max_length=100)
    def __str__(self):
        return self.name
