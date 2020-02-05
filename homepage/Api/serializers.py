from rest_framework import serializers
from homepage.models import News


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('post_title', 'post_Body', 'post_time', 'pk')
