from django.shortcuts import render
from .models import Post
from .forms import PostForm
from .bitch import load_encodings, load_names, face_accuracy, face_close_match


# home page
def home(request):
    # initialize
    failed = False
    submitted = False
    checked = False

    ml_magic = ''
    upload = ''
    acc = ''
    source = ''

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
        source = face_close_match(upload.image, encodings, names, checked)
        sim = source + '/' + source + '_face-1.jpg'

        source = source.replace('_', ' ')

    # if image broke
    if acc == -100 or sim == -100:
        failed = True
        print('something went wrong')

    return render(request, 'face/home.html', {'upload': upload, 'form': form,
                                              'submitted': submitted, 'ml_magic': ml_magic,
                                              'acc': acc, 'sim': sim, 'checked': checked,
                                              'failed': failed, 'source': source})


# about page
def about(request):
    return render(request, 'face/about.html', {'title': 'about'})
