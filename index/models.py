from django.db import models
import re
from ckeditor.fields import RichTextField

# Create your models here.

# Remove HTML tags and return clean string text
CLEANR = re.compile('<.*?>') 
def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

class A_Home(models.Model):
    profile_img   = models.ImageField(upload_to='images/', help_text='Make sure the img is: 600x600')
    name          = models.CharField(max_length=20)
    changing_text = models.TextField(max_length=500, help_text='Type like this: Designer, Developer, Freelancer')

    # class Meta:
    #      verbose_name_plural = 'zx'

    def __str__(self):
        return self.name

class A_Links(models.Model):
    name          = models.CharField(max_length=20, help_text='type like this: bx bxl-twitter')
    link          = models.URLField()
    def __str__(self):
        return self.name

class B_About(models.Model):
    about         = RichTextField()
    img           = models.ImageField(upload_to='B_About/')
    text_bold     = models.TextField(max_length=100)
    text_small    = RichTextField()
    birthday      = models.DateField()
    website       = models.URLField()
    phone         = models.IntegerField()
    address       = models.CharField(max_length=100)
    age           = models.IntegerField()
    degree        = models.CharField(max_length=15)
    email         = models.EmailField()
    freelancer    = models.BooleanField()
    botom_text    = RichTextField(blank=True)

    def __str__(self):
        return cleanhtml(self.about)

class C_Skil_text(models.Model):
    text           = RichTextField()
    def __str__(self):
        return cleanhtml(self.text)

class D_Skil(models.Model):
    name           = models.CharField(max_length=20)
    val            = models.IntegerField()
    def __str__(self):
        return self.name

class E_resume_text(models.Model):
    text_resume    = RichTextField(blank=True)
    text_summary   = RichTextField(blank=True)
    def __str__(self):
        return f"{cleanhtml(self.text_resume[0:60])} | {cleanhtml(self.text_summary[0:60])}"

class F_Summary(models.Model):
    text           = RichTextField()
    def __str__(self):
        return cleanhtml(self.text[0:80])

class G_Education(models.Model):
    bold_text1     = models.CharField(max_length=100)
    session1       = models.CharField(max_length=10)
    text1          = RichTextField(blank=True)
    text2          = RichTextField(blank=True)
    def __str__(self):
        return self.bold_text1

class H_Services_text(models.Model):
    text = RichTextField()
    def __str__(self):
        return cleanhtml(self.text[0:80])

class I_Services(models.Model):
    icon           = models.CharField(max_length=50, help_text='Put bootstrap icon like this: bi bi-briefcase-fill')
    sub            = RichTextField(blank=True)
    text           = RichTextField(blank=True)
    def __str__(self):
        return cleanhtml(self.sub)

class J_Portfolio_text(models.Model):
    text           = RichTextField(blank=True)
    def __str__(self):
        return cleanhtml(self.text)

class K_Portfolio(models.Model):
    CHOICES = (
        ('app', 'App'),
        ('card', 'Game'),
        ('web', 'Web'),       
    )
    category       = models.CharField(max_length=5, choices=CHOICES)
    image          = models.ImageField(upload_to='K_Portfolio/', help_text='Make sure the img is: 800x600')
    urlname        = models.CharField(max_length=20)

    def __str__(self):
        return self.urlname

class L_Contact(models.Model):
    text           = models.CharField(max_length=500)
    location       = models.TextField(max_length=500, help_text='Give only the link here like: https://www.google.com/maps/embed?')

class M_message(models.Model):
    name           = models.CharField(max_length=30)
    email          = models.EmailField()
    sub            = models.CharField(max_length=50)
    message        = models.CharField(max_length=500)


