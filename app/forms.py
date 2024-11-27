from django import forms
from .models import Blog

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length = 100, 
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Name'
            }
        )
    )
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Email'
            }
        )
    )
    message = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control', 
                'rows': 5,
                'placeholder': 'Type your message ...'
            }
        )
    )

class BlogForm(forms.Form):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'content']
