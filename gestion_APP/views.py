from django.shortcuts import render, redirect
from . import models, forms
from gestion_APP.models import Reserva
from gestion_APP.forms import FormReserva 

# Create your views here.
def index (request):
    return render(request, 'index.html')

def reservas (request):
    reservas = Reserva.objects.all()
    data = {'reservas': reservas}
    return render(request, 'reservas.html', data)

def agregarreserva(request):
    form = FormReserva()
    if request.method == 'POST':
        form = FormReserva(request.POST)
        if (form.is_valid()):
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'agregar.html', data)

def editarreserva(request, id):  
    reserva = Reserva.objects.get(id=id)
    form = FormReserva(instance=reserva)
    if request.method == "POST":  
        form = FormReserva(request.POST, instance=reserva)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/reservas')  
            except Exception as e: 
                pass    
    return render(request,'agregar.html',{'form':form}) 

def eliminarreserva(request, id):
    reserva = Reserva.objects.get(id = id)
    try:
        reserva.delete()
    except:
        pass
    return redirect('/reservas')

