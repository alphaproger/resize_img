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
    path = BASE_DIR + file
    width = int(width)
    pct = Image.open(path)
    if not height:
        height = pct.size[1] * width / pct.size[0]
    else:
        height = int(height)
    size = (width, height)

    md5_hash = hashlib.md5()
    md5_hash.update(file.split('/')[-1])
    new_path = '{0}_{1}x{2}.{3}'.format(
        BASE_DIR + "/".join(file.split('/')[:-1]+[md5_hash.hexdigest()]),
        width,
        height,
        file.split('.')[-1])
    new_pct = pct.resize(size, Image.LANCZOS)
    new_pct.save(new_path)
    return new_pct


def resize(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            model = UploadImage(image=request.FILES['image'])
            model.save()

            file_name = model.image.url
            width = request.POST['width']
            height = request.POST.get('height')
            new_url = resize_picture(file_name, width, height)
            return HttpResponseRedirect(reverse('home.views.resize'))
    else:
        form = UploadImageForm()

    images = UploadImage.objects.all()

    return render_to_response(
        'home/base.html',
        {'documents': images, 'form': form},
        context_instance=RequestContext(request)
    )
