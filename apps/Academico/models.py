from django.db import models

# Create your models here.
class Course(models.Model):
    code = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=50)
    credits = models.PositiveSmallIntegerField()