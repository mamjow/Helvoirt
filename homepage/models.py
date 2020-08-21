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


def path_and_rename(instance, filename):
    upload_to = 'intro-photos/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    return os.path.join(upload_to, filename)


class Section(models.Model):
    section_id = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=40, unique=True)
    section_icon = models.CharField(max_length=50, null=True)
    section_root = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    section_order = models.IntegerField(null=False, default=0)
    section_summery = models.TextField(null=True)

    class Meta:
        db_table = 'section'

    def __str__(self):
        return self.section_name


class Post(models.Model):
    Article_type = (('Nieuws', 'Het laatste nieuws'),
                    ('Introductie', 'Een introductie'))
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=50, null=False)
    post_header = models.TextField(max_length=250, null=True, blank=True)
    post_body = RichTextUploadingField(null=True)
    post_expire_date = models.DateTimeField(null=True, blank=True)
    post_available_date = models.DateTimeField(default=timezone.now, null=False)
    post_image = models.ImageField(upload_to='post-uploads/', null=True, blank=True)
    post_section = models.ForeignKey(Section, on_delete=models.CASCADE, default=1)
    post_type = models.CharField(max_length=30, choices=Article_type, default="Nieuws")
    post_author = models.ForeignKey(
        user,
        on_delete=models.CASCADE,
        limit_choices_to={'is_staff': True},
        null=True,
        default=user,
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.post_title

    class Meta:
        db_table = 'post'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.post_title)
        self.post_header = self.post_title
        # if self.post_images is None:
        #     self.post_images = default_place_pics()
        super(Post, self).save(*args, **kwargs)


class Contact(models.Model):
    Name = models.CharField(max_length=80, null=False)
    ContactTime = models.DateTimeField(default=timezone.now, null=False)
    Email = models.EmailField(max_length=80, null=False)
    Category = models.CharField(max_length=80, null=False)
    Subject = models.CharField(max_length=80, null=False)
    Body = models.TextField(null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'contact_request'


class Partnership(models.Model):
    partner_name = models.CharField(max_length=40, default="HelvoirThuis")
    partner_link = models.URLField(max_length=128, null=False)
    partner_logo = models.ImageField(upload_to='partners-logo/', null=True, blank=True)
    short_summery = models.TextField(null=True)

    class Meta:
        db_table = 'partnership'
        verbose_name_plural = "partnership"

    def __str__(self):
        return self.partner_name


class SliderGallery(models.Model):
    image = models.ImageField(upload_to='slidergallery', null=False)

    class Meta:
        db_table = 'gallery'


class Advertisement(models.Model):
    adv_title = models.CharField(max_length=40, null=False)
    adv_address = models.TextField(null=True)
    adv_images = models.FileField(upload_to='uploads/', null=True)

    class Meta:
        db_table = 'advertisement'


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
    event_more = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    event_image = models.ImageField(upload_to='events-upload/', null=True, blank=True)

    def __str__(self):
        return self.event_title
