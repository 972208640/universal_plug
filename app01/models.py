from django.db import models


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)


class Article(models.Model):
    title = models.CharField(max_length=32)

