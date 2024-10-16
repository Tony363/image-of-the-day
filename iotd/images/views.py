# from django.shortcuts import render_to_response
import os
from django.shortcuts import render
from images.models import FeaturedImage
from django.conf import settings

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Image
from django.urls import reverse_lazy
def home(request):
    image = FeaturedImage.objects.latest('uploaded') 
    return render(request,'images/home.html',{ 'image' : image})

class ImageListView(ListView):
    model = Image
    template_name = 'images/image_list.html'

class ImageDetailView(DetailView):
    model = Image
    template_name = 'images/image_detail.html'

class ImageCreateView(CreateView):
    model = Image
    template_name = 'images/image_form.html'
    fields = ['title', 'file']

class ImageUpdateView(UpdateView):
    model = Image
    template_name = 'images/image_form.html'
    fields = ['title', 'file']

class ImageDeleteView(DeleteView):
    model = Image
    template_name = 'images/image_confirm_delete.html'
    success_url = reverse_lazy('image_list')