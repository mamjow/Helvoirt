from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate
from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponse
from .forms import AddPost
from django.shortcuts import get_object_or_404
from homepage.models import BlogPost

User = get_user_model()


# Create your views here.


class Panel(TemplateView):
    template_name = 'manager/panel.html'


def post_list(request):
    posts = BlogPost.objects.all().order_by('post_time').reverse()
    return render(request, 'manager/table_post.html', {'posts': posts})


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
