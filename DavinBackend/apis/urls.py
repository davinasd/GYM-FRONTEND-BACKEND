
from django.urls import path
from .views import (
    UserListApiView,
    UserDetailApiView
)

urlpatterns = [
    path('api/', UserListApiView.as_view()),
    path('api/<name>/', UserDetailApiView.as_view()),
]