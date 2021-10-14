from django.urls import path
from . import views

app_name = 'enroll'
urlpatterns = [
    path('signup', views.signup_user, name="signup_user"),
    path('login', views.login_user, name="login_user"),
    path('logout', views.user_logout, name="logout"),
    path('passchange', views.passchange, name="passchange"),
    path('profile', views.profile, name="profile"),
    path('profile-edit', views.edit_profile, name="edit_profile")
]
