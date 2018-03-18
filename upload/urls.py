from . import views
from django.urls import path


urlpatterns = [
    path('', views.MyTemplateView.as_view(), name='upload'), 
]