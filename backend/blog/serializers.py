from rest_framework import serializers
from .models import BlogPost, Chapter

class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class ChapterSerializer(serializers.ModelSerializer):
    subchapters = RecursiveField(many=True, read_only=True)

    class Meta:
        model = Chapter
        fields = ['id', 'title', 'content', 'order', 'subchapters']

class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    chapters = ChapterSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'author', 'created_at', 'chapters']
