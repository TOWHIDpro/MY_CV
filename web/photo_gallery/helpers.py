from django.utils.text import slugify
from . models import AddImage
import random
import string


def random_string(num):
    letters = string.ascii_lowercase
    return ( ''.join(random.choice(letters) for i in range(num)) )

def generate_slug(text):
    new_slug = slugify(text)
    if AddImage.objects.filter(slug = new_slug).exists():
        return generate_slug(text + '-' + random_string(5))
    return new_slug