from django.forms import ModelForm, forms
from homepage.models import News
from .models import Events, IntroPost


class AddNews(ModelForm):
    class Meta:
        model = News
        fields = ('news_title', 'news_header', 'news_images', 'news_time',
                  'news_body',)


class AddEvent(ModelForm):
    class Meta:
        model = Events
        fields = ('event_title', 'event_def_date', 'event_plan', 'event_more', 'event_image')


class AddIntro(ModelForm):
    class Meta:
        model = IntroPost
        exclude = ('post_author',)
        fields = '__all__'
