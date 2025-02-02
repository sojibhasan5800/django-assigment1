from django import forms
from .models import catagory_model
class catagory_form(forms.ModelForm):
    class Meta:
        model = catagory_model
        fields = '__all__'