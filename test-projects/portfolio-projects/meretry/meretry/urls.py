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
    # Post/Comment Paths
    path('posts', views.PostView.as_view()),
    path('posts/<int:id>', views.PostView.as_view()),
    path('posts/<int:id>/like', views.LikeUnlikeView.as_view()),
    path('posts/<int:id>/comments', views.CommentView.as_view()),
    path('posts/comments/<int:id>', views.CommentView.as_view()),
]
