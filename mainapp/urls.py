from django.urls import path
from django.conf.urls import url
from .views import PersonView
from .views import StuffView
from .views import DispView
from mainapp import views


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^addperson/', PersonView.as_view(), name='addperson'),
    url(r'^addstuff/', StuffView.as_view(), name='addstuff'),
    url(r'^dispinfo/', DispView.as_view(), name='dispinfo')
]