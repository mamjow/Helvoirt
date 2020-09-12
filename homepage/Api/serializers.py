from rest_framework import serializers, fields

from homepage.models import Post


class BlogPostSerializer(serializers.ModelSerializer):
    post_author = serializers.StringRelatedField()
    post_available_date = fields.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = Post
        fields = (
            'post_id',
            'post_title',
            'post_header',
            'post_body',
            'post_expire_date',
            'post_available_date',
            'post_image',
            'post_section',
            'post_type',
            'post_author',
            'slug')
