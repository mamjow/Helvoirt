from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
from accounts.models import CustomUser
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

user = CustomUser


class BlogPost(models.Model):
    post_title = models.CharField(max_length=200, null=False)
    post_header = models.TextField(max_length=250, )
    # post_Body = RichTextField()
    post_body = RichTextUploadingField(null=True)
    post_images = models.ImageField(upload_to='uploads/', null=True)
    post_time = models.DateTimeField(default=timezone.now, null=False)
    post_author = models.ForeignKey(
        user,
        on_delete=models.CASCADE,
        limit_choices_to={'is_staff': True},
        null=True
    )
    post_category = models.ForeignKey('WebCategory', on_delete=models.CASCADE, default=1)
    post_type = models.ForeignKey('PostType', on_delete=models.CASCADE, default=1)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.post_title)
        self.post_header = self.post_title
        super(BlogPost, self).save(*args, **kwargs)


class Contact(models.Model):
    Name = models.CharField(max_length=80, null=False)
    ContactTime = models.DateTimeField(default=timezone.now, null=False)
    Email = models.EmailField(max_length=80, null=False)
    Category = models.CharField(max_length=80, null=False)
    Subject = models.CharField(max_length=80, null=False)
    Body = models.TextField(null=False)

    def __str__(self):
        return self.name


class WebCategory(models.Model):
    PostCategory = models.CharField(max_length=40, default="Home Page")
    Category_summery = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.PostCategory


class PostType(models.Model):
    PostType = models.CharField(max_length=40, default="Blog Post")
    PostType_summery = models.TextField(null=True)

    def __str__(self):
        return self.PostType


class HomeAdv(models.Model):
    adv_title = models.CharField(max_length=40, null=False)
    adv_address = models.TextField(null=True)
    adv_images = models.FileField(upload_to='uploads/', null=True)


from django.db import models

# Create your models here.
