from django.db import models


class Person(models.Model):
    """
    this model used for stored the user information in the database
    """
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField(default=0)
