from django import forms
from django.db.models import fields
from .models import Post


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post    
        fields = ('title', 'body', 'status', 'image', 'image_caption',)
