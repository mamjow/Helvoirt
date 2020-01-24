import os
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
from accounts.models import CustomUser
from ckeditor_uploader.fields import RichTextUploadingField

user = CustomUser


def path_and_rename(instance, filename):
    upload_to = 'intro-photos/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    return os.path.join(upload_to, filename)


class Events(models.Model):
    STATUS = (
        ('top', 'Top event'),
        ('once', 'One casual event'),
        ('weekly', 'Once per week'),
        ('monthly', 'Oce per month'),
        ('pre', 'Pre planning'),
    )
    event_title = models.CharField(max_length=50, null=False)
    event_def_date = models.DateField(null=True)
    event_plan = models.CharField(max_length=10, choices=STATUS, default='pre')
    event_more = models.ForeignKey('IntroPost', on_delete=models.CASCADE, null=True, blank=True)
    event_image = models.ImageField(upload_to='events-upload/', null=True, blank=True)


class IntroPost(models.Model):
    post_title = models.CharField(max_length=200, null=False)
    post_header = models.TextField(max_length=250, null=True, blank=True)
    # post_Body = RichTextField()
    post_body = RichTextUploadingField(null=True)
    post_images = models.ImageField(upload_to=path_and_rename, null=True, blank=True)
    post_author = models.ForeignKey(
        user,
        on_delete=models.CASCADE,
        limit_choices_to={'is_staff': True},
        null=True,
        default=user,
    )
    post_sponsor = models.ForeignKey('homepage.WebCategory', on_delete=models.CASCADE, default=1)
    post_type = models.ForeignKey('homepage.PostType', on_delete=models.CASCADE, default=1)
