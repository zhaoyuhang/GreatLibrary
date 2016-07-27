from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# create your models here.

class Message(models.Model):
	content 		= models.CharField(max_length=500)
	relatedUser 	= models.OneToOneField('UserInfo')
	sendTime 		= models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.content

class Note(models.Model):
	title 			= models.CharField(max_length=300)
	content 		= models.CharField(max_length=3000)
	def __str__(self):
		return self.title

class UserInfo(models.Model):
	name 			= models.CharField(max_length=20)
	password 		= models.CharField(max_length=50)
	gender 			= models.CharField(max_length=10, default="male")
	phone 			= models.IntegerField(default=0)
	info 			= models.CharField(max_length=255, default="your information")
	email 			= models.EmailField()
	prevImage 		= models.CharField(default='headImages/default.jpg', max_length=100)
	headImage 		= models.CharField(default='headImages/default.jpg', max_length=100)
	score 			= models.FloatField(default=0)
	isAdmin 		= models.BooleanField(default=False)
	isBlocked 		= models.BooleanField(default=True)
	followList  	= models.ManyToManyField('self')
	collectionList 	= models.ManyToManyField('Book.Book')
	noteList 		= models.ManyToManyField('Note')
	sendMessageList = models.ManyToManyField('Message', related_name="messages_you_send")
	reveiveMessageList = models.ManyToManyField('Message', related_name="messages_you_received")
	def __str__(self):
		return self.name

