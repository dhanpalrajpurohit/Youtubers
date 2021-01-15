from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

class Hiretuber(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    tuber_id = models.IntegerField()
    tuber_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    message = models.TextField(blank=True,max_length=255)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.email