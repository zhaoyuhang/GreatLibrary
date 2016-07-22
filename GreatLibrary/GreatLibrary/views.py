from django.shortcuts import render

def home(request):
	if 'status' in request.session and 'username' in request.session:
		if request.session['status']:
			return render(request, 'home.html', {'logined': 1,})
	return render(request, 'home.html',)