from django import forms
from admin_app.models import *


class RoomModelForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['title', 'image', 'type']


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


class BookApplicationForm(forms.ModelForm):
    class Meta:
        model = BookApplication
        fields = ['number_persons', 'services', 'start_book', 'end_book']
        widgets = {
            'start_book': forms.DateInput(attrs={'type': 'date'}),
            'end_book': forms.DateInput(attrs={'type': 'date'})
        }
