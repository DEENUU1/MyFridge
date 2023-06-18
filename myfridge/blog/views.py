from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
    ListView,
    DetailView,
)

from .models import Post, Comment
from django.core.exceptions import PermissionDenied
from typing import Any, Dict


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ("title", "text", "image")
    template_name = "post_create.html"
    success_url = reverse_lazy("users:profile")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ("title", "text", "image")
    template_name = "post_update.html"
    success_url = reverse_lazy("users:profile")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        if not queryset.exists():
            raise PermissionDenied("You are not authorized to edit this Shopping List.")
        return queryset


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("users:profile")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        if not queryset.exists():
            raise PermissionDenied("You are not authorized to edit this Shopping List.")
        return queryset


class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ("text",)
    template_name = "comment_create.html"
    success_url = reverse_lazy("users:profile")

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.kwargs["pk"]
        return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ("text",)
    template_name = "comment_update.html"
    success_url = reverse_lazy("users:profile")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        if not queryset.exists():
            raise PermissionDenied("You are not authorized to edit this Shopping List.")
        return queryset


class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy("users:profile")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        if not queryset.exists():
            raise PermissionDenied("You are not authorized to edit this Shopping List.")
        return queryset
