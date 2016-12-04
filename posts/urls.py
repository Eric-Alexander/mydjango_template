from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [

    url(r'^$', views.posts_readall),
    url(r'^create/$', views.posts_create),
    url(r'^read/$', views.posts_read),
    url(r'^update/$', views.posts_update),
    url(r'^delete$', views.posts_delete)

]
