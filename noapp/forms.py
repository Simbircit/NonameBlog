from .models import *
from django import forms


class FeedBackForm(forms.ModelForm):

    class Meta:
        model = FeedBack
        fields = ['name', 'text', 'mail']


class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment
        fields = ['name', 'text']
