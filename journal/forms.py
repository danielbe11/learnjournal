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
            'notes',
            'attachment'
        ]
        # labels = {
        #     'name_text': 'Resource name*',
        #     'link': 'URL*',
        #     'language': 'Programming language',
        #     'framework': 'Framework',
        #     'notes': 'Notes',
        #     'attachment': 'Attachment',
        #     }
        # help_texts = {
        #     'notes': 'Details about the resource'
        # }
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 8, 'cols': 80, 'placeholder': 'Optional'}),
            'name_text': forms.Textarea(attrs={'rows': 2, 'cols': 20}),
            'link': forms.Textarea(attrs={'rows': 1, 'cols': 80}),
        }