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
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from Blog import views
from .views import Vista, ListadoPosteo, EditarPosteo, EliminarPosteo, MostrarPosteo, Posteos_admin

app_name = 'Blog'

urlpatterns = [
    path('usuarios/', include('usuarios.urls')),
    path('admin/', admin.site.urls),
    path('', Posteos_admin.as_view(), name="inicio"),
    path('categorias/', views.categorias, name="Categorias"),
    path('busqueda_post', views.busqueda_post, name='Busqueda_post'),
    path('python/', views.python, name="Python"),
    path('django/', views.django, name="Django"),
    path('windows/', views.windows, name="Windows"),
    path('linux/', views.linux, name="Linux"),
    path('contacto/', views.contacto, name="Contacto"),
    path('vista_usuario', Vista.as_view(), name='Vista'),
    path('nueva_categoria', views.nueva_categoria, name='Nueva_categoria'),
    path('carga_usuario', views.carga, name='Carga'),
    path('single-post', views.single_post, name='Single-post'),
    path('posteos/', ListadoPosteo.as_view(), name='Posteos'),
    path('editar-posteo/<int:pk>/', EditarPosteo.as_view(), name='Editar_posteo'),
    path('eliminar-posteo/<int:pk>/', EliminarPosteo.as_view(), name='Eliminar_posteo'),
    path('mostrar-posteo/<int:pk>/', MostrarPosteo.as_view(), name='Mostrar_posteo'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)