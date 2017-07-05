from django.conf.urls import url

from . import views
app_name = 'board'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_pk>[0-9]+)/$', views.postcomment, name='postcomment'),
]
