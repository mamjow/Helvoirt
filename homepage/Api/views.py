from datetime import date
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import BlogPostSerializer

from homepage.models import Post


# class BlogListAPI(generics.ListCreateAPIView):
#     lookup_field = 'pk'
#     queryset = Post.objects.all()
#     serializer_class = BlogPostSerializer
#     # permission_classes = (IsAdminUser,)
#

@api_view(['GET'])
def apioverview(request):
    api_url = {
        'List View': '/post-list/',
        'detail View': '/post-list/str:pk/',
        'Create': '/post-create/',
        'update': '/post-update/<str:pk>/',
        'Delete': '/post-delete/<str:pk>/',
    }
    # queryset = Post.objects.all()
    # serializer = BlogPostSerializer
    return Response(api_url)


@api_view(['GET'])
@permission_classes([])
def post_list(request):
    posts = Post.objects.all().filter(post_available_date__date__lte=date.today()).order_by(
        'post_available_date').reverse()
    serializer = BlogPostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def post_details(request, pk):
    posts = Post.objects.get(post_id=pk)
    serializer = BlogPostSerializer(posts, many=False)
    return Response(serializer.data)


@api_view(['POST'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def post_create(request):
    serializer = BlogPostSerializer(data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
    except Exception as e:
        print(e)
    print(serializer.errors)
    return Response(serializer.data)
