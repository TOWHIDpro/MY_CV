from django.urls import path
from . views import TodoList, TodoDetail

urlpatterns = [
    path('user/<int:pk>', TodoList.as_view()),
    path('<int:pk>', TodoDetail.as_view(), name="todo-details"),
    
]
