from django.contrib.auth import get_user_model 
from rest_framework import viewsets #new
from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.

class PostViewSet(viewsets.ModelViewSet): #new
    permission_classes=(IsAuthorOrReadOnly,)
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class UserViewSet(viewsets.ModelViewSet): #new
    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer
