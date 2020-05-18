from django.shortcuts import render
from .models import Post
from django.contrib import messages


# home page
def home(request):
    # messages.success(request, f'image chosen successfully')

    return render(request, 'face/home.html')


# about page
def about(request):
    return render(request, 'face/about.html', {'title': 'About'})
