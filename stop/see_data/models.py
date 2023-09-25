from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=False)
    phone_number = PhoneNumberField(blank=False)