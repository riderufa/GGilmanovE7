from django.db import models
from django.utils.text import slugify
from time import time

def gen_slug(title):
    slug = slugify(title, allow_unicode=True)
    return slug + '-' + str(int(time()))

# Create your models here.
class Comment(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    date_com = models.DateTimeField(auto_now_add=True)
    advert = models.ForeignKey('Advert', on_delete=models.CASCADE, null=True, blank=True, related_name='comments')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Advert(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True)
    date_adv = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='adverts')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

