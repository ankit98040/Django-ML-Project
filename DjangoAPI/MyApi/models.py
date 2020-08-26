from django.db import models

class MyFile(models.Model):
    image = models.ImageField()