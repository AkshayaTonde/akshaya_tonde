from django.db import models

# Create your models here.
class contact_Details(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=70)
    email = models.EmailField
    notes = models.CharField(max_length=100)
    creation_date = models.DateTimeField