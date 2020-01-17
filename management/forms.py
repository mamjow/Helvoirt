from django.forms import ModelForm
from homepage.models import BlogPost


class AddPost(ModelForm):
    class Meta:
        model = BlogPost
        fields = ('post_title', 'post_header', 'post_images', 'post_category', 'post_type', 'post_time',
                  'post_body',)
