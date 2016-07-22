from django.shortcuts import render

def home(request):
	logined = False
	return render(request, 'home.html',)