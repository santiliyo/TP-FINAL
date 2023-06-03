"""
URL configuration for Clases_Coder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from Blog import views

urlpatterns = [
    path('blog/', views.inicio, name="inicio"),
    path('categorias/', views.categorias, name="Categorias"),
    path('busqueda/', views.busqueda, name="Busqueda"),
    path('python/', views.python, name="Python"),
    #path('cursos/', views.cursos, name="Cursos"),
    path('contacto/', views.contacto, name="Contacto")
]