from django import forms


class UploadImageForm(forms.Form):
    image = forms.ImageField(
        label='Select a file',
        help_text='max. 10 megabytes'
    )