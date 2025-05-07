from rest_framework import viewsets
from .models import BlogPost, Chapter
from .serializers import BlogPostSerializer, ChapterSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
