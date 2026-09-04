from django.urls import path
from .views import (
    PostView,
    CreatePostView,
)

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('new/', CreatePostView.as_view(), name='post_new'),
    
]