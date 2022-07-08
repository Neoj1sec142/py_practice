from django.shortcuts import render
from rest_framework import generics, status, permissions
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from .models import User, Post, Comment # ...your other models
from .serializers import UserSerializer, PostSerializer, GetPostSerializer, CommentSerializer # ...your other serializers
# User views
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        return Response(users)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailByUsername(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    def post(self, request):
        refresh_token = request.data['refresh_token']
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)


class PostView(APIView):
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        if post_id:
            try:
                post = Post.objects.get(id=post_id)
                return Response(GetPostSerializer(post).data, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response({'error': "No post found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            posts = Post.objects.all()
            posts_data = PostSerializer(posts, many=True).data
            return Response(data=posts_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, name=request.user.name, avatar=request.user.avatar)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        try:
            post = Post.objects.get(id=post_id)
            if post.user.id == request.user.id:
                post.delete()
                return Response({'msg': 'Post deleted'}, status=status.HTTP_200_OK)
            else:
                return Response({'Error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        except ObjectDoesNotExist:
            return Response({'error': "No post found"}, status=status.HTTP_404_NOT_FOUND)


class LikeUnlikeView(APIView):
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        try:
            post = Post.objects.get(id=post_id)
            liked = post.likes.filter(id=request.user.id).exists()

            if liked:
                post.likes.remove(request.user.id)
                return Response(GetPostSerializer(post).data, status=status.HTTP_200_OK)
            else:
                post.likes.add(request.user.id)
                post.save()
                return Response(GetPostSerializer(post).data, status=status.HTTP_200_OK)
        except:
            return Response({'error': "No post found"}, status=status.HTTP_404_NOT_FOUND)


class CommentView(APIView):
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        comment_id = kwargs.get('c_id')

        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            post = Post.objects.filter(id=post_id).first()
            if post:
                serializer.save(user=request.user, post=post)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': "No post found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        comment_id = kwargs.get('id')
        try:
            comment = Comment.objects.get(id=comment_id)
            if comment.user.id == request.user.id:
                comment.delete()
                return Response({'msg': "Comment Deleted"}, status=status.HTTP_200_OK)
            else:
                return Response({'error': "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        except ObjectDoesNotExist:
            return Response({'error': "No comment found"}, status=status.HTTP_404_NOT_FOUND)

