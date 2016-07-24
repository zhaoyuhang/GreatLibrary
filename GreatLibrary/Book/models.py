from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
	name 		= models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Review(models.Model):
	content 	= models.CharField(max_length=3000)
	starNum 	= models.IntegerField(default=0)
	writer 		= models.OneToOneField('Account.UserInfo', default=None)
	def __str__(self):
		return self.content

class Book(models.Model):
	name 		= models.CharField(max_length=100)
	author 		= models.CharField(max_length=100)
	cover 		= models.CharField(max_length=100)
	ISBN 		= models.CharField(max_length=100)
	press 		= models.CharField(max_length=100)
	pressTime 	= models.DateTimeField(default=timezone.now)
	grade 		= models.FloatField(default=5.0)
	gradeNum 	= models.IntegerField(default=0)
	intro 		= models.CharField(max_length=500)
	labelList 	= models.ManyToManyField('Tag')
	reviewList  = models.ManyToManyField('Review')
	def __str__(self):
		return self.name