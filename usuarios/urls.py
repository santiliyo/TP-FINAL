from django.urls import path, include
from usuarios import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'usuarios'

urlpatterns = [
    #path('Blog/', include('Blog.urls')),
    path('login/', views.login_request, name='Login_usr'),
    path('register/', views.register, name='Register'),
    path('logout/', views.Logout.as_view(), name='Logout'),
    path('perfil/', views.mostrar_perfil, name='Mostrar_perfil'),
    path('perfil/editar/', views.editar_perfil, name='Editar_perfil'),
    path('perfil/eliminar/<int:pk>/', views.EliminarPerfil.as_view(), name='Eliminar_perfil'),
    path('perfil/cambiar-password/', views.CambiarPassword.as_view(), name='Cambiar_password'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)