from django import forms
from django.core.exceptions import ValidationError


class UploadImageForm(forms.Form):

    image = forms.ImageField(
        label='Select a file',
        help_text='max. 5 megabytes'
    )
    width = forms.IntegerField(help_text='required', required=True)
    height = forms.IntegerField(help_text='optional', required=False)


    def clean_image(self):
        image = self.cleaned_data['image']
        if image:
            if image._size > 5 * 1024 * 1024:
                raise ValidationError("Image file too large ( > 5mb )")
            return image
        else:
            raise ValidationError("Couldn't read uploaded image")