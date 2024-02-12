from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *

# Create your views here.
# returning a string using function based view
def fun_view(request):
    return HttpResponse('<center><h1>fun_view is done</h1></center>')

#returning a string using class based view
class cls_view(View):
    def get(self,request):
        return HttpResponse('<center><h1>class_view is done</h1></center>')
    


#rendering a function based html file
def fbv_view(request):
        return render(request,'fbv_view.html')
#rendering a class based html file
class cbv_view(View):
     def get(self,request):
          return render(request,'cbv_view.html')
     


# Insertion of data by using Function based views
def insertion_fbv(request):
    SFO=School_Form()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=School_Form(request.POST)
        if SFDO.is_valid():
            SFDO.save()
        return HttpResponse('Insertion is done')              
         
    return render(request,'insertion_fbv.html',d)


class insert_school_by_cbv(View):
     def get(self,request):
          ESFO=School_Form()
          d={'ESFO':ESFO}
          return render(request,'insert_school_by_cbv.html',d)
     def post(self,request):
          SCFO=School_Form(request.POST)
          if SCFO.is_valid():
                SCFO.save()
          return HttpResponse('insertion is done')
     
class cbv_view(TemplateView):
     template_name='cbv_view.html'
          