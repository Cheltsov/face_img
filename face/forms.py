from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('img_1', 'img_2')
