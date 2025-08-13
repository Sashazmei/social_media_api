from django.urls import path
from .views import CreatePostView, MyPostsView, FeedView
from .views import LikeToggleView, PostLikesListView
from .views import CommentListCreateView
urlpatterns = [
    path('create/', CreatePostView.as_view(), name='create-post'),
    path('my/', MyPostsView.as_view(), name='my-posts'),
    path('feed/', FeedView.as_view(), name='feed'),
    path('<int:pk>/like/', LikeToggleView.as_view(), name='like-toggle'),
    path('<int:pk>/likes/', PostLikesListView.as_view(), name='post-likes'),
    path('<int:pk>/comments/', CommentListCreateView.as_view(), name='post-comments'),
]
