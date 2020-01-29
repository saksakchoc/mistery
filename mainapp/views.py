from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .forms import InfoForm
from .models import Info

def index(request):
    return render(request, 'mainapp/index.html')



class InfoView(TemplateView):
    def __init__(self):
        self.params = {
            'form': InfoForm(),
        }
    
    def get(self,request):
        return render(request,'mainapp/uploadinfo.html', self.params)

    def post(self,request):
        person = InfoForm.persondata[int(request.POST['person'])][1]
        stuff = InfoForm.persondata[int(request.POST['stuff'])][1]
        card = request.POST['card']
        content = request.POST['content']
        info = Info(person=person,stuff=stuff,card=card,content=content)
        info.save()
        return redirect(to='/mainapp/uploadinfo')