from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UserInfo(models.Model):
	name = models.CharField(max_length=20)
	password = models.CharField(max_length=50)
	gender = models.CharField(max_length=10)
	phone = models.CharField(max_length=20)
	info = models.CharField(max_length=255)
	email = models.EmailField()
	score = models.FloatField()
	isAdmin = models.BooleanField(default=False)
	isBlocked = models.BooleanField(default=False)

	def __str__(self):
		return self.name