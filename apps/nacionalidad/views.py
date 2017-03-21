from django.shortcuts import render,redirect
from django.http import  HttpResponse
from apps.nacionalidad.forms import NacionalidadForm
from django.views.generic import ListView, CreateView
from apps.nacionalidad.models import Nacionalidad
# Create your views here.

def index(request):
    #return HttpResponse("LLego hasta el index")
    return render(request,'nacionalidad/index.html')


def nacionalidad_view(request):
    if request.method == 'POST':
        form = NacionalidadForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('nacionalidad:index')
    else:
        form = NacionalidadForm()
    return render(request, 'nacionalidad/nacionalidad_form.html',{'form':form})



class NacionalidadCreate(CreateView):
    model = Nacionalidad
    template_name = 'nacionalidad/nacionalidad_form.html'
