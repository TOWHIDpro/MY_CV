from django.urls import path
from . import views

app_name = 'education'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:slug>', views.details, name="details")
]
