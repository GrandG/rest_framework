from django.urls import path, include, re_path

from . import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path(r'snippets/', views.SnippetList.as_view(), name='snippet-list'),
    re_path(r'snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    path(r'users/', views.UserList.as_view(), name='user-list'),
    re_path(r'users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    path(r'api-auth/', include('rest_framework.urls')),
    path(r'', views.api_root),
    re_path(r'snippets/(?P<pk>[0-9]+)/highlighted/$', views.SnippetHighlight.as_view(), name='snippet-highlighted')
]

urlpatterns = format_suffix_patterns(urlpatterns)