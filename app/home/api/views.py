from __future__ import absolute_import
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.files import File
from urlparse import urlparse
from io import BytesIO
from urllib2 import urlopen
from urllib2 import HTTPError
import json

from app.home.models import UploadImage
from app.scripts.resizefunc import resize_picture


class ResizeAPI(APIView):
    http_method_names = ['get']

    def get(self, *args, **kwargs):
        model = UploadImage()

        url = u'http://' + kwargs['file']
        width = kwargs['width']
        height = kwargs['height']
        # print('************', url, width, height, '************')
        name = urlparse(url).path.split('/')[-1]
        try:
            response = urlopen(url)
            io = BytesIO(response.read())
        except HTTPError as r:
            return Response("You could't send a request to another site. Traceback: " + str(r))

        model.image.save(name, File(io))

        try:
            # function resizing of picture
            (new_name, height) = resize_picture(name, width, height)
        except BaseException as r:
            return Response('There have been some problems. Traceback: '+str(r))
        finally:
            model.delete()

        model = UploadImage(image=new_name, width=width, height=height)
        model.save()

        # for JSON format you need to use : json.dumps(model.image.url)
        return Response({
            'URL of image': model.image.url
        })
