from django.contrib import admin
from .models import Post
from .models import Contact
from .models import Partnership
from .models import Advertisement
from .models import Events
from .models import Section


# Register your models here.

class BlogPostView(admin.ModelAdmin):
    list_display = [
        'post_title',
        'post_available_date',
        'post_author',
    ]
    search_fields = ('post_title',)
    list_filter = ('post_author',)
    prepopulated_fields = {'slug': ('post_title',)}


class ContactView(admin.ModelAdmin):
    list_display = [
        'Name',
        'ContactTime',
        'Email',
        'Category',
        'Subject'
    ]


class MenuTabView(admin.ModelAdmin):
    list_display = [
        'partner_name',
    ]


class SectionView(admin.ModelAdmin):
    list_display = [
        'section_name',
        'section_root',
        'section_order',
        'section_visible',

    ]


admin.site.register(Contact, ContactView)
admin.site.register(Post, BlogPostView)
admin.site.register(Partnership, MenuTabView)
admin.site.register(Advertisement)
admin.site.register(Events)
admin.site.register(Section, SectionView)

# Register your models here.
