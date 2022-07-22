from django.contrib import admin

# Register your models here.
from tesseract_ocr.models import ImageFile


admin.site.register(ImageFile)