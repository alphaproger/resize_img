# -*- coding: utf8 -*-
from django.conf.urls import url
from .views import ResizeAPI


urlpatterns = [
    url(r'^resize_img/(?P<file>.+)/(?P<width>\d+)/(?P<height>\d*)/$', ResizeAPI.as_view()),
    url(r'^resize_img/(?P<file>.+)/(?P<width>\d+)/$', ResizeAPI.as_view(), {'height': ""}),
]