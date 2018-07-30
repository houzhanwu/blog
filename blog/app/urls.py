
from django.urls import path

from app import views


urlpatterns = [
    path('index/', views.Index.as_view(), name='index'),
]
