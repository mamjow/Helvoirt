from django.shortcuts import render
import os
from .models import News
from .models import Sponsor
from .models import HomeAdv
from management.models import Events
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

NEWS_POST_PER_PAGE = 6


def home(request):
    template = "content/homepage.html"
    news_post = News.objects.all().order_by('news_time').reverse()
    qN = news_post.filter()
    eqs = Events.objects.all()
    ms = Sponsor.objects.all()
    path = "static/image"  # insert the path to your directory
    img_list = os.listdir(path)
    adv_gif = HomeAdv.objects.all()

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
        'menu_list': ms,
        'menuactive': 'Home',
        'images': img_list,
        'adv': adv_gif
    }
    return render(request, template, context)


def post_details(request, slug=None):
    template = "content/post-card-full.html"
    qs = News.objects.get(slug=slug)
    context = {
        'post_details': qs,
    }
    return render(request, template, context)


def contact(request):
    ms = Sponsor.objects.all()
    if request.method == 'POST':

        form = Contact(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            print(name, email)
            messages.info(request, 'Your password has been changed successfully!')
            form.save()
    template = "content/contactus.html"
    context = {
        'form': ContactUsForm,
        'menu_list': ms,
        'menuactive': 'Contact Us'
    }
    return render(request, template, context)


def gallery(request):
    path = "C:\\Users\\mjmos\\PycharmProjects\\Helvoirthuis\\home\\static\\image"  # insert the path to your directory
    img_list = os.listdir(path)
    return render_to_response('content/gallery.html', {'images': img_list})


