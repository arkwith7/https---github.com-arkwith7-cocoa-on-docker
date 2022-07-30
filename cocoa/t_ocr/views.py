from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


import os
import shutil

from t_ocr.forms import ImageFileForm
from t_ocr.models import ImageFile

config = dict()
config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Create your views here.
def index(request):
    # print("general_ocr list start...")
    data = dict()
    image_form = ImageFileForm(request.POST or None, request.FILES or None)
    # print("image_form : ",image_form)
    # print("image_form.is_valid():[{}]".format(image_form.is_valid()))
    # print("image_form.ocr_engine:[{}]".format(image_form.ocr_engine))
    if image_form.is_valid():
        # print("general_ocr enroll start...")
        image = image_form.save()
        image.execute_and_save_ocr()
        print("ImageFileModel.id:[{}]".format(image.id))
        print("ImageFileModel.image:[{}]".format(image.image))
        print("ImageFileModel.ocr_engine:[{}]".format(image.ocr_engine))
        # dictionary for initial data with  
        # field names as keys 
        context ={} 
    
        # add the dictionary during initialization 
        context["data"] = ImageFile.objects.get(id = image.id) 
        return render(request, 'template_ml.html', context=context)

    image_list = ImageFile.objects.all().order_by('-id')
    page = request.GET.get('page', 1)

    data['image_form'] = image_form
    # data['image_list'] = image_list

    paginator = Paginator(image_list, 3)
    try:
        data['image_list'] = paginator.page(page)
    except PageNotAnInteger:
        data['image_list'] = paginator.page(1)
    except EmptyPage:
        data['image_list'] = paginator.page(paginator.num_pages)

    return render(request, "template_ocr_list.html", data)

    # if request.method == 'POST':
    #     if 'file' not in request.files:
    #         # flash('No files selected')
    #         return HttpResponseRedirect('/')
    #     try:
    #         shutil.rmtree('./images')
    #     except:
    #         pass
    #     os.mkdir('./images')
    #     files = request.files.getlist("file")
    #     for f in files:
    #         f.save(os.path.join('./images', f.filename))
    #     for (dirpath, dirnames, filenames) in os.walk(config["IMAGES"]):
    #         files = filenames
    #         break
    #     config["FILES"] = files

    #     print("config['IMAGES']",config["IMAGES"])
    #     print("config['FILES']",config["FILES"])

    #     return HttpResponseRedirect('/tagger', code=302)
    # else:
    #     return render(request, 'index.html')

def tagger(request):
    data = dict()
    # print("tagger app.config :",app.config)
    # if (app.config["HEAD"] == len(app.config["FILES"])):
    #     return redirect(url_for('final'))
    # directory = app.config["IMAGES"]
    # image = app.config["FILES"][app.config["HEAD"]]
    # labels = app.config["LABELS"]
    # not_end = not(app.config["HEAD"] == len(app.config["FILES"]) - 1)
    # print(not_end)
    # return render_template('tagger.html', not_end=not_end, directory=directory, image=image, labels=labels, head=app.config["HEAD"] + 1, len=len(app.config["FILES"]))
    return render(request, "tagger.html", data)

def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
