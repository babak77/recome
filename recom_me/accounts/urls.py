from django.conf.urls import patterns, url
urlpatterns = patterns('',
    url(
        r'^$',
        'django.contrib.auth.views.login',
        name='login',
        kwargs={'template_name': 'login.html'}
    ),
    url(
        r'^login/$',
        'django.contrib.auth.views.login',
        name='login',
        kwargs={'template_name': 'login.html'}
    ),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        name='logout',
        kwargs={'next_page': 'login.html'}
    ),
)