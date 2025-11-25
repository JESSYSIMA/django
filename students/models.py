from django.db import models
from university.models import University

class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
