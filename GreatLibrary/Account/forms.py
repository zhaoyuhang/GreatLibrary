from django import forms
from django.utils import timezone

GENDER_CHOICE = (
	('male', 'male'),
	('female', 'female'),
	)

class AccountForm(forms.Form):
	name = forms.CharField(min_length=4, max_length=20)
	password = forms.CharField(min_length=6, max_length=30, widget=forms.PasswordInput)
	email = forms.EmailField()

class LoginForm(forms.Form):
	name = forms.CharField(max_length=20)
	password = forms.CharField(max_length=30, widget=forms.PasswordInput)

class DataForm(forms.Form):
	name = forms.CharField(min_length=4, max_length=20)
	password = forms.CharField(min_length=6, max_length=30)
	gender = forms.ChoiceField(choices = GENDER_CHOICE)
	phone = forms.IntegerField()
	email = forms.EmailField()
	headImage = forms.ImageField()
	info = forms.CharField(max_length=255, widget=forms.Textarea)

class MessageForm(forms.Form):
	content = forms.CharField(min_length=20, max_length=500, widget=forms.Textarea)

class NoteForm(forms.Form):
	title = forms.CharField(max_length=50)
	content = forms.CharField(max_length=5000, widget=forms.Textarea)