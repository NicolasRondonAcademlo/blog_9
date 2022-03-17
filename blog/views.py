from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from blog.models import Article
from blog.permissions import IsOwnerOrReadOnly
from blog.serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,]