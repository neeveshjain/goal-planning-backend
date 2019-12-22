from django.db import models

# Create your models here.
class Activity(models.Model):
    class Meta:
        verbose_name_plural = 'activities'
    
    activity_name = models.CharField(max_length=300)
