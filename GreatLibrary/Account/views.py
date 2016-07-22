from django.shortcuts import render
from django import forms
from django.db import models
from django.contrib.auth.decorators import login_required
from .models import UserInfo
import re

GENDER_CHOICE = (
	('male', 'male'),
	('female', 'female'),
	)

class AccountForm(forms.Form):
	name = forms.CharField(max_length=20)
	password = forms.CharField(max_length=30, widget=forms.PasswordInput)
	email = forms.EmailField()

class LoginForm(forms.Form):
	name = forms.CharField(max_length=20)
	password = forms.CharField(max_length=30, widget=forms.PasswordInput)

class DataForm(forms.Form):
	name = forms.CharField(max_length=20)
	password = forms.CharField(max_length=30)
	gender = forms.ChoiceField(choices = GENDER_CHOICE)
	phone = forms.CharField(max_length=20)
	email = forms.EmailField()
	info = forms.CharField(max_length=255, widget=forms.Textarea)

# Create your views here.
def login(request):
	if 'username' in request.session and 'status' in request.session:
		if request.session['status'] == True:
			return render(request, 'home.html', {'logined': True})
	if request.method == "POST":
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			data = login_form.clean()
			name = data.get("name")
			password = data.get("password")
			if UserInfo.objects.filter(name__exact=name, password__exact=password):
				request.session['username'] = name
				request.session['status'] = True
				return render(request, 'home.html', {'logined': 1, 'notice': name})
			else:
				notice = "invalid name or password"
				return render(request, 'login.html', {'login_form': LoginForm(), 'notice': notice})
	return render(request, 'login.html', {'login_form': LoginForm()})

def logout(request):
	if 'username' in request.session:
		request.session['username'] = ""
	if 'status' in request.session:
		request.session['status'] = False
	return render(request, 'logout.html')

def register(request):
	if 'status' in request.session:
		if request.session["status"] == True:
			notice = "you have already logged in"
			return render(request, 'register.html', {'account_form': AccountForm(), 'notice': notice})
	if request.method == "POST":
		account_form = AccountForm(request.POST)
		if account_form.is_valid():
			data = account_form.clean()
			name = data.get("name")
			password = data.get("password")
			email = data.get("email")
			if UserInfo.objects.filter(name=name):   # if user already exist
				notice = "account already exists, please login"
				return render(request, 'register.html', {'account_form': prev_account, 'notice':notice})
			user = UserInfo(name=name, password=password, email=email)
			user.save()
			request.session['status'] = True
			request.session['username'] = name
			return render(request, 'home.html', {'logined': 1, 'notice': name})
	else:
		account_form = AccountForm()
		return render(request, 'register.html', {'account_form': account_form,})

def editdata(request):
	if 'status' in request.session:
		if request.session['status'] == False:
			return render(request, 'login.html', {'notice': 'no user logged in, please log in first', 'login_form': LoginForm()})
	else:
		return render(request, 'login.html', {'notice': 'no user logged in, please log in first', 'login_form': LoginForm()})

	this_user = UserInfo.objects.get(name=request.session['username'])
	if request.method == 'POST':
		dataform = DataForm(request.POST)
		if dataform.is_valid():
			data = dataform.clean()
			name = data.get('name')
			password = data.get('password')
			gender = data.get('gender')
			phone = data.get('phone')
			email = data.get('email')
			info = data.get('info')
			if checkData(request, name, password, phone, email) == True:
				 if 'editdata_notice' in request.session:
				 	del request.session['editdata_notice']
				 this_user.set_name(name)
				 request.session['username'] = name
				 this_user.set_password(password)
				 this_user.set_gender(gender)
				 this_user.set_phone(phone)
				 this_user.set_email(email)
				 this_user.set_info(info)
				 this_user.save()
	return render(request, 'editdata.html', {'dataform': DataForm(initial={
			'name': this_user.name,
			'password': this_user.password,
			'gender': this_user.gender,
			'phone': this_user.phone,
			'email': this_user.email,
			'info': this_user.info
		})})

def checkData(request, name=None, password=None, phone=None, email=None):
	if not name or len(name)==0:
		request.session['editdata_notice'] = "invalid username"
		return False
	if not password or len(password) < 6:
		request.session['editdata_notice'] = "password too short"
		return False
	if len(phone) < 7 or re.match(r'd+$', phone) == False:
		request.session['editdata_notice'] = "invalid phonenumber"
		return False
	if not email:
		request.session['editdata_notice'] = "invalid email address"
		return False
	this_user = UserInfo.objects.get(name=request.session['username'])
	if name != this_user.get_name():
		try:
			UserInfo.objects.get(name=name)
			request.session['editdata_notice'] = "username repeated"
			return False
		except UserInfo.DoesNotExist:
			return True
	return True