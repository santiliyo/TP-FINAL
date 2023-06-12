from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from Blog.models import Categoria, Post, Registro_usuario
from django.contrib.auth.models import User

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

admin.site.register(Categoria, BlogAdmin)

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    list_display = ('id', 'usuario', 'Titulo', 'Imagen')
    search_fields = ('Titulo', 'usuario')
    list_filter = ('created', 'update')
        
        
    def get_form(self, request, obj=None, **kwargs):
        #self.exclude = ('url', )
        form = super(PostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['usuario'].initial = request.user
        return form

admin.site.register(Post, PostAdmin)

class Registro_usuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('clave', 'confirmar_clave', 'created', 'update')
    list_display = ('id', 'usuario', 'mail', 'dni')

admin.site.register(Registro_usuario, Registro_usuarioAdmin)