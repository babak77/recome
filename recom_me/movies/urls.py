from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='movies'),
    url(r'^addperson/$', views.addPerson, name='addperson'),
    url(r'^addmovie/$', views.addMovie, name='addmovie'),
   
]