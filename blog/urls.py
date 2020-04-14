from django.conf.urls import url
from . import views
from django.urls import path, re_path

app_name = 'blog'
urlpatterns = [
	path('', views.post_list, name='post_list'),
	re_path(r'^post_list/$', views.post_list, name='post_list'),
]