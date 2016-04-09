from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='books'),
    #url(r'^rating/$', views.index, name='rating'),
    url(r'^addperson/$', views.addPerson, name='addperson'),
    url(r'^addbook/$', views.addBook, name='addbook'),
    url(r'^(?P<book_id>[0-9]+)/(?P<slug>[^\.]+)/$', views.book_detail, name='book_detail'),

    url(r'^like/$', views.like, name='like'),
    
]