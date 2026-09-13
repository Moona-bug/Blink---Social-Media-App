from django.urls import path
from .views import (
    PostView,
    CreatePostView,
    PostDetailView,
    LikePostView,
    AddCommentView,
    RepostView,
)

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('new/', CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/like/', LikePostView.as_view(), name='like_post'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('post/<int:pk>/repost/', RepostView.as_view(), name='repost')
]