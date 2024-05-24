from django import forms
from .models import Davlatlar

class DavlatlarForm(forms.ModelForm):
    class Meta:
        model = Davlatlar
        fields = {'name', 'price', 'about', 'image', 'dav'}