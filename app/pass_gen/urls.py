from django.urls import path
from . import views

urlpatterns = [
    path('', views.passgen, name="passgen")
]
