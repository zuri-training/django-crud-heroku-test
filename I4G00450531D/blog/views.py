from .models import Post
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView , UpdateView , DeleteView , DetailView

# Create your views here.

class PostListView (ListView):
    model= Post

class PostCreateView (CreateView):
    model = Post
    # all fields in model should be shown
    fields = "__all__"
    # specify blog:all which is app name and what it redirects to because app name was given in urls and app name is a good convention as it helps in a case where they are so many apps.
    success_url = reverse_lazy('blog:all')


class PostDetailView(DetailView):
    model = Post


class PostUpdateView (UpdateView):
    model = Post
    fields =  "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView (DeleteView):
    model = Post
    fields =  "__all__"
    success_url = reverse_lazy("blog:all")