from django.urls import path, include, re_path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path(r'snippets/', views.SnippetList.as_view()),
    re_path(r'snippets/(?P<pk>[0-9]+)/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)