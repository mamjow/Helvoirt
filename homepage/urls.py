from django.conf.urls import url
from . import views
from .Api import views as api_view
from django.urls import path

from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.home, name="home-blog"),
    # url('contact/', views.contact),
    # url(r'^(?P<id>\d+)/$', post_details, name='post_details'),
    url(r'^article/(?P<slug>[\w-]+)/view/$', views.post_details, name='post_details'),
    url('gallery/', views.gallery, name='gallery'),

    # homepage post
    url(r'^article/$', views.get_all_articles, name='news_list'),
    url(r'^article/add/$', views.add_article, name='add_article'),
    url(r'^article/(?P<pk>\d+)/update/$', views.update_article, name='update_news'),
    url(r'^article/(?P<pk>\d+)/delete/$', views.delete_article, name='delete_news'),

    # Section
    url(r'^section/(?P<id>\d+)/view/$', views.section_show, name='section_show'),

    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^dashboards/$', views.Panel.as_view(template_name='manager/panel.html'), name='dashboards'),
    #  calender and events
    url(r'^calender/$', views.calender_page, name='calender_page'),
    url(r'^calender/add/$', views.new_event, name='event_add'),
    url(r'^calender/(?P<pk>\d+)/edit/$', views.save_event, name='event_edit'),
    url(r'^calender/(?P<pk>\d+)/delete/$', views.delete_event, name='event_delete'),

]
