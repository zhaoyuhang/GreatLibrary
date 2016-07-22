from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserInfo(models.Model):
	name 		= models.CharField(max_length=20)
	password 	= models.CharField(max_length=50)
	gender 		= models.CharField(max_length=10, default="male")
	phone 		= models.CharField(max_length=20, default="")
	info 		= models.CharField(max_length=255, default="")
	email 		= models.EmailField()
	score 		= models.FloatField(default=0)
	isAdmin 	= models.BooleanField(default=False)
	isBlocked 	= models.BooleanField(default=False)

	def __str__(self):
		return self.name
	def get_name(self):
		return self.name
	def set_name(self, name):
		self.name = name
		self.save()
	def set_password(self, password):
		self.password = password
		self.save()
	def set_gender(self, gender):
		self.gender = gender
		self.save()
	def set_phone(self, phone):
		self.phone = phone
		self.save()
	def set_email(self, email):
		self.email = email
		self.save()
	def set_info(self, info):
		self.info = info
		self.save()