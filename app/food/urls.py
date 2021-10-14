from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('', views.index, name="index"),
    path('details/<int:pk>', views.details, name="details"),
    path('add', views.add, name="add"),
    path('edit/<int:pk>', views.edit, name="edit"),
    path('delete/<int:pk>', views.delete, name="delete"),
]
