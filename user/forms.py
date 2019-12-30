from django import forms
from .models import User

class FormUser(forms.ModelForm):
    img = forms.ImageField(required=True)
    CHOICES = [('1', 'Face'), ('2', 'Finger')]
    face_or_finger = forms.ChoiceField(choices=CHOICES, widget=forms.Select(), required=True)
    class Meta:
        model = User
        fields = ('email', )
