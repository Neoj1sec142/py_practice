from . import serializers, views
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # JavaScript Web Tokens
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token-create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),  name='token-refresh'),
    path('blacklist/', views.UserLogout.as_view(), name='token-blacklist'),
    # User Paths
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/create', views.UserCreate.as_view(), name='user_create'),
    path('users/logout', views.UserLogout.as_view(), name='user_logout'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('users/<str:username>', views.UserDetailByUsername.as_view(), name='user_detail_by_username'),
    # path('users/alldetails/', views.UserAllDetailsList.as_view(), name='useralldetails_list'),
    # path('users/alldetails/<int:pk>', views.UserAllDetailsDetail.as_view(), name='useralldetails_detail'),
    # Post/Comment Paths
    path('posts', views.PostView.as_view(), name='post_list'),
    path('posts/<int:id>', views.PostView.as_view(), name='post_detail'),
    path('posts/<int:id>/like', views.LikeUnlikeView.as_view(), name='post_like'),
    path('posts/<int:id>/comments', views.CommentView.as_view(), name='comment_list'),
    path('posts/comments/<int:id>', views.CommentView.as_view(), name='comment_detail'),
]
