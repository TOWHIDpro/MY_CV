from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    profile_img = models.ImageField(upload_to='profilepic', blank=True)
    expert_at = models.CharField(max_length=100, blank=True)
    about = models.CharField(max_length=500, blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True)
    phone = models.PositiveIntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "USER PROFILE"

    def __str__(self):
        return self.user.username