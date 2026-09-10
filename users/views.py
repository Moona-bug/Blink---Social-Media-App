from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm, ProfileUpdateForm
from .models import CustomUser

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class ProfileView(DetailView):
    model = CustomUser
    template_name = 'users/profile.html'
    context_object_name = 'profile_user'

class ProfileUpdateView( LoginRequiredMixin,UpdateView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = 'users/profile_edit.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user