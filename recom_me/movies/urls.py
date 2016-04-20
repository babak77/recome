from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='movies'),
    #url(r'^rating/$', views.index, name='rating'),
    url(r'^addperson/$', views.addPerson, name='addperson'),
    url(r'^addmovie/$', views.addMovie, name='addmovie'),
    url(r'^(?P<movie_id>[0-9]+)/(?P<slug>[^\.]+)/$', views.movie_detail, name='movie_detail'),

    url(r'^like/$', views.like, name='Movie_like'),
    
]