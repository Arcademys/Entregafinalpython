
# Create your views here.


from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm, ActualizarUsuarioForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('perfil_usuario')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registro.html', {'form': form})

@login_required
def perfil_usuario(request):
    if request.method == 'POST':
        form = ActualizarUsuarioForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil_usuario')
    else:
        form = ActualizarUsuarioForm(instance=request.user)
    return render(request, 'usuarios/perfil.html', {'form': form})