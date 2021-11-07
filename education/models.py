from django.db import models
from django.utils.text import slugify
from froala_editor.fields import FroalaField

# Create your models here.

class Subject(models.Model):
    title = models.CharField(max_length=100)
    small_disc = FroalaField()
    image_URL = models.ImageField(upload_to='subjects', help_text='the image should be 600x300')
    disc =FroalaField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Subject, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

class Middle_text(models.Model):
    text = FroalaField()
    def __str__(self):
        return self.text[0:60]

class Gallery(models.Model):
    image = models.CharField(max_length=500, help_text='The image should be 450x300 && put "coppy image address" here.')

    def __str__(self):
        return self.image[0:60]