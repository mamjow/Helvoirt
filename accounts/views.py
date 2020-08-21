from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import redirect
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
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        data = {'username': username, 'email': email, 'password2': password2, 'password1': password1}
        form = CustomUserCreationForm(data=data)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return HttpResponse(json.dumps({"message": "Success"}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"message": form.errors}), content_type="application/json")
    else:
        form = CustomUserCreationForm()
    return HttpResponse(json.dumps({"message": "Denied"}), content_type="application/json")


def validate_username(request):
    username = request.POST.get('user_name', None)
    password = request.POST.get('user_password', None)
    if User.objects.filter(username=username).exists():
        user = authenticate(username=username, password=password)
        if user is None:
            return JsonResponse({"message": 'password'})
    else:
        return JsonResponse({"message": 'username'})
    return JsonResponse({"message": 'success'})


def validate_existingusername(request):
    username = request.POST.get('NewUserName', None)
    if User.objects.filter(username=username).exists():
        return JsonResponse({"success": False}, status=400)

    return JsonResponse({"success": True}, status=200)
