from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import get_user_model, authenticate
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import AddPost

from Homepage.models import BlogPost

from django.shortcuts import get_object_or_404
from Homepage.models import BlogPost, WebCategory

User = get_user_model()


# Create your views here.


class Panel(TemplateView):
    template_name = 'manager/modiriat.html'


def add_post(request):
    data = dict()
    form = AddPost()
    context = {
        'form': form
    }
    data['html_form'] = render_to_string('manager/newpost.html',
                                         context,
                                         request=request,
                                         )
    return JsonResponse(data)


# def add_post(request):
#
#     inform = AddPost(request.POST or None, request.FILES or None)
#     if request.method == 'POST' or None:
#         inform.save()
#     template = "manager/add_post.html"
#     context = {
#         'form': inform
#     }
#     return render(request, template, context)


def post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'manager/table_post.html', {'posts': posts})
