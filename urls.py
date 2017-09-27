from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/blog/$', views.add_blog, name='add_blog'),
    url(r'^edit/blog/(?P<id>\d+)/$', views.edit_blog, name='edit_blog'),
    url(r'^blog/(?P<id>\d+)/$', views.blog, name='blog'),
]
