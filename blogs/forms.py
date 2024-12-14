from dataclasses import fields
from tkinter import Widget
from django import forms
from . models import Blog,BlogPost


class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['text']
        labels={'text':''}
        widget=forms.TextInput(attrs={'autofocus': True})
        
        
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['post']
        label={'post':''}
        widgets = {'post':forms.Textarea(attrs={'cols':80,'autofocus': True})}
        