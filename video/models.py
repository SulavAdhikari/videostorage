from django.db import models
from datetime import date
# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos')
    cost = models.IntegerField()
    size = models.BigIntegerField()
    uploaded_date = models.DateField(default=date.today())
