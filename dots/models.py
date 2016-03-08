from django.db import models


# Create your models here.
class Dot(models.Model):
    """
        Dots model
    """
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
