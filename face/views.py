from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages
from django.utils import timezone
from .forms import PostForm
from .bitch import load_encodings, load_names, magic


# home page
def home(request):
    # messages.success(request, f'image chosen successfully')

    # initialize
    submitted = False
    ml_magic = ''
    upload = ''

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            submitted = True
            upload = Post.objects.last()
    else:
        form = PostForm()

    # if user submitted image
    if submitted:
        encodings = load_encodings()
        names = load_names()

        ml_magic = magic(upload.image, encodings, names)

    return render(request, 'face/home.html', {'upload': upload, 'form': form,
                                              'submitted': submitted, 'ml_magic': ml_magic})


# about page
def about(request):
    return render(request, 'face/about.html', {'title': 'About'})
