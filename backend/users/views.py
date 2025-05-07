from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'status': 'success', 'user': {'username': user.username, 'email': user.email}})
        else:
            return Response({'status': 'failure'}, status=401)

class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)