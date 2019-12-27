from rest_framework import serializers
from Homepage.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('post_title', 'post_Body', 'post_time', 'pk')
