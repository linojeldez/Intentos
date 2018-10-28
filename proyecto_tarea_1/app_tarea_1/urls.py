from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	# formato: dirección_pag, función_asociada , name=nombre
    	path('',views.informacion, name='informacion'),
        path('carta/',views.carta, name='carta'),
        path('rosti/',views.rosti, name='rosti'),
]
