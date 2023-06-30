from django.forms import ModelForm
from django import forms
from Blog.models import Post, Categoria



class CategoriaForm(ModelForm):
    class Meta:
       model = Categoria
       fields = '__all__'


class BlogForm(ModelForm):
    class Meta:
       model = Post
       fields = ['Titulo', 'Post', 'Imagen', 'categorias',]
       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Titulo'].widget.attrs['size'] = '100'
        self.fields['Post'].widget.attrs['size'] = '200'
        self.fields['Post'].widget.attrs['rows'] = '20'
        self.fields['Post'].widget.attrs['cols'] = '120'


class Buscar_post_Form(forms.Form):
    Post = forms.CharField(label='Ingresar una palabra del Titulo')
 




    




  