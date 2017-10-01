from django.conf.urls import url

from . import views
app_name = 'board'
urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^(?P<post_user>[a-zA-Z0-9]+)/$', views.userpage, name='userpage'),
    url(r'^(?P<post_user>[a-zA-Z0-9]+)/add_todo/$', views.add_todo, name = 'add_todo'),
    url(r'^(?P<post_user>[a-zA-Z0-9]+)/delete_comment/$', views.delete_comment, name = 'delete_comment'),
    url(r'^(?P<post_user>[a-zA-Z0-9]+)/delete_todo/$', views.delete_todo, name = 'delete_todo'),
]
