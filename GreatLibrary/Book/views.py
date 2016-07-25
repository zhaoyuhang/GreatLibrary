from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Book

# Create your views here.
def bookDetail(request, bookname):
	try:
		this_book = Book.objects.get(name=bookname)
		print '---------detail will be shown----------'
	except Book.DoesNotExist:
		this_book = None
	return render(request, 'bookDetail.html')