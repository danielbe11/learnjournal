from django import forms
from .models import Resource


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = [
            'name_text',
            'link',
            'language',
            'framework',
            'notes'
        ]