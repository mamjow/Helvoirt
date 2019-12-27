from django.conf.urls import url
from . import views
from Homepage.views import post_details, gallery


urlpatterns = [
    url(r'^$', views.home, name="home-blog"),
    url('contact/', views.contact),
    #url(r'^(?P<id>\d+)/$', post_details, name='post_details'),
    url(r'^(?P<slug>[\w-]+)/$', post_details, name='post_details'),
    url('gallery/', gallery, name='gallery'),



]