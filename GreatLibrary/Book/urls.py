from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'detail/(?P<bookname>(\w|\d| )+)/', views.bookDetail, name='bookDetail'),
]