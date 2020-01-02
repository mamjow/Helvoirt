from django.shortcuts import render
import os
#from .forms import ContactUsForm
#from .forms import NewPost
from .models import BlogPost
from .models import WebCategory
from .models import HomeAdv
from django.contrib import messages


def home(request):
    template = "content/homepage.html"
    qs = BlogPost.objects.all().order_by('post_time').reverse()
    ms = WebCategory.objects.all()
    path = "static/image"  # insert the path to your directory
    img_list = os.listdir(path)
    adv_gif = HomeAdv.objects.all()

    context = {
        'object_list': qs,
        'menu_list': ms,
        'menuactive': 'Home',
        'images': img_list,
        'adv': adv_gif
    }
    return render(request, template, context)


def post_details(request, slug=None):
    template = "content/postview.html"
    qs = BlogPost.objects.filter(slug=slug).first()
    context = {
        'post_details': qs,
    }
    return render(request, template, context)


def contact(request):
    ms = WebCategory.objects.all()
    if request.method == 'POST':

        form = ContactUsForm(request.POST or None)
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


