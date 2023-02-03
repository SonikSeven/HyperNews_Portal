from django.urls import path, re_path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", RedirectView.as_view(url="news/")),
    re_path(r"news/(?P<link>\d+)", views.ArticleView.as_view()),
    re_path("news/create", views.AddArticleView.as_view()),
    re_path("news", views.MainView.as_view()),
]

urlpatterns += static(settings.STATIC_URL)
