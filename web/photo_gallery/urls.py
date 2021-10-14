from django.urls import path
from . import views

app_name = 'photo_gallery'
urlpatterns = [
    path('', views.gallery, name="photo_gallery"),
    path('post/<slug:slug>', views.details, name="post")
]
