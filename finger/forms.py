from django import forms
from .models import Fphoto

class FphotoForm(forms.ModelForm):

    class Meta:
        model = Fphoto
        fields = ('img_1', 'img_2')
