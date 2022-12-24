from rest_framework.response import Response
from rest_framework.views import APIView
from blog.models import Post , Category
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostSerializers , CategorySerializers
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter , OrderingFilter
from .pagination import DefaultPagination
'''
from rest_framework.decorators import api_view

@api_view(['GET',"POST"])
def listView(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serialized_posts = PostSerializers(posts,many=True) 
        return Response(serialized_posts.data)
    elif request.method:
        serialized_posts = PostSerializers(data=request.data)
        if serialized_posts.is_valid():
            serialized_posts.save()
            return Response(serialized_posts.data)
        else :
            return Response(serialized_posts.errors)

@api_view(['GET','PUT','DELETE'])
def detailView(request,id):
    post = get_object_or_404(Post,id=id)
    if request.method == 'GET':
        serialized_post = PostSerializers(post) 
        return Response(serialized_post.data)
    elif request.method == 'PUT':
        serialized_post = PostSerializers(post,data=request.data) 
        serialized_post.is_valid(raise_exception=True)
        serialized_post.save()
        return Response(serialized_post.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response({'detail':'itemremoved'},status=200)

class PostList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializers
    def get(self,request):
        posts = Post.objects.all()
        serialized_posts = PostSerializers(posts,many=True) 
        return Response(serialized_posts.data)

    def post(self,request):
        serialized_posts = PostSerializers(data=request.data)
        if serialized_posts.is_valid():
            serialized_posts.save()
            return Response(serialized_posts.data)
        else :
            return Response(serialized_posts.errors)

class PostDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializers 
    def get(self,request,id):
        post = get_object_or_404(Post,id=id,status=True)
        serialized_post = PostSerializers(post) 
        return Response(serialized_post.data)

    def put(self,request,id):
        post = get_object_or_404(Post,id=id,status=True)
        serialized_post = PostSerializers(post,data=request.data) 
        serialized_post.is_valid(raise_exception=True)
        serialized_post.save()
        return Response(serialized_post.data)

    def delete(self,request,id):
        post = get_object_or_404(Post,id=id,status=True)
        post.delete()
        return Response({'detail':'itemremoved'},status=200)
'''

class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializers 
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['category','id', 'author','title']
    search_fields = ['=title',]
    ordering_fields = ['published_date']
    pagination_class = DefaultPagination


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializers 
    