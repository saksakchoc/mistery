from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .forms import InfoForm
from .forms import PersonForm
from .forms import StuffForm
from .models import Info
from .models import Person
from .models import Stuff

def index(request):
    return render(request, 'mainapp/index.html')


# 情報登録画面のView
class InfoView(TemplateView):
    def __init__(self):
        self.params = {
            'form': InfoForm(),
        }
    
    def get(self,request):
        return render(request,'mainapp/uploadinfo.html', self.params)

    def post(self,request):
        person = InfoForm.persondata[int(request.POST['person'])][1]
        stuff = InfoForm.stuffdata[int(request.POST['stuff'])][1]
        card = request.POST['card']
        content = request.POST['content']
        info = Info(person=person,stuff=stuff,card=card,content=content)
        info.save()
        return redirect(to='/mainapp/uploadinfo')
# 登場人物登録画面のView
class PersonView(TemplateView):
    def __init__(self):
        self.params = {
            'form': PersonForm
        }

    def get(self,request):
        return render(request,'mainapp/addperson.html', self.params)

    def post(self,request):
        person = request.POST['person']
        person = Person(person=person)
        person.save()
        return redirect(to='/mainapp/addperson')
# 証拠品登録画面のView
class StuffView(TemplateView):
    def __init__(self):
        self.params = {
            'form': StuffForm
        }

    def get(self,request):
        return render(request,'mainapp/addstuff.html', self.params)

    def post(self,request):
        stuff = request.POST['stuff']
        stuff = Stuff(stuff=stuff)
        stuff.save()
        return redirect(to='/mainapp/addstuff')

class DispView(TemplateView):
    def __init__(self):
        self.params = {
            'title': 'aa',
            'persondata' : Person.objects.all(),
            'stuffdata' : Stuff.objects.all(),
            'infodata' : Info.objects.all()
        }
        
    def get(self,request):
        return render(request,'mainapp/dispinfo.html', self.params)