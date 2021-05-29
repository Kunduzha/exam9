import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

# from api_v2.serializers.article import ArticleSerializer
from article.models import Article
from api_v2.serializers import ArticleSerializer


class ArticleView(APIView):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        response_data = serializer.data
        return Response(data=response_data)

    def post(self, request, *args, **kwargs):
        article_data = request.data
        print(article_data)
        serializer = ArticleSerializer(data=article_data)
        serializer.is_valid(raise_exception=True)
        article = serializer.save()
        return JsonResponse({'id': article.id})

class Article_detail(APIView):
    def get(self, request, *args, **kwargs):
        try:
            article = Article.objects.get(pk=kwargs.get("pk"))
            article_srlz = ArticleSerializer(article)
            response_data = article_srlz.data
            return Response(response_data)
        except Article.DoesNotExist:
            return Response(data={"error": "error"}, status=404)

    def put(self, request, pk, **kwargs):
        try:
            article = Article.objects.get(pk=pk)
            data = request.data
            srlz_update = ArticleSerializer(instance=article, data=data)

            if srlz_update.is_valid(raise_exception=True):
                srlz_update.save()
                return Response(data=srlz_update.data)
        except Article.DoesNotExist:
            return Response(data={"error": "error"}, status=404)


    def delete(self, request, pk, **kwargs):
        try:
            article = Article.objects.get(pk=pk)
            article.delete()
            return Response()
        except Article.DoesNotExist:
            return Response(data={"error": "error"}, status=404)

