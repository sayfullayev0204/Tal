from django import forms
from .models import Murojatlar

class MurojatlarForm(forms.ModelForm):
    class Meta:
        model = Murojatlar
        fields = ['name', 'email', 'title', 'message']
