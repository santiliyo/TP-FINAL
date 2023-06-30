from django.contrib import admin
from usuarios.models import Usuario_avatar

class UsuariosAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('user', 'avatar',)

admin.site.register(Usuario_avatar, UsuariosAdmin)
