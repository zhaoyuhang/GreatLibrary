from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Book, Review
from .forms import ReviewForm, ShowReviewForm
from Account.models import UserInfo

# Create your views here.
def bookDetail(request, book_isbn):
	this_book = Book.objects.get(ISBN=book_isbn)
	
	if request.method == 'POST':
		if 'give_star' in request.POST:
			print '-------------give star to a review-------------'
			showreviewform = ShowReviewForm(request.POST)
			if showreviewform.is_valid():
				print '-------------review was given a star------------'
				writer_name = showreviewform.clean().get('username')
				writer = UserInfo.objects.get(name=writer_name)
				related_review = Review.objects.get(writer=writer, related_book=this_book)
				related_review.starNum += 1
				related_review.save()

		if 'write_review' in request.POST:
			if 'status' in request.session and request.session['status'] == True:
				user = UserInfo.objects.get(name=request.session['username'])
				try:
					target = Review.objects.get(writer=user, related_book=this_book)
				except Review.DoesNotExist:
					target = None
				if target == None:		# user didn't write a review to this book
					print '--------write review to book--------------'
					return render(request, 'writereview.html', {'bookname': this_book.name, 'reviewform': ReviewForm()})
			else:						# if no user logged in 
				return HttpResponseRedirect('/account/login/')

		elif 'submit_review' in request.POST:
			if 'status' in request.session and request.session['status'] == True:
				print '--------submit your review----------------'
				reviewform =  ReviewForm(request.POST)
				if reviewform.is_valid():
					content = reviewform.clean().get('content')
					this_user = UserInfo.objects.get(name=request.session['username'])
					review = Review(content=content, starNum=0, writer=this_user, related_book=this_book)
					review.save()
			else:
				return HttpResponseRedirect('/account/login/')
		
		elif 'collect' in request.POST:
			if 'status' in request.session and request.session['status'] == True:
				print '----------add book into collection---------'
				user = UserInfo.objects.get(name=request.session['username'])
				if this_book not in user.collectionList.all():
					user.collectionList.add(this_book)

	reviews = Review.objects.filter(related_book=this_book)
	showreviewforms = [ {'form': ShowReviewForm(initial={'content': review.content, 'starnum': review.starNum, 'username': review.writer.name}), 'name': review.writer.name} for review in reviews ]
	return render(request, 'bookdetail.html', {'book': this_book, 'showreviewforms': showreviewforms})