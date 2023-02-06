from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mensajeabout(self):
    return HttpResponse('<h1> Calculadora </h1> '
                       + '<h2> Desarrollado por:</h2> <br> <h3>Deiwer Hernán Chaleal</h3> <br><h3>Daniel Estevan Madroñero</h3><br><h3>Brayan Daniel Ceron</h3>')

    
