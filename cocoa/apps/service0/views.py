from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ImageFileForm
from .models import ImageFile
from django.core.files.storage import FileSystemStorage

@login_required(login_url="/login/")
def home(request):
    data = dict()

    image_form = ImageFileForm(request.POST or None, request.FILES or None)
    if image_form.is_valid():
        image = image_form.save()
        image.execute_and_save_ocr()
        redirect('home')

    image_list = ImageFile.objects.all().order_by('-id')

    data['image_form'] = image_form
    data['image_list'] = image_list
    data['segment'] = 'ocr'

    return render(request, "service0/index.html", data)

@login_required(login_url="/login/")
def image_upload(request):
    print("OCR....")
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        return render(request, "service0/index.html", {
            "image_url": image_url
        })
    return render(request, "service0/index.html", {"segment": 'ocr'})
