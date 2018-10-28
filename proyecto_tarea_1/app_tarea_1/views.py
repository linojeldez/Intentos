from django.shortcuts import render

# Create your views here.

def informacion(request):
	return render(request,'app_tarea_1/informacion.html')

def carta(request):
	return render(request,'app_tarea_1/carta.html')

def rosti(request):
	return render(request,'app_tarea_1/rosti.html')
