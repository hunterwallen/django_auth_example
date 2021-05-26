from django.db import models

class UserAccount(models.Model):
    email = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=1000)
