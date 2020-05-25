from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    check = forms.BooleanField(required=False)

    class Meta:
        model = Post
        fields = ('title', 'image', 'check')




