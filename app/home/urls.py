from django.conf.urls import url, include

urlpatterns = [
    url(r'^api/', include('app.home.api.urls')),
    url(r'^example_of_api/', 'app.home.views.example_of_api'),
    url(r'^$', 'app.home.views.resize', name='upload'),
]