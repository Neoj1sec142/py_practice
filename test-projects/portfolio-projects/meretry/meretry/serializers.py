from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import User, Post, Comment

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['id','email','first_name','last_name','username','password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'text', 'name', 'date', 'likes', 'post_comments']
        read_only_fields = ('post_comments',)


class CommentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'text', 'date', 'name']


class GetPostSerializer(serializers.ModelSerializer):
    post_comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'text', 'name', 'date', 'likes', 'post_comments']