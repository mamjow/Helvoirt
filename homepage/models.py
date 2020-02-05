import os
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
from accounts.models import CustomUser
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
user = CustomUser

def default_place_pics():
    return "post-default.jpg"


class News(models.Model):
    news_title = models.CharField(max_length=200, null=False)
    news_header = models.TextField(max_length=250, null=True, blank=True)
    # post_Body = RichTextField()
    news_body = RichTextUploadingField(null=True)
    news_images = models.ImageField(upload_to='post-uploads/', null=True, blank=True)
    news_time = models.DateTimeField(default=timezone.now, null=False)
    news_author = models.ForeignKey(
        user,
        on_delete=models.CASCADE,
        limit_choices_to={'is_staff': True},
        null=True,
        default=user,
    )
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.news_title)
        self.news_header = self.news_title
        # if self.post_images is None:
        #     self.post_images = default_place_pics()
        super(News, self).save(*args, **kwargs)


class Contact(models.Model):
    Name = models.CharField(max_length=80, null=False)
    ContactTime = models.DateTimeField(default=timezone.now, null=False)
    Email = models.EmailField(max_length=80, null=False)
    Category = models.CharField(max_length=80, null=False)
    Subject = models.CharField(max_length=80, null=False)
    Body = models.TextField(null=False)

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    Title = models.CharField(max_length=40, default="HelvoirThuis")
    Short_summery = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Sponsor"

    def __str__(self):
        return self.Title


class IntroType(models.Model):
    Type = models.CharField(max_length=40, default="Blog Post")
    Type_summery = models.TextField(null=True)

    def __str__(self):
        return self.Type


class SliderGallery(models.Model):
    image = models.ImageField(upload_to='slidergallery', null=False)


class HomeAdv(models.Model):
    adv_title = models.CharField(max_length=40, null=False)
    adv_address = models.TextField(null=True)
    adv_images = models.FileField(upload_to='uploads/', null=True)


from django.db import models

# Create your models here.
