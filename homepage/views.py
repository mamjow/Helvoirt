from datetime import date

from django.shortcuts import render, render_to_response, redirect
import os

from django.template.loader import render_to_string
from django.views.generic import TemplateView

from .models import Post
from .models import Partnership
from .models import Advertisement
from .models import Events
from .models import Section
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse, HttpResponse
from .forms import AddPost, AddEvent
from django.shortcuts import get_object_or_404

NEWS_POST_PER_PAGE = 6


class Panel(TemplateView):
    template_name = 'manager/panel.html'


def dashboard(request):
    return render(request, 'manager/panel.html')


def home(request):
    template = "content/homepage.html"
    object_all_post = Post.objects.all().filter(post_available_date__date__lt=date.today()).order_by(
        'post_available_date').reverse()
    qN = object_all_post.filter()
    eqs = Events.objects.all()
    ms = Partnership.objects.all()
    list_sections = Section.objects.all().order_by('section_order')
    path = "static/image"  # insert the path to your directory
    img_list = os.listdir(path)
    adv_gif = Advertisement.objects.all()

    # Pagination
    page = request.GET.get('page', 1)
    news_post_paginator = Paginator(qN, NEWS_POST_PER_PAGE)
    try:
        qN = news_post_paginator.page(page)
    except PageNotAnInteger:
        qN = news_post_paginator(NEWS_POST_PER_PAGE)

    except EmptyPage:
        qN = news_post_paginator(qN.paginator.num_pages)

    context = {
        'event_list': eqs,
        'object_list': qN,
        'partner_list': ms,
        'menuactive': 'Home',
        'images': img_list,
        'adv': adv_gif,
        'sec_list': list_sections.filter(section_root=None).filter(section_visible=True)
    }
    return render(request, template, context)


def post_details(request, slug=None):
    template = "content/post-card-full.html"
    qs = Post.objects.get(slug=slug)
    context = {
        'post_details': qs,
    }
    return render(request, template, context)


def section_show(request, id):
    template = "content/section.html"
    qs = Post.objects.filter(post_section=id)
    list_sections = Section.objects.all().order_by('section_order')
    context = {
        'section_news': qs.filter(post_type="Nieuws"),
        'section_intro': qs.filter(post_type="Introductie"),
        'sec_list': list_sections,
    }
    return render(request, template, context)


# def contact(request):
#     ms = Sponsor.objects.all()
#     if request.method == 'POST':
#
#         form = Contact(request.POST or None)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#
#             print(name, email)
#             messages.info(request, 'Your password has been changed successfully!')
#             form.save()
#     template = "content/contactus.html"
#     context = {
#         'form': ContactUsForm,
#         'menu_list': ms,
#         'menuactive': 'Contact Us'
#     }
#     return render(request, template, context)


def gallery(request):
    path = "C:\\Users\\mjmos\\PycharmProjects\\Helvoirthuis\\home\\static\\image"  # insert the path to your directory
    img_list = os.listdir(path)
    return render_to_response('content/gallery.html', {'images': img_list})


def get_all_articles(request):
    article = Post.objects.all().order_by('post_available_date').reverse()
    context = {
        'article': article,
    }
    return render(request, 'manager/posts_manager.html', context)


def delete_article(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
    data = ('success ' + post.post_title)
    return JsonResponse(data, safe=False)


def update_article(request, pk):
    obj = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = AddPost(request.POST or None, request.FILES or None, instance=obj)
    else:
        form = AddPost(instance=obj)
    return save_article(request, form, pk, 'manager/includes/posts_form.html')


def add_article(request):
    pk = 0
    if request.method == 'POST':
        form = AddPost(request.POST or None, request.FILES or None)
    else:
        form = AddPost()
    return save_article(request, form, pk, 'manager/includes/posts_form.html')


def save_article(request, form, pk, template_name):
    data = dict()
    article = Post
    if request.method == 'GET':
        if pk == 0:
            form = AddPost()
            context = {'form': form,
                       }
        else:
            obj = get_object_or_404(article, pk=pk)
            form = AddPost(request.POST or None, request.FILES or None, instance=obj)
            context = {'form': form, 'image': obj}
        data['html_form'] = render_to_string(template_name, context, request=request)
    else:
        if pk != 0:
            obj = get_object_or_404(article, pk=pk)
            form = AddPost(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.post_author = request.user
            instance.save()
            data['form_is_valid'] = True
            article_objects = article.objects.all()
            data['html_book_list'] = render_to_string('manager/includes/posts_table_body.html', {
                'article': article_objects
            })
        else:
            data['form_is_valid'] = False
    return JsonResponse(data)


def calender_page(request):
    event_list = Events.objects.all()
    template = 'manager/calender.html'
    context = {
        'eventform': AddEvent,
        'events': event_list
    }
    return render(request, template, context)


def save_event(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            form = AddEvent()
        else:
            obj = get_object_or_404(Events, pk=pk)
            form = AddEvent(request.POST or None, request.FILES or None, instance=obj)
        template = 'manager/calender.html'
        event_list = Events.objects.all()
        context = {
            'eventform': form,
            'events': event_list
        }
        return render(request, template, context)
    else:
        if pk == 0:
            form = AddEvent(request.POST or None, request.FILES or None)
        else:
            obj = get_object_or_404(Events, pk=pk)
            form = AddEvent(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()
        return redirect('calender_page')


def new_event(request):
    form = AddEvent()
    context = {'form': form}
    html_form = render_to_string('manager/includes/posts_form.html',
                                 context,
                                 request=request,
                                 )
    print(context)
    return JsonResponse(context)


def delete_event(request, pk):
    obj = get_object_or_404(Events, pk=pk)
    print(pk)
    obj.delete()
    event_list = Events.objects.all()
    template = 'manager/calender.html'
    context = {
        'form': AddEvent,
        'events': event_list
    }
    return render(request, template, context)
