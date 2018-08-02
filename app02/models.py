from django.db import models


class Plane(models.Model):
    name = models.CharField(max_length=32)

