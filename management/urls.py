from django.urls import path
from django.conf.urls import url
# from django.views.generic import TemplateView
from management import views
urlpatterns = [
    url(r'^dashboard/$', views.Panel.as_view(template_name='manager/panel.html'), name='dashboard'),
    # homepage post
    url(r'^news/$', views.news_list, name='news_list'),
    url(r'^news/add/$', views.add_news, name='add_news'),
    url(r'^news/(?P<pk>\d+)/update/$', views.update_news, name='update_news'),
    url(r'^news/(?P<pk>\d+)/delete/$', views.delete_news, name='delete_news'),
    #  Intro post
    url(r'^posts/$', views.intro_page, name='intro_page'),
    url(r'^posts/create/$', views.add_intro, name='add_intro'),
    url(r'^posts/(?P<pk>\d+)/update/$', views.update_intro, name='update_intro'),
    url(r'^posts/(?P<pk>\d+)/delete/$', views.book_delete, name='book_delete'),
    #  calender and events
    url(r'^calender/$', views.calender_page, name='calender_page'),
    url(r'^calender/add/$', views.new_event, name='event_add'),
    url(r'^calender/(?P<pk>\d+)/edit/$', views.save_event, name='event_edit'),
    url(r'^calender/(?P<pk>\d+)/delete/$', views.delete_event, name='event_delete'),
]
