from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path(r'snippets/', views.snippet_list),
    re_path(r'snippets/(?P<id>[0-9]+)/', views.snippet_detail),
]