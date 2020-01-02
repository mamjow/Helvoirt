from django.forms import ModelForm
from homepage.models import BlogPost
from django import forms


class AddPost(ModelForm):
    class Meta:
        model = BlogPost
        fields = ('post_title', 'post_images', 'post_category', 'post_type', 'post_time',
                  'post_author', 'post_body',)

        # widgets = {
        #     'post_title': forms.TextInput(
        #         attrs={'class': 'form-control',
        #                'id': 'PostBodyInput'}
        #     ),
        #     'post_body': forms.Textarea(
        #         attrs={'class': 'form-control'}
        #     ),
        #     'post_type': forms.Select(
        #         attrs={'class': 'form-control'}
        #     ),
        #     'post_category': forms.Select(
        #         attrs={'class': 'form-control'}
        #     ),
        #     'post_author': forms.Select(
        #         attrs={'class': 'form-control'}
        #     ),
        #
        # }

    # def clean_post_title(self, *args, **kwargs):
    #     post_title = self.cleaned_data.get("post_title")
    #     return post_title
    #
    # def clean_post_body(self, *args, **kwargs):
    #     post_body = self.cleaned_data.get("post_body")
    #     return post_body
    #
    #
    #
    # def clean_post_time(self, *args, **kwargs):
    #     post_time = self.cleaned_data.get("post_time")
    #     return post_time
    #
    # def clean_post_author(self, *args, **kwargs):
    #     post_author = self.cleaned_data.get("post_author")
    #     return post_author
    #
    # def clean_post_category(self, *args, **kwargs):
    #     post_category = self.cleaned_data.get("post_category")
    #     return post_category
    #
    # def clean_post_type(self, *args, **kwargs):
    #     post_type = self.cleaned_data.get("post_type")
    #     return post_type
    #
