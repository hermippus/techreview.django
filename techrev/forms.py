from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        title = forms.CharField(max_length=50)
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Заголовок'}),
            'content': forms.Textarea(attrs={'placeholder': 'Содержание'}),
        }