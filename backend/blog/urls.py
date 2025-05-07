from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, ChapterViewSet

router = DefaultRouter()
router.register(r'posts', BlogPostViewSet)
router.register(r'chapters', ChapterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
