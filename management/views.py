from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate
from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponse
from .forms import AddPost, AddIntro, AddEvent
from django.shortcuts import get_object_or_404
from homepage.models import BlogPost
from .models import IntroPost, Events

User = get_user_model()


# Create your views here.


class Panel(TemplateView):
    template_name = 'manager/panel.html'


def post_list(request):
    posts = BlogPost.objects.all().order_by('post_time').reverse()
    return render(request, 'manager/table_post.html', {'posts': posts})


def intro_page(request):
    template = 'manager/introduce.html'
    context = {
        'form': AddIntro,
    }
    return render(request, template, context)


def calender_page(request):
    event_list = Events.objects.all()
    template = 'manager/calender.html'
    context = {
        'form': AddEvent,
        'events': event_list
    }
    return render(request, template, context)


def update_post(request, pk):
    obj = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = AddPost(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.post_author = request.user
            instance.save()
            return redirect('/panel/posts/')
    template = 'manager/includes/updatepost.html'
    context = {
        'form': AddPost(instance=obj),
        'oid': pk,
        'image': obj,
    }
    return render(request, template, context)


def add_post(request):
    if request.method == 'POST':
        form = AddPost(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.post_author = request.user
            instance.save()
            return redirect('/panel/posts/')
    template = 'manager/includes/newpost.html'
    context = {
        'form': AddPost,
    }
    return render(request, template, context)


def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        post.delete()
    data = ('success' + post.post_title)
    return JsonResponse(data, safe=False)
