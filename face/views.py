from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages
from django.utils import timezone
from .forms import PostForm
from .bitch import load_encodings, load_names, magic, face_accuracy, face_close_match


# home page
def home(request):
    # initialize
    failed = False
    submitted = False
    checked = False

    ml_magic = ''
    upload = ''
    acc = ''

    sim = None
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            submitted = True
            upload = Post.objects.last()
            checked = form.cleaned_data.get('check')
            # messages.success(request, f'image uploaded successfully')
    else:
        form = PostForm()

    # if user submitted image
    if submitted:
        # load encodings and names
        encodings = load_encodings()
        names = load_names()

        # accuracy of image to known images
        acc = face_accuracy(upload.image, encodings, checked)

        # similar image to the one uploaded
        sim = face_close_match(upload.image, encodings, names, checked)

    # if image broke
    if acc == -100 or sim == -100:
        print(acc + " " + sim)
        failed = True
        print('something went wrong')

    return render(request, 'face/home.html', {'upload': upload, 'form': form,
                                              'submitted': submitted, 'ml_magic': ml_magic,
                                              'acc': acc, 'sim': sim, 'checked': checked,
                                              'failed': failed})


# about page
def about(request):
    return render(request, 'face/about.html', {'title': 'about'})
