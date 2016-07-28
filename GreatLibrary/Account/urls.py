from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^login/', views.login, name="login"),
    url(r'^logout/', views.logout, name="logout"),
    url(r'^register/', views.register, name="register"),
    url(r'^editdata/(?P<username>(\w|\d| )+)/', views.editdata, name="editdata"),
    url(r'^data/(?P<username>(\w|\d| )+)/', views.showdata, name="showdata"),
    url(r'^note/(?P<username>(\w|\d| )+)/', views.note, name="note"),
    url(r'^review/(?P<username>(\w|\d| )+)/', views.review, name='review'),
    url(r'^collection/(?P<username>(\w|\d| )+)/', views.collection, name='colletion'),
]