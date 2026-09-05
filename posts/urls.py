from django.urls import path
from .views import (
    PostView,
    CreatePostView,
    PostDetailView,
)

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('new/', CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]