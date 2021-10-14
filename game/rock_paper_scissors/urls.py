from django.urls import path
from . import views

urlpatterns = [
    path('', views.rock_paper_scissors, name="rock_paper_scissors")
]
