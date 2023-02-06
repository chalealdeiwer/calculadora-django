from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mensajeabout(req):
    return HttpResponse(req,'<h1> Calculadora </h1> ')