from django.db import models

class UserAccount(models.Model):
    email = models.CharField(max_length=75, unique=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    password = models.CharField(max_length=1000)
