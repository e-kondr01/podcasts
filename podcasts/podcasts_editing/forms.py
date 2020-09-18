from django import forms 
from .models import *


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['photo']


class AudioForm(forms.ModelForm): 

    class Meta: 
        model = Audio
        fields = ['audio'] 