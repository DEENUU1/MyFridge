from django.db import models
from users.models import CustomUser
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to="images", default=None, blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f"{self.author} {self.post}"
