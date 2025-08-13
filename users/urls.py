from django.urls import path
from .views import RegisterView, MyProfileView, PublicProfileView
from rest_framework.authtoken.views import obtain_auth_token
from .views import FollowToggleView, FollowersListView, FollowingListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('profile/', MyProfileView.as_view(), name='my-profile'),
    path('profile/<str:username>/', PublicProfileView.as_view(), name='public-profile'),
    path('follow/<str:username>/', FollowToggleView.as_view(), name='follow-toggle'),
    path('followers/', FollowersListView.as_view(), name='followers-list'),
    path('following/', FollowingListView.as_view(), name='following-list'),
]
