from django.contrib import admin
from . models import user_profile
# Register your models here.

@admin.register(user_profile)
class user_profileAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)

