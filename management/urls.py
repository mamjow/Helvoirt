from django.urls import path
from django.conf.urls import url
# from django.views.generic import TemplateView
from accounts import views
from .views import add_post
from .views import update_post
from .views import delete_post
from .views import post_list
from management.views import Panel

urlpatterns = [
    url('posts/addpost/', add_post, name='post_new'),
    url('posts/$', post_list, name='post_list'),
    url(r'^posts/(?P<pk>\d+)/update/$', update_post, name='post_update'),
    url(r'^books/(?P<pk>\d+)/delete/$', delete_post, name='post_delete'),
    url('dashboard/$', Panel.as_view(template_name='manager/modiriat.html')),

]
