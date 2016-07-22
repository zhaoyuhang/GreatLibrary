from django.shortcuts import render
from django import forms
from django.db import models
from django.contrib.auth import login, logout
from .models import UserInfo

class AccountForm(forms.Form):
	name = forms.CharField(max_length=20)
	password = forms.CharField(max_length=30, widget=forms.PasswordInput)
	email = forms.EmailField()

class LoginForm(forms.Form):
	name = forms.CharField(max_length=20)
	password = forms.CharField(max_length=30, widget=forms.PasswordInput)

# Create your views here.
def login(request):
	if request.method == "POST":
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			data = login_form.clean()
			name = data.get("name")
			password = data.get("password")
			if UserInfo.objects.filter(name__exact=name, password__exact=password):
				return render(request, 'home.html', {'logined': True})
			else:
				notice = "invalid name or password"
				return render(request, 'login.html', {'login_form': LoginForm(), 'notice': notice})
	return render(request, 'login.html', {'login_form': LoginForm()})

def logout(request):
	return render(request, 'home.html')

def register(request):
	if request.method == "POST":
		account_form = AccountForm(request.POST)
		if account_form.is_valid():
			data = account_form.clean()
			name = data.get("name")
			password = data.get("password")
			email = data.get("email")
			if UserInfo.objects.filter(name=name):   # if user already exist
				notice = "account already exists, please login"
				prev_account = AccountForm()
				prev_account.name = name
				return render(request, 'register.html', {'account_form': prev_account, 'notice':notice})
			user = UserInfo(name=name, password=password, email=email)
			user.save()
			logined = True
			return render(request, 'home.html', {'logined': logined})
	else:
		account_form = AccountForm()
		return render(request, 'register.html', {'account_form': account_form,})