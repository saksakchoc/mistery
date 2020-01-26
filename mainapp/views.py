from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import InfoForm

def index(request):
    return render(request, 'mainapp/index.html')



class InfoView(TemplateView):
    def __init__(self):
        self.params = {
            'title':'Hello',
            'form': InfoView(),
            'result': 'None',
        }
    
    def get(self,request):
        return render(request,'mainapp/uploadinfo.html', self.params)

    def post(self,request):
        #データを保存する処理を追加する
        return render(request, 'mainapp/uploadinfo.html',self.params)