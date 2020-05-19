from django.shortcuts import render
from .models import Post
from django.contrib import messages
from django.utils import timezone


# home page
def home(request):
    # messages.success(request, f'image chosen successfully')

    image = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'face/home.html', {'image': image})


# about page
def about(request):
    return render(request, 'face/about.html', {'title': 'About'})
