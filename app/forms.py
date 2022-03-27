from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('author', 'comment')
		widgets = {
			'author' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Введите имя'}),
			'comment' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Введите текст'})
		}