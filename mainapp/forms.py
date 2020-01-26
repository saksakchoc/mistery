from django import forms

class InfoForm(forms.Form):
    persondata = [
        ('0','幸子'),
        ('1','山田'),
        ('2','上田'),
    ]
    person = forms.ChoiceField(label='person', choices=persondata)
    stuff = forms.CharField(label='stuff')
    card = forms.CharField(label='card')
    content = forms.CharField(label='content')