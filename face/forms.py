from django import forms
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'image', 'check')
        labels = {'title': 'name', 'image': 'image', 'check': 'check'}





