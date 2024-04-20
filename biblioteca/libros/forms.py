from django import forms
from .models import Libro, Avatar
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'editorial', 'fecha_publicacion', 'idioma']

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']