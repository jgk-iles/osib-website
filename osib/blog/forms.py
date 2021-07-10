from django.forms import ModelForm, TextInput
from django.db.models import fields
from .models import Post


class CreatePostForm(ModelForm):

    class Meta:
        model = Post    
        fields = ('title', 'body', 'status', 'image', 'image_caption',)
        widgets = {
            'image_caption': TextInput(attrs={'placeholder': '[Optional] Add image caption'})
        }
