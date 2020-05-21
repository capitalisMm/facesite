from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages
from django.utils import timezone
from .forms import PostForm


# home page
def home(request):
    # messages.success(request, f'image chosen successfully')
    submitted = False
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            submitted = True
    else:
        form = PostForm()

    upload = Post.objects.last()
    return render(request, 'face/home.html', {'upload': upload, 'form': form, 'submitted': submitted})


# about page
def about(request):
    return render(request, 'face/about.html', {'title': 'About'})
