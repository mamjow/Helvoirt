from django.contrib import admin
from .models import News
from .models import Contact
from .models import Sponsor
from .models import HomeAdv
from .models import IntroType

# Register your models here.

class BlogpostView(admin.ModelAdmin):
    list_display = [
        'news_title',
        'news_time',
        'news_author',
    ]
    search_fields = ('news_title',)
    list_filter = ('news_author',)
    prepopulated_fields = {'slug': ('news_title',)}


class contactView(admin.ModelAdmin):
    list_display = [
        'Name',
        'ContactTime',
        'Email',
        'Category',
        'Subject'
    ]

class menutabView(admin.ModelAdmin):
    list_display = [
        'Title',
    ]


admin.site.register(Contact, contactView)
admin.site.register(News, BlogpostView)
admin.site.register(Sponsor, menutabView)
admin.site.register(HomeAdv)
admin.site.register(IntroType)

# Register your models here.
