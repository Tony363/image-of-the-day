# from django.shortcuts import render_to_response
import os
from django.shortcuts import render
from images.models import FeaturedImage
from django.conf import settings

def home(request):
    image = FeaturedImage.objects.latest('uploaded') 
    print("WTF",settings.TEMPLATES)
    return render(request,'images/home.html',{ 'image' : image})
