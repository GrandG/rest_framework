from django.urls import path, include, re_path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path(r'snippets/', views.snippet_list),
    re_path(r'snippets/(?P<id>[0-9]+)/', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)