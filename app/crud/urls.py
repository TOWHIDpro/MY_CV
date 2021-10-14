from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="crud"),
    path('delete', views.delete, name="delet"),
    path('update', views.update_data, name="update_data")
]