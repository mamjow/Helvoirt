from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model, authenticate, login

import json
from django.http import HttpResponse

User = get_user_model()


def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    # stayloggedin = request.GET.get('stayloggedin')
    # if stayloggedin == "true":
    #  pass
    # else:
    #  request.session.set_expiry(0)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse(json.dumps({"message": "Success"}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"message": "inactive"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"message": "invalid"}), content_type="application/json")
    return HttpResponse(json.dumps({"message": "denied"}), content_type="application/json")


def signup_user(request):
    response_data = {}
    if request.method == "POST" and request.is_ajax:
        user_name = request.POST['NewUserName']
        user_email = request.POST['NewUserEmail']
        user_password = request.POST['NewUserPass1']
        user_password2 = request.POST['NewUserPass2']
        if user_password == user_password2:
            user_username = user_name.replace(" ", "").lower()
            new_user = User.objects.create(username=user_username, email=user_email,
                                           )
            new_user.set_password(user_password)

            new_user.is_active = True
            new_user.save()
            log_user = authenticate(username=user_username, password=user_password)
            # if log_user is not None:
            # login(request, log_user)
            response_data = {'message': 'Success'}
        else:
            response_data = {'message': 'Password-must-match'}

    else:
        response_data = {'message': 'Failed'}
        # logout(request)
    return JsonResponse(response_data)


def validate_username(request):
    username = request.GET.get('user_name', None)
    password = request.GET.get('user_password', None)
    if User.objects.filter(username=username).exists():
        user = authenticate(username=username, password=password)
        if user is None:
            return JsonResponse({"message": 'password'})
    else:
        return JsonResponse({"message": 'username'})
    return JsonResponse({"message": 'success'})


def validate_existingusername(request):
    username = request.GET.get('NewUserName', None)
    if User.objects.filter(username=username).exists():
        return JsonResponse({"success": False}, status=400)

    return JsonResponse({"success": True}, status=200)
