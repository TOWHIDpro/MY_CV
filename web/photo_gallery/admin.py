from django.contrib import admin
from . models import AddImage
# Register your models here.


class AddImageAdmin(admin.ModelAdmin):
    # exclude = ['slug']
    pass
admin.site.register(AddImage, AddImageAdmin)
