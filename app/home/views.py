from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from PIL import Image
import hashlib

from app.settings import BASE_DIR
from .models import UploadImage
from .forms import UploadImageForm
# Create your views here.


def resize_picture(file, width, height=None):
    file = str(file)

    name = file.split('.')[0]
    extension = file.split('.')[-1]
    path = BASE_DIR + '/media/' + file
    md5_hash = hashlib.md5(name)

    # open file
    pct = Image.open(path)

    # set sizes
    width = int(width)
    if not height:
        height = pct.size[1] * width / pct.size[0]
    else:
        height = int(height)
    size = (width, height)

    new_name = '{0}_{1}x{2}.{3}'.format(md5_hash.hexdigest(), width, height, extension)

    # resize image and save
    new_pct = pct.resize(size, Image.LANCZOS)
    new_pct.save(BASE_DIR + '/media/' + new_name)

    return new_name, height


def resize(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():

            file_name = request.FILES['image']
            width = request.POST['width']
            height = request.POST['height']

            model = UploadImage(image=file_name)
            model.save()

            try:
                # function resizing of picture
                (new_name, height) = resize_picture(file_name, width, height)
            except BaseException as r:
                return HttpResponse('Incorrect height or width.<br><br><b>Traceback: '+str(r))
            finally:
                model.delete()

            model = UploadImage(image=new_name, width=width, height=height)
            model.save()

            return HttpResponseRedirect(reverse('home.views.resize'))
    else:
        form = UploadImageForm()

    images = UploadImage.objects.all()

    return render_to_response(
        'home/base.html',
        {'documents': images, 'form': form},
        context_instance=RequestContext(request)
    )
