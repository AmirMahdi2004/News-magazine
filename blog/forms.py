from django import forms

from blog.models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['sender', 'email', 'content']


class SearchForm(forms.Form):
    query = forms.CharField()
