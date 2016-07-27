from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'detail/(?P<book_isbn>\d+)/', views.bookDetail, name='bookDetail'),
]