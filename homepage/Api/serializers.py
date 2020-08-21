from rest_framework import serializers
from homepage.models import Post


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('post_title', 'post_Body', 'post_time', 'pk')
