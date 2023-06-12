from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import BlogForm, RegistroForm, LoginForm, Buscar_usr_Form, Buscar_post_Form, CategoriaForm
from .models import Categoria, Post, Registro_usuario


#class HomePageView(TemplateView):
#    template_name = 'blog/base.html'

def inicio(request):
    return render(request, "blog/index.html")

def busqueda(request):
    if request.method == "POST":
        miFormulario = Buscar_usr_Form(request.POST) 

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            usuarios = Registro_usuario.objects.filter(mail__icontains=informacion["usuario"])

            return render(request, "blog/resultadosbusqueda.html", {"usuarios": usuarios})
    else:
        miFormulario = Buscar_usr_Form()

    return render(request, "blog/busqueda.html", {"miFormulario": miFormulario})

def busqueda_post(request):
    if request.method == "POST":
        form = Buscar_post_Form(request.POST) 

        if form.is_valid():
            informacion = form.cleaned_data
            
            posts = Post.objects.filter(Post__icontains=informacion["Titulo"])

            return render(request, "blog/resultadosbusqueda_post.html", {"posts": posts})
    else:
        form = Buscar_post_Form()

    return render(request, "blog/busqueda_post.html", {"form": form})


'''
def buscar(request):
    busqueda=request.GET.get("buscar")
    usuarios=Post.objects.all()
    if busqueda:
        usuarios=Post.objects.filter(
                Q(Titulo__icontains=busqueda) |
                Q(Post__icontains=busqueda) |
                Q(usuario__icontains=busqueda) |
                Q(categorias__icontains=busqueda) 
        ).distinct()
        #return render(request, "blog/resultadosbusqueda.html", {"blog":blog, "usuario":usuario})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)
'''


def categorias(request):
    return render(request, "blog/categorias.html")  

def python(request):
    return render(request, "blog/python.html")

def django(request):
    return render(request, "blog/django.html")

def html(request):
    return render(request, "blog/html.html")

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

#Login de usuarios
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            password = form.cleaned_data['password']
            user = authenticate(request, usuario=usuario, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, '¡Inicio de sesión exitoso!')
                return redirect('blog/index.html')  
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})


#Registro de usuarios
def registro(request):
    #form=Registro_usuario.objects.all()
    if request.method=="POST":
        form=RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            form.save()
            messages.success(request, f'Usuario {usuario} registrado con exito')
        return render(request, "blog/carga_usuarios.html")
    else:
        form=RegistroForm()
    return render(request, "blog/registro.html", {'form':form})


#Para agregar POSTEO
def carga(request):
    formu=Post.objects.all()
    if request.method=="POST":
        formu=BlogForm(request.POST, request.FILES)
        if formu.is_valid():
            formu.save()
            return render(request, "blog/vista_usuarios.html")
    else:
        formu=BlogForm()
    return render(request, "blog/carga_usuarios.html", {'form':formu})

#Para agregar categoria
def nueva_categoria(request):
    formcat=Categoria.objects.all()
    if request.method=="POST":
        formcat=CategoriaForm(request.POST)
        if formcat.is_valid():
            formcat.save()
            return render(request, "blog/carga_usuarios.html")
    else:
        formcat=CategoriaForm()
    return render(request, "blog/nueva_categoria.html", {'formcat':formcat})

#Para ver POSTEO
class Vista(ListView):
    model = Post
    template_name = 'blog/vista_usuarios.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Posteos'
        return context