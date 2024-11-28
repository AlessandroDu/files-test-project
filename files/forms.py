from django import forms
from django.forms import ModelForm
from .models import File

class UploadForm(ModelForm):
    file = forms.FileField()
    class Meta:
        model = File
        fields = ['name', 'file']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'filename'})
        }
