from django.urls import path, include

from api_v2.views import ArticleView, Article_detail


app_name = 'api_v2'


article_urls = [
    path('', ArticleView.as_view(), name='articles'),
    path('<int:pk>/', Article_detail.as_view()),
    # path('/article/<pk>/', Article_detail.as_view(), name='article')
]


urlpatterns = [
    path('articles/', include(article_urls)),

]