from django.db import models
# from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Chapter(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='chapters')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subchapters')
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} ({'Sub' if self.parent else 'Main'} Chapter)"
