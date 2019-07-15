from django.db import models

class Show(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    releaseDate = models.DateTimeField()
    description = models.CharField(max_length = 255)
