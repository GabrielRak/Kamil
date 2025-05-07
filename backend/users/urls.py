from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,RegisterView,LoginView


router = DefaultRouter()

router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
]