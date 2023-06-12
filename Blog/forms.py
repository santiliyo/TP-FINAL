from django.forms import ModelForm
from django import forms
from Blog.models import Post, Registro_usuario, Categoria
from django.contrib.auth.forms import UserCreationForm



class CategoriaForm(ModelForm):
    class Meta:
       model = Categoria
       fields = '__all__'


class BlogForm(ModelForm):
    class Meta:
       model = Post
       fields = ['Titulo', 'Post', 'Imagen', 'categorias', 'usuario', ]
       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Titulo'].widget.attrs['size'] = '100'
        self.fields['Post'].widget.attrs['size'] = '200'
        self.fields['Post'].widget.attrs['rows'] = '20'
        self.fields['Post'].widget.attrs['cols'] = '120'


class RegistroForm(ModelForm):
    clave = forms.CharField(widget=forms.PasswordInput)
    confirmar_clave = forms.CharField(widget=forms.PasswordInput)

    class Meta:
       model = Registro_usuario
       fields = '__all__'
           
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].widget.attrs['size'] = '20'
        self.fields['clave'].widget.attrs['size'] = '20'
        self.fields['confirmar_clave'].widget.attrs['size'] = '20'
        self.fields['mail'].widget.attrs['size'] = '20'
        self.fields['dni'].widget.attrs['size'] = '20'


class Buscar_post_Form(forms.Form):
    Titulo   = forms.CharField()   

class LoginForm(forms.Form):
    usuario = forms.CharField(label='Usuario:',max_length=15)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'label': 'Password:', 'max_length': 8})) 
 

class Buscar_usr_Form(forms.Form):
    usuario = forms.CharField()




  