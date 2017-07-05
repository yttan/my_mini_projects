from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.postcomment, name='postcomment'),
]
