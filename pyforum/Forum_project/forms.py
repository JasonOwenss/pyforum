from django import forms
from .models import Forum, Comment


class ForumForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class' : 'titleInput','placeholder': 'Post Title'}),label='')
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'contentInput','placeholder': 'Post Content'}),label='')
    class Meta:
        model = Forum
        fields = ['title','content']

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea,label='')
    class Meta:
        model = Comment
        fields = ['content','forum']
        widgets = {'forum':forms.HiddenInput()}
        
    
