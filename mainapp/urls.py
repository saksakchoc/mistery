from django.urls import path
from django.conf.urls import url
from .views import InfoView
from .views import PersonView
from .views import StuffView
from mainapp import views


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^uploadinfo/', InfoView.as_view(), name='uploadinfo'),
    url(r'^addperson/', PersonView.as_view(), name='addperson'),
    url(r'^addstuff/', StuffView.as_view(), name='addstuff')
]