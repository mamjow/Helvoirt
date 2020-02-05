from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponse
from .forms import AddNews, AddIntro, AddEvent
from django.shortcuts import get_object_or_404
from homepage.models import News
from .models import IntroPost, Events

User = get_user_model()


# Create your views here.


class Panel(TemplateView):
    template_name = 'manager/panel.html'


def news_list(request):
    news = News.objects.all().order_by('news_time').reverse()
    context = {
        'news': news,
    }
    return render(request, 'manager/news_manager.html', context)


def delete_news(request, pk):
    post = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        post.delete()
    data = ('success' + post.news_title)
    return JsonResponse(data, safe=False)


def update_news(request, pk):
    obj = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = AddNews(request.POST or None, request.FILES or None, instance=obj)
    else:
        form = AddNews(instance=obj)
    return save_news(request, form, pk, 'manager/includes/news_form.html')


def add_news(request):
    pk = 0
    if request.method == 'POST':
        form = AddNews(request.POST or None, request.FILES or None)
    else:
        form = AddNews()
    return save_news(request, form, pk, 'manager/includes/news_form.html')


def save_news(request, form, pk, template_name):
    data = dict()
    if request.method == 'GET':
        if pk == 0:
            form = AddNews()
            context = {'form': form,
                       }
        else:
            obj = get_object_or_404(News, pk=pk)
            form = AddNews(request.POST or None, request.FILES or None, instance=obj)
            context = {'form': form, 'image': obj}
        data['html_form'] = render_to_string(template_name, context, request=request)
    else:
        if pk != 0:
            obj = get_object_or_404(News, pk=pk)
            form = AddNews(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.news_author = request.user
            instance.save()
            data['form_is_valid'] = True
            newsobjects = News.objects.all()
            data['html_book_list'] = render_to_string('manager/includes/news_table_body.html', {
                'news': newsobjects
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
    print(pk, request.method)
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
    html_form = render_to_string('manager/includes/news_form.html',
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


def intro_page(request):
    template = 'manager/introduce.html'
    intro_list = IntroPost.objects.all()
    event_list = Events.objects.all()
    context = {
        'form': AddIntro,
        'intro_list': intro_list,
        'events': event_list
    }
    return render(request, template, context)


def update_intro(request, pk):
    obj = get_object_or_404(IntroPost, pk=pk)
    if request.method == 'POST':
        form = AddIntro(request.POST or None, request.FILES or None, instance=obj)
    else:
        form = AddIntro(instance=obj)
    return save_intro(request, form, pk, 'manager/includes/intro_form.html')


def add_intro(request):
    pk = 0
    if request.method == 'POST':
        form = AddIntro(request.POST or None, request.FILES or None)
    else:
        form = AddIntro()
    return save_intro(request, form, pk, 'manager/includes/intro_form.html')


def save_intro(request, form, pk, template_name):
    data = dict()
    if request.method == 'GET':
        if pk == 0:
            form = AddIntro()
            context = {'form': form,
                       }
        else:
            obj = get_object_or_404(IntroPost, pk=pk)
            form = AddIntro(request.POST or None, request.FILES or None, instance=obj)
            context = {'form': form, 'image': obj}
        data['html_form'] = render_to_string(template_name, context, request=request)
    else:
        if pk != 0:
            obj = get_object_or_404(IntroPost, pk=pk)
            form = AddIntro(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.post_author = request.user
            instance.save()
            data['form_is_valid'] = True
            intro_list = IntroPost.objects.all()
            data['html_book_list'] = render_to_string('manager/includes/intro_table.html', {
                'intro_list': intro_list
            })
        else:
            data['form_is_valid'] = False
    return JsonResponse(data)


def book_delete(request, pk):
    book = get_object_or_404(IntroPost, pk=pk)
    data = dict()
    if request.method == 'POST':
        book.delete()
        data['form_is_valid'] = True
        books = IntroPost.objects.all()
        data['html_book_list'] = render_to_string('books/includes/partial_book_list.html', {
            'books': books
        })
    else:
        context = {'book': book}
        data['html_form'] = render_to_string('books/includes/partial_book_delete.html', context, request=request)
    print(data)
    return JsonResponse(data)
