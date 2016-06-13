from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import UploadImage
from django.forms.utils import ErrorList


class UploadImageForm(ModelForm):
    class Meta:
        model = UploadImage
        fields = ['image', 'width', 'height']

    def __init__(self, *args, **kwargs):
        super(UploadImageForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs = {
            'class': "btn btn-default"
        }
        self.fields['width'].widget.attrs = {
            'class': "form-control", "placeholder": "required, min = 1"
        }
        self.fields['height'].widget.attrs = {
            'class': "form-control", "placeholder": "optional, min = 1"
        }

    def clean_image(self):
        image = self.cleaned_data['image']
        if image:
            if image._size > 5 * 1024 * 1024:
                raise ValidationError("Image file too large ( > 5mb )")
            return image

        else:
            raise ValidationError("Couldn't read uploaded image")
