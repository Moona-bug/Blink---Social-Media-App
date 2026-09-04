from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class PostView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post/post_new.html'
    fields = {'content'}
    success_url = 'home'
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)