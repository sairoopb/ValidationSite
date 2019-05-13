from django.conf import settings
from django.db import models

class Credential(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.username