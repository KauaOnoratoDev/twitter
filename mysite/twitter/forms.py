from django import forms

from .models import Post, User

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['post_text']
        labels = {
            'post_text': ''
        }
        widgets = {
            'post_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'O que está acontencendo?',
                'rows': 3,
            }),
        }
        