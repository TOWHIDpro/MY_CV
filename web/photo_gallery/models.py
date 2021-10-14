from django.db import models
from froala_editor.fields import FroalaField


# Create your models here.

class AddImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    content = FroalaField()
    slug = models.SlugField(unique=True, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    edited = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwarge):
        from . helpers import generate_slug
        self.slug = generate_slug(self.title)
        super(AddImage, self).save(*args, **kwarge)