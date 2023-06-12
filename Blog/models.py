from django.db import models
from datetime import datetime, timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.

class Registro_usuario(models.Model):
    usuario=models.CharField(max_length=70, verbose_name="usuario", unique=True)
    clave=models.CharField(max_length=8, verbose_name="clave")
    confirmar_clave=models.CharField(max_length=8, verbose_name="confirmar_clave")
    mail=models.EmailField(max_length=40)
    dni=models.CharField(max_length=8, verbose_name="dni", unique=True)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)

    class Meta:
       verbose_name='Registro'
       verbose_name_plural='Registros'
       ordering = ['usuario']

    def __str__(self):
      return self.usuario

class Categoria(models.Model):
    Nombre=models.CharField(max_length=70, verbose_name="Nombre", unique=True)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)

    class Meta:
       verbose_name='Categoria'
       verbose_name_plural='Categorias'
       ordering = ['Nombre']

    def __str__(self):
      return self.Nombre

class Post(models.Model):
    Titulo=models.CharField(max_length=150, verbose_name="Titulo", unique=True, default="Titulo")
    Post = models.TextField(max_length=8000, verbose_name="Contenido", default="Ingresar Contenido:")
    Imagen=models.ImageField(upload_to="blog", blank=True, null=True, default = None)
    usuario=models.ForeignKey(Registro_usuario, on_delete=models.CASCADE)
    categorias=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)

    class Meta:
       verbose_name='Post'
       verbose_name_plural='Posts'
       ordering = ['update']

    def __str__(self):
      return '%s - %s' % (self.Titulo, self.created)

    def save(self, *args, **kwargs):
        self.url = slugify(self.Titulo)
        super(Post, self).save(*args, **kwargs)

