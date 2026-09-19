from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View

from .models import Post, Like, Repost
from .forms import CommentForm

# Create your views here.
class PostView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
    
            if self.request.user.is_authenticated:
                liked_posts = Like.objects.filter(
                    user=self.request.user
                ).values_list('post_id', flat=True)
    
                reposted_posts = Repost.objects.filter(
                    user=self.request.user
                ).values_list('post_id', flat=True)
    
                context['liked_posts'] = liked_posts
                context['reposted_posts'] = reposted_posts
    
            else:
                context['liked_posts'] = []
                context['reposted_posts'] = []
    
            return context

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post/post_new.html'
    fields = {'content', 'image', 'video'}
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            liked_posts = Like.objects.filter(
                user=self.request.user
            ).values_list('post_id', flat=True)

            reposted_posts = Repost.objects.filter(
                user=self.request.user
            ).values_list('post_id', flat=True)

            context['liked_posts'] = liked_posts
            context['reposted_posts'] = reposted_posts

        else:
            context['liked_posts'] = []
            context['reposted_posts'] = []

        return context

class LikePostView(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        like, created = Like.objects.get_or_create(
            post=post,
            user=request.user
        )

        if not created:
            like.delete()

        return redirect(request.META.get('HTTP_REFERER', 'home'))

class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)

            comment.post = post
            comment.author = request.user

            comment.save()

        return redirect('post_detail', pk=post.pk)

class RepostView(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        repost, created = Repost.objects.get_or_create(
            post = post,
            user=request.user
        )

        if not created:
            repost.delete()

        return redirect(
            request.META.get('HTTP_REFERER', 'home')
        )