from django.db import models
import re
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

# Remove HTML tags and return clean string text
CLEANR = re.compile('<[^>]*>') 
def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

class Subject(models.Model):
    title = models.CharField(max_length=100)
    small_disc = RichTextField()
    image_URL = models.ImageField(upload_to='subjects', help_text='the image should be 600x300')
    disc = RichTextField()
    site_title = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Subject, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

class Middle_text(models.Model):
    text = RichTextField()
    def __str__(self):
        return cleanhtml(self.text[0:60])

class Gallery(models.Model):
    image = models.CharField(max_length=500, help_text='The image should be 450x300 && put "coppy image address" here.')

    def __str__(self):
        return self.image[0:60]