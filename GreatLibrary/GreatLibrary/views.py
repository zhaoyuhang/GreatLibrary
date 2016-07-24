from django.shortcuts import render

def home(request):
	if 'editdata_notice' in request.session:
		del request.session['editdata_notice']
	if 'status' in request.session and 'username' in request.session:
		if request.session['status']:
			return render(request, 'home.html', {'logined': 1,})
	return render(request, 'home.html',)