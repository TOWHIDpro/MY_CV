from django.contrib import admin
from . models import Subject, Gallery, Middle_text
# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    fields = ('title', 'small_disc', 'image_URL', 'disc')
    

admin.site.register(Gallery)
admin.site.register(Middle_text)
