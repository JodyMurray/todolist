from django.urls import path
from .views import TaskList
from base import views


urlpatterns = [
    path('', views.TaskList.as_view(), name='tasks'),
]