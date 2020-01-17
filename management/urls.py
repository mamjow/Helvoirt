from django.urls import path
from django.conf.urls import url
# from django.views.generic import TemplateView
from accounts import views
from .views import add_post
from .views import update_post
from .views import delete_post
from .views import post_list
from .views import Panel

urlpatterns = [
    url(r'^dashboard/$', Panel.as_view(template_name='manager/panel.html'), name='dashboard'),
    url(r'^posts/$', post_list, name='post_list'),
    url(r'^posts/addpost/$', add_post, name='post_new'),
    url(r'^posts/(?P<pk>\d+)/update/$', update_post, name='post_update'),
    url(r'^posts/(?P<pk>\d+)/delete/$', delete_post, name='post_delete'),
]
