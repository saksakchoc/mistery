from django.db import models
from django import forms
from .models import Person
from .models import Stuff

class InfoForm(forms.Form):
    person = Person.objects.all()
    persondata = []
    i = 0
    for item in person:
        tp = (i,item.person)
        persondata.append(tp)
        i += 1
    stuff = Stuff.objects.all()
    stuffdata = []
    i = 0
    for item in stuff:
        tp = (i,item.stuff)
        stuffdata.append(tp)
        i += 1
    person = forms.ChoiceField(label='person', choices=persondata)
    stuff = forms.ChoiceField(label='stuff', choices=stuffdata)
    card = forms.CharField(label='card')
    content = forms.CharField(label='content')

class PersonForm(forms.Form):
    person = forms.CharField(label='person')
class StuffForm(forms.Form):
    stuff = forms.CharField(label='stuff')