from django import forms
from app.models import *

class School_Form(forms.ModelForm):
    class Meta:
        model=School
        fields='__all__'