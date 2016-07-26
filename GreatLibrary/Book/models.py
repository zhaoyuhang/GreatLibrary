from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
	name 			= models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Review(models.Model):
	content 		= models.CharField(max_length=3000)
	starNum 		= models.IntegerField(default=0)
	writer 			= models.ForeignKey('Account.UserInfo', default=None)
	related_book	= models.ForeignKey('Book', default=None)
	def __str__(self):
		return self.content

class Book(models.Model):
	name 			= models.CharField(max_length=100)
	author 			= models.CharField(max_length=100, default="")
	cover 			= models.CharField(max_length=300, default="")
	ISBN 			= models.CharField(max_length=100, default="")
	press 			= models.CharField(max_length=100, default="")
	pressTime 		= models.CharField(max_length=40, default="")
	grade 			= models.FloatField(default=10.0)
	gradeNum 		= models.IntegerField(default=0)
	intro 			= models.CharField(max_length=3000, default="")
	labelList 		= models.ManyToManyField('Tag', default=[])
	reviewList  	= models.ManyToManyField('Account.UserInfo', default=[], through='Review')
	def __str__(self):
		return self.name