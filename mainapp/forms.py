from django import forms

class InfoForm(forms.Form):
    persondata = [
        ('0','幸子'),
        ('1','山田'),
        ('2','上田'),
    ]
    stuffdata = [
        ('0','指紋'),
        ('1','血痕'),
        ('2','凶器'),
    ]
    person = forms.ChoiceField(label='person', choices=persondata)
    stuff = forms.ChoiceField(label='stuff', choices=stuffdata)
    card = forms.CharField(label='card')
    content = forms.CharField(label='content')