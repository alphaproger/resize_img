from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template.loader import get_template

from .models import UploadImage
from .forms import UploadImageForm
# Create your views here.


def resize(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            model = UploadImage(image=request.FILES['image'])
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
