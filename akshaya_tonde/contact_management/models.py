from django.db import models
import datetime
# Create your models here.

class ContactsInfo(models.Model):
    
    name = models.CharField(max_length=70)
    email = models.EmailField
    notes = models.CharField(max_length=100)
    creation_date = models.DateTimeField
    