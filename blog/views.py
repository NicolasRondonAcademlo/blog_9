from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from blog.models import Article
from blog.permissions import IsOwnerOrReadOnly
from blog.serializers import ArticleSerializer
from rest_framework.decorators import  action


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,]
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=False)
    def published_articles(self, request, *args, **kwargs):
        articles = Article.objects.filter(is_published=True)
        serializer = self.get_serializer_class()
        serializer = serializer(articles, many=True)
        return  Response(serializer.data, status=200)