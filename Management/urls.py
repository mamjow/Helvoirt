from django.urls import path
from django.conf.urls import url
# from django.views.generic import TemplateView
from accounts import views
from .views import add_post
from .views import post_list
from Management.views import Panel

urlpatterns = [
    url('posts/addpost/', add_post, name='add_details'),
    url('posts/$', post_list, name='post_list'),
    url('dashboard/$', Panel.as_view(template_name='manager/modiriat.html')),

]
