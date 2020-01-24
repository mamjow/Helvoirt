from django.contrib import admin
from .models import BlogPost
from .models import Contact
from .models import WebCategory
from .models import HomeAdv
from .models import PostType

# Register your models here.

class BlogpostView(admin.ModelAdmin):
    list_display = [
        'post_title',
        'post_time',
        'post_author',
    ]
    search_fields = ('post_title',)
    list_filter = ('post_author',)
    prepopulated_fields = {'slug': ('post_title',)}


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
        'PostCategory',
        'Category_summery'
    ]


admin.site.register(Contact, contactView)
admin.site.register(BlogPost, BlogpostView)
admin.site.register(WebCategory, menutabView)
admin.site.register(HomeAdv)
admin.site.register(PostType)

# Register your models here.
