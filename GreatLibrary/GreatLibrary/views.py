from django.shortcuts import render
from Book.models import Book

def home(request):
	books = Book.objects.all()
	if 'editdata_notice' in request.session:
		del request.session['editdata_notice']

	return render(request, 'home.html', {'books': books})