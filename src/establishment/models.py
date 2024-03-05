from django.db import models


class Establishment(models.Model):
    """
    Represents an establishment
    opening_hours format - 'HH-HH'
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    locations = models.CharField(max_length=100)
    opening_hours = models.CharField(max_length=5)

    def __str__(self):
        return self.name
