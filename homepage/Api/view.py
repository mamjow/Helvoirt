from rest_framework import generics
from .serializers import BlogPostSerializer
from rest_framework.permissions import IsAdminUser
from homepage.models import BlogPost


class BlogListAPI(generics.ListCreateAPIView):
    lookup_field = 'pk'
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    # permission_classes = (IsAdminUser,)
