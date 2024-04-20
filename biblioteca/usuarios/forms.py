


from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2', 'telefono', 'direccion')

class ActualizarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'telefono', 'direccion')