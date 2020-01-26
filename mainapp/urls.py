from django.urls import path
from django.conf.urls import url
from .views import InfoView


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^uploadinfo/', InfoView.as_view(), name='uploadinfo')
]