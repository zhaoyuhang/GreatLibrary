from django.shortcuts import render
from Book.models import Book, Tag
from Account.models import UserInfo


def home(request):
	if 'editdata_notice' in request.session:
		del request.session['editdata_notice']
	if request.method == 'POST':
		data = request.POST['search']
		search_by_bookname = []
		search_by_username = []
		search_by_isbn = []			# only data is pure numbers
		search_by_tag = []			# if data in Tag list

		books = Book.objects.all()
		for book in books:
			if data in book.name or book.name in data:
				search_by_bookname.append(book)

		users = UserInfo.objects.all()
		for user in users:
			if data in user.name or user.name in data:
				search_by_username.append(user)

		if data.isdigit() == True:
			for book in books:
				if data in book.name:
					search_by_isbn.append(book)
		else:
			try:
				this_tag = Tag.objects.get(name='data')
				for book in books:
					if this_tag in book.labelList:
						search_by_tag.append(book)
			except Tag.DoesNotExist:
				this_tag = None

		return render(request, 'search.html', {'by_bookname': search_by_bookname, 'by_username': search_by_username, 'by_isbn': search_by_isbn, 'by_tag': search_by_tag})
	else:
		books = Book.objects.all()
		return render(request, 'home.html', {'books': books})