from django.conf.urls import url
urlpatterns = [
    url(r'^$', 'home.views.resize', name='upload')
]