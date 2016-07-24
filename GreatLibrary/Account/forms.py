from django import forms

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
	info = forms.CharField(max_length=255, widget=forms.Textarea)