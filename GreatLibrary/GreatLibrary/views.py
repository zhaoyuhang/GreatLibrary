from django.shortcuts import render
from Book.models import Book

def home(request):
	if 'editdata_notice' in request.session:
		del request.session['editdata_notice']

	if request.method == 'POST':
		data = request.POST.get('search')
		print data
		print request.POST
		return render(request, 'search.html')
	else:
		books = Book.objects.all()
		return render(request, 'home.html', {'books': books})