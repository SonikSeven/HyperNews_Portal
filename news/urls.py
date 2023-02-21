from django.urls import path, re_path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    re_path("^news/?$", views.MainView.as_view(), name="main"),
    path("", RedirectView.as_view(pattern_name="main")),
    re_path(r"^news/(?P<article_number>\d+)/?$", views.ArticleView.as_view()),
    re_path("^news/create/?$", views.AddArticleView.as_view(), name="create_article"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL)
