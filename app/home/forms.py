from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import UploadImage


class UploadImageForm(ModelForm):
    class Meta:
        model = UploadImage
        fields = ['image', 'width', 'height']


    def clean_image(self):
        image = self.cleaned_data['image']
        if image:
            if image._size > 5 * 1024 * 1024:
                raise ValidationError("Image file too large ( > 5mb )")
            return image

        else:
            raise ValidationError("Couldn't read uploaded image")