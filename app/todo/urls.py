from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name="todo"),
    path('details/<int:id_number>', views.details, name="details"),
]
