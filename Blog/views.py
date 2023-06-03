from django.shortcuts import render
from django.views.generic import TemplateView

#class HomePageView(TemplateView):
#    template_name = 'blog/base.html'

def inicio(request):
    return render(request, "blog/index.html")

def busqueda(request):
    return render(request, "blog/busqueda.html")

def categorias(request):
    return render(request, "blog/categorias.html")  

def python(request):
    return render(request, "blog/python.html")

def contacto(request):
    return render(request, "blog/contacto.html")