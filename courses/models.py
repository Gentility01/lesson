from django.db import models

# Create your models here.
class Courses(models.Model):
    title   = models.CharField( max_length=150)
