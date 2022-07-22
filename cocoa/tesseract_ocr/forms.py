from django import forms
from tesseract_ocr.models import ImageFile
# , BusinessRegistrationImageFile


class ImageFileForm(forms.ModelForm):
    class Meta:
        model = ImageFile
        fields = ('image', )

# class BusinessRegistrationImageFileForm(forms.ModelForm):
#     class Meta:
#         model = BusinessRegistrationImageFile
#         fields = ('image', )
