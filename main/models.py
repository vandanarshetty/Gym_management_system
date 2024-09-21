from django.db import models
from django.utils.html import mark_safe 


class Banners(models.Model):
    img = models.ImageField(upload_to="banners/")
    alt_text = models.CharField(max_length=150)
    def __str__(self):
        return self.alt_text
    def image_tag(self):
        return mark_safe('<img src="%s" width="80"/>'% (self.img.url))

# Create your models here.
class Service(models.Model):   
    title = models.CharField(max_length=150)
    detail = models.TextField()
    img = models.ImageField(upload_to="banners/")
    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="%s" width="80"/>'% (self.img.url))

