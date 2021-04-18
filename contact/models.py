from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

class Contact(models.Model):
    owner=ForeignKey(to=User,on_delete=models.CASCADE)
    country_code=models.CharField(max_length=5)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=20)
    contact_picture=models.URLField(null=True)
    is_favourited=models.BooleanField(default=False)