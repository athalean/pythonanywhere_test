from django import forms
from panywhere.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment