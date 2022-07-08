from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey('User',on_delete=models.CASCADE, blank=True, related_name='posts')
    text = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True)
    likes = models.ManyToManyField('User', related_name="likes" , blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('-date',)


class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user_comments", blank=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name="post_comments", blank=True)
    text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text}-{self.user.name}"

    class Meta:
        ordering = ('-date',)