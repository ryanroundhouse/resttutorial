from django.db import models

class Happiness(models.Model):
	rating = models.CharField(max_length=1)
	description = models.TextField()