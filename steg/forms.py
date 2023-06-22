from django import forms
from steg.models import Blog, Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = "__all__"
        fields = ['title', 'content', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
