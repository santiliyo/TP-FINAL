from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from .forms import BlogForm, Buscar_post_Form, CategoriaForm
from .models import Categoria, Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseForbidden, HttpResponse



def inicio(request):
    return render(request, "blog/index.html")

#Para buscar POSTEO por palabra 
def busqueda_post(request):
    if request.method == "POST":
        form = Buscar_post_Form(request.POST) 
        if form.is_valid():
            informacion = form.cleaned_data
            posts = Post.objects.filter(Titulo__icontains=informacion["Post"])
            return render(request, "blog/resultadosbusqueda_post.html", {"posts": posts})
    else:
        form = Buscar_post_Form()
    return render(request, "blog/busqueda_post.html", {"form": form})


def categorias(request):
    return render(request, "blog/categorias.html")  

def python(request):
    return render(request, "blog/python.html")

def django(request):
    return render(request, "blog/django.html")

def windows(request):
    return render(request, "blog/windows.html")

def linux(request):
    return render(request, "blog/linux.html")

def contacto(request):
    return render(request, "blog/contacto.html")

def login(request):
    return render(request, "blog/login.html")

def resultados_busqueda(request):
    return render(request, "blog/resultadosbusqueda_post.html")

def single_post(request):
    return render(request, "blog/single-post.html")


#Para agregar POSTEO
@login_required
def carga(request):
    if request.method=="POST":
        formu=BlogForm(request.POST, request.FILES)
        if formu.is_valid():
            post = formu.save(commit=False)
            post.usuario = request.user
            post.save()
            formu.save()
            return render(request, "blog/vista_usuarios.html")
    else:
        formu=BlogForm()
    return render(request, "blog/carga_usuarios.html", {'form':formu})

#Para agregar categoria
def nueva_categoria(request):
    formcat=Categoria.objects.all()
    username = request.user.username
    if username != "papa" and username != "root":
        #return HttpResponse("Acceso denegado")
        return render(request, "Blog/nueva_categoria.html", {"mensaje":"No tiene permisos para ingresar una nueva categoria"})
    if request.method=="POST":
        formcat=CategoriaForm(request.POST)
        if formcat.is_valid():
            formcat.save()
            return render(request, "blog/nueva_categoria.html")
    else:
        formcat=CategoriaForm()
    return render(request, "blog/nueva_categoria.html", {'formcat':formcat})

#Para ver POSTEO
class Vista(ListView):
    model = Post
    template_name = 'blog/vista_usuarios.html'
    ordering = ['-created']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Posteos'
        return context
    
class ListadoPosteo(ListView):
    model = Post
    template_name = 'Blog/listar_posteo.html'
    ordering = ['-created']

class Posteos_admin(ListView):
    model = Post
    template_name = 'blog/index.html'
    #ordering = ['-created']
    
#Para editar Posteo
@method_decorator(login_required, name='dispatch')
class EditarPosteo(UpdateView):
    model = Post
    template_name = 'Blog/editar_posteo.html'
    fields = ["Titulo", "Post", "Imagen", "categorias",]
    success_url = reverse_lazy('Posteos')

    def get(self, request, *args, **kwargs):
       self.object = self.get_object()

       # Verificar si el usuario autenticado es el autor del posteo
       if self.object.usuario != self.request.user:
           # Si el usuario no es el autor
           return HttpResponseForbidden("No tienes permiso para editar este posteo.")

       return super().get(request, *args, **kwargs)

#Eliminar Posteo
@method_decorator(login_required, name='dispatch')
class EliminarPosteo(DeleteView):
    model = Post
    template_name = 'Blog/eliminar_posteo.html'
    success_url = reverse_lazy('Posteos')

    def get(self, request, *args, **kwargs):
       self.object = self.get_object()

       # Verificar si el usuario autenticado es el autor del posteo
       if self.object.usuario != self.request.user:
           # Si el usuario no es el autor
           return HttpResponseForbidden("NO TIENES PERMISO PARA ELIMINAR ESTE POSTEO.")

       return super().get(request, *args, **kwargs)

#Mostrar Posteo
class MostrarPosteo(DetailView):  
    model = Post
    template_name = 'Blog/mostrar_posteo.html'

