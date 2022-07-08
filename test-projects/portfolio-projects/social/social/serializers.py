from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import User, Profile, Post, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email','date','password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        Token.objects.create(user=user)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class GetProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = [
            'id','user','website','location',
            'status', 'bio',
            'youtube', 'twitter', 'facebook', 'linkedin',
            'instagram', 'experience', 'education'
        ]

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','user','text','name','date','likes','post_comments']
        read_only_fields = ('post_comments',)

class CommentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name',read_only=True)
    
    
    class Meta:
        model = Comment
        fields = ['id','user','post','text','date','name']
        
class GetPostSerializer(serializers.ModelSerializer):
    post_comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = ['id','user','text','name','date','likes','post_comments']