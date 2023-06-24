from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
    ListView,
    DetailView,
)

from .models import Post, Comment
from typing import Any, Dict
from django.shortcuts import reverse
from django.contrib import messages
from .forms import DateSortingForm
from django.db.models import Q


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ("title", "text", "image")
    template_name = "post_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user

        user = self.request.user
        user.points += 10
        user.save()
        messages.success(self.request, "Your post has been created! You got 10 points!")
        return super().form_valid(form)

    def get_success_url(self):
        post = get_object_or_404(Post, pk=self.object.pk)
        return reverse("blog:post_detail", kwargs={"pk": post.pk})

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ("title", "text", "image")
    template_name = "post_update.html"
    success_url = reverse_lazy("blog:post_list")

    def get_success_url(self):
        post = get_object_or_404(Post, pk=self.object.pk)
        return reverse("blog:post_detail", kwargs={"pk": post.pk})

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        if not queryset.exists():
            messages.error(
                self.request, "You are not authorized to edit this Shopping List."
            )
        messages.success(self.request, "Your post has been updated!")
        return queryset


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post_list")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        if not queryset.exists():
            messages.error(
                self.request, "You are not authorized to delete this Shopping List."
            )
        messages.success(self.request, "Your post has been deleted!")
        return queryset


class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(text__icontains=query)
            )

        order_by = self.request.GET.get("order_by")
        if order_by:
            if order_by == "1":
                queryset = queryset.order_by("created_date")
            if order_by == "2":
                queryset = queryset.order_by("-created_date")

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order_by"] = DateSortingForm(self.request.GET)
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(post=self.object)
        return context


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ("text",)
    template_name = "comment_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs["post_id"])

        user = self.request.user
        user.points += 1
        user.save()
        messages.success(
            self.request, "Your comment has been created! You got 1 point!"
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.kwargs["post_id"]})


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ("text",)
    template_name = "comment_update.html"
    success_url = reverse_lazy("blog:post_list")

    def get_success_url(self):
        comment = get_object_or_404(Comment, pk=self.object.pk)
        return reverse("blog:post_detail", kwargs={"pk": comment.post.pk})

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        if not queryset.exists():
            messages.error(
                self.request, "You are not authorized to edit this Shopping List."
            )
        messages.success(self.request, "Your comment has been updated!")
        return queryset


class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy("blog:post_list")

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        if not queryset.exists():
            messages.error(
                self.request, "You are not authorized to delete this Shopping List."
            )
        messages.success(self.request, "Your comment has been deleted!")
        return queryset
