from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import get_user_model, authenticate
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import AddPost
from django.shortcuts import get_object_or_404
from homepage.models import BlogPost, WebCategory

User = get_user_model()


# Create your views here.


class Panel(TemplateView):
    template_name = 'manager/modiriat.html'


def add_post(request):
    if request.method == 'POST':
        form = AddPost(request.POST or None, request.FILES or None)
    else:
        form = AddPost()
    return save_post_form(request, form, 'manager/includes/newpost.html')


def update_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    if request.method == 'POST':
        form = AddPost(request.POST, request.FILES, instance=post)
    else:
        form = AddPost(instance=post)
    return save_post_form(request, form, 'manager/includes/updatepost.html')


def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    data = dict()
    if request.method == 'POST':
        post.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        posts = BlogPost.objects.all()
        data['html_book_list'] = render_to_string('manager/table_post.html', {
            'posts': post
        })
    else:
        context = {'post': post}
        data['html_form'] = render_to_string('manager/includes/deletepost.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


def save_post_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        form = AddPost(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            posts = BlogPost.objects.all().order_by('post_time').reverse()
            data['html_post_list'] = render_to_string('manager/includes/list_post.html', {
                'posts': posts
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def post_list(request):
    posts = BlogPost.objects.all().order_by('post_time').reverse()
    return render(request, 'manager/table_post.html', {'posts': posts})
