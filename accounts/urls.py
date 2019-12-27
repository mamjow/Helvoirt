from django.urls import path
from django.conf.urls import url
# from .views import SignUp
from accounts import views

urlpatterns = [
    url(r'^signup/$', views.signup_user, name='signupuser'),
    # url(r'^ajax/signup/$', views.user_signup, name='signupuser'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    url(r'^ajax/validate_existingusername/$', views.validate_existingusername, name='validate_existingusername'),
]