from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from app.scripts.resizefunc import resize_picture
from .models import UploadImage
from .forms import UploadImageForm


def example_of_api(request):
    return render_to_response('home/example_of_api.html')


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

            return HttpResponseRedirect(reverse('app.home.views.resize'))
    else:
        form = UploadImageForm()

    images = UploadImage.objects.all()

    return render_to_response(
        'home/index.html',
        {'documents': images, 'form': form},
        context_instance=RequestContext(request)
    )