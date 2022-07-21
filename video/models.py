from django.db import models
from datetime import date


class Video(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos')
    length = models.IntegerField()
    size = models.BigIntegerField()
    uploaded_date = models.DateField(default=date.today())

    def __str__(self):
        return self.title