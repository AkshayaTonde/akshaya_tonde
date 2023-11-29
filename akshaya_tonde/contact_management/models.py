from django.db import models
import datetime
import django.utils.timezone
# Create your models here.

class ContactsInfo(models.Model):
    
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    notes = models.CharField(max_length=100)
    creation_date = models.DateTimeField(default=django.utils.timezone.now)


