from django.urls import path
from .views import TareaList

urlpatterns = [
    path('tareas/', TareaList.as_view()),
]