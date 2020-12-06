from django.db import models
from django.utils import timezone

class Comment(models.Model):
    comment= models.CharField(max_length=500)
    log_data=models.DateTimeField

    def __str__(self):
        date=timezone.localtime(self.log_data)
        return f"'{self.comment}'submitted on {date.strftime('%A,%d %B,%Y at %X')}"

