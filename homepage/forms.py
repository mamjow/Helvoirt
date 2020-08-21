from django.forms import ModelForm, forms
from homepage.models import Post
from .models import Events


class AddPost(ModelForm):
    class Meta:
        model = Post
        fields = ('post_title', 'post_header', 'post_image', 'post_available_date',
                  'post_body',)

        def clean_something_unique_or_null(self):
            if self.cleaned_data['something_unique_or_null'] == "":
                return None
            else:
                return self.cleaned_data['something_unique_or_null']


class AddEvent(ModelForm):
    class Meta:
        model = Events
        fields = ('event_title', 'event_def_date', 'event_plan', 'event_more', 'event_image')
