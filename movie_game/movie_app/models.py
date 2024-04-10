from django.db import models

class actor_name(models.Model):
    name = models.CharField(max_length=255)
    poster_one = models.CharField(max_length=255)
    poster_two = models.CharField(max_length=255)
    poster_three = models.CharField(max_length=255)
    poster_four = models.CharField(max_length=255)
