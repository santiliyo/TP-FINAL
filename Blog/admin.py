from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from Blog.models import Categoria, Post

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
        form = super(PostAdmin, self).get_form(request, obj, **kwargs)
        return form

admin.site.register(Post, PostAdmin)

