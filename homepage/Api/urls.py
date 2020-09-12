from django.urls import path
from homepage.Api import views as api_view
from rest_framework.authtoken import views as tviews

app_name = "blog_api"

# Rest API
urlpatterns = [
    path('api-token-auth/', tviews.obtain_auth_token, name='api-token-auth'),

    path('', api_view.apioverview),
    path('post-list', api_view.post_list),
    path('post-create', api_view.post_create),
    path('post-detail/<str:pk>/', api_view.post_details),
]
