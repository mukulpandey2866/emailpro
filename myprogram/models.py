from django.db import models


class Email(models.Model):
    email=models.CharField(max_length=50,default='')


# Create your models here.
