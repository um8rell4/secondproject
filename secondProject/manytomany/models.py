from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=30)


class Students(models.Model):
    name = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course)
# Create your models here.
