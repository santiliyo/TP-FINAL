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
from django.contrib import admin
from django.conf import settings
from Blog import views
from .views import Vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name="inicio"),
    path('categorias/', views.categorias, name="Categorias"),
    path('busqueda/', views.busqueda, name="Busqueda"),
    path('busqueda_post', views.busqueda_post, name='Busqueda_post'),
    #path('resultadosbusqueda_post', views.resultados_busqueda, name='Resultadosbusqueda_post'),
    #path(r'^(?P<pk>\d+)$', Buscar.as_view(), name="Buscar"),
    path('python/', views.python, name="Python"),
    path('django/', views.django, name="Django"),
    path('html/', views.html, name="HTML"),
    path('windows/', views.windows, name="Windows"),
    path('linux/', views.linux, name="Linux"),
    path('contacto/', views.contacto, name="Contacto"),
    path('vista_usuario', Vista.as_view(), name='Vista'),
    path('nueva_categoria', views.nueva_categoria, name='Nueva_categoria'),
    path('carga_usuario', views.carga, name='Carga'),
    path('login_usuario', views.login, name='Login'),
    path('registro_usuario', views.registro, name='Registro'),
    path('single-post', views.single_post, name='Single-post'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)