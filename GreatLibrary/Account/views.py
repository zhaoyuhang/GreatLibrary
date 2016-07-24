from django.shortcuts import render
from django.db import models
from django.http import HttpResponseRedirect
from .models import UserInfo
from .forms import AccountForm, LoginForm, DataForm

def login(request):
	if 'editdata_notice' in request.session:
		del request.session['editdata_notice']
	if 'status' in request.session:
		if request.session['status'] == True:
			return HttpResponseRedirect('/home/')
			
	if request.method == "POST":
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			data = login_form.clean()
			name = data.get("name")
			password = data.get("password")
			if UserInfo.objects.filter(name__exact=name, password__exact=password):
				request.session['username'] = name
				request.session['status'] = True
				return HttpResponseRedirect('/home/')
			else:
				notice = "invalid name or password"
				return render(request, 'login.html', {'login_form': LoginForm(), 'notice': notice})
	return render(request, 'login.html', {'login_form': LoginForm()})

def logout(request):
	if 'username' in request.session:
		request.session['username'] = ""
	if 'status' in request.session:
		request.session['status'] = False
	if 'editdata_notice' in request.session:
		del request.session['editdata_notice']
	return render(request, 'logout.html')

def register(request):
	if 'editdata_notice' in request.session:
		del request.session['editdata_notice']
	if 'status' in request.session:
		if request.session["status"] == True:
			notice = "you have already logged in"
			return render(request, 'register.html', {'account_form': AccountForm(), 'notice': notice})
	if request.method == "POST":
		account_form = AccountForm(request.POST)
		if account_form.is_valid():
			print '-------------getting data from form--------------'
			data = account_form.clean()
			name = data.get("name")
			password = data.get("password")
			email = data.get("email")
			if UserInfo.objects.filter(name=name):   # if user already exist
				notice = "account already exists, please login"
				print '-------------account already exists--------------'
				return render(request, 'register.html', {'account_form': AccountForm(initial={
						'name': name,
						'password': password,
						'email': email,
					}), 'notice':notice})
			print '-------------valid data, user registered--------------'
			user = UserInfo(name=name, password=password, email=email)
			user.save()
			request.session['status'] = True
			request.session['username'] = name
			return HttpResponseRedirect('/home/')
	return render(request, 'register.html', {'account_form': AccountForm()})


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
			print '-------------getting data from form--------------'
			data = dataform.clean()
			name = data.get('name')
			password = data.get('password')
			gender = data.get('gender')
			phone = data.get('phone')
			email = data.get('email')
			info = data.get('info')
			this_name = this_user.name
			if checkData(request, name, password, phone, email, this_name):
				if 'editdata_notice' in request.session:
					del request.session['editdata_notice']
				this_user.name = name
				this_user.password = password
				this_user.gender = gender
				this_user.phone = phone
				this_user.email = email
				this_user.info = info
				this_user.save()
				request.session['username'] = name
		else:
			request.session['editdata_notice'] = 'Make sure every entry is not empty!'
	return render(request, 'editdata.html', {'dataform': DataForm(initial={
			'name': this_user.name,
			'password': this_user.password,
			'gender': this_user.gender,
			'phone': this_user.phone,
			'email': this_user.email,
			'info': this_user.info
		})})

def checkData(request, name=None, password=None, phone=None, email=None, this_name=None):
	print '-------------checking data--------------'
	if not email:
		request.session['editdata_notice'] = "invalid email address!"
		print '-------------invalid email address--------------'
		return False
	if name != this_name:
		try:
			UserInfo.objects.get(name=name)
			request.session['editdata_notice'] = "username repeated!"
			print '-------------username repeated--------------'
			return False
		except UserInfo.DoesNotExist:
			return True
	print '-------------valid data--------------'
	return True
	