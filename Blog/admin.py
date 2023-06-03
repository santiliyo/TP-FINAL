from django.contrib import admin
from . import models

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "status", "slug", "author")
    p_fields = {"slug": ("title",),}


@admin.register(models.Comentarios)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "name", "email", "publish", "status")
    list_filter = ("status", "publish")
    search_fields = ("name", "email", "content")


#admin.site.register(models.Post)

#admin.site.register(models.Comentarios)

admin.site.register(models.Category)


