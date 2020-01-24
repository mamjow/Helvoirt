from django.forms import ModelForm
from homepage.models import BlogPost
from .models import Events, IntroPost


class AddPost(ModelForm):
    class Meta:
        model = BlogPost
        fields = ('post_title', 'post_header', 'post_images', 'post_time',
                  'post_body',)


class AddEvent(ModelForm):
    class Meta:
        model = Events
        fields = ('event_title', 'event_def_date', 'event_plan', 'event_more', 'event_image')


class AddIntro(ModelForm):
    class Meta:
        model = IntroPost
        fields = '__all__'
