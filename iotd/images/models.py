from django.db import models
from django.urls import reverse

# Create your models here.
class FeaturedImage(models.Model):

    name = models.CharField(max_length=200)
    tagline = models.TextField()
    uploaded = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to="") 


class Image(models.Model):
    title = models.CharField(max_length=255)
    file = models.ImageField(upload_to='images/')

    def get_absolute_url(self):
        return reverse('image_detail', kwargs={'pk': self.pk})