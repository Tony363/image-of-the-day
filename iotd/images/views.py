# from django.shortcuts import render_to_response
from django.shortcuts import render
from images.models import FeaturedImage
from django.conf import settings

def home(request):
    image = FeaturedImage.objects.latest('uploaded') 
    print(settings.STATIC_ROOT)
    return render('images/home.html',
                              { 'image' : image})
