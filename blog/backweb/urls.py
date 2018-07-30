
from django.urls import path

from backweb import views


urlpatterns = [
    # 登录
    path('login/', views.Login.as_view(), name='login'),
]
