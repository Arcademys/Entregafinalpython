
# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Libro, Avatar
from .forms import LibroForm, UserCreateForm, AvatarForm

def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 'libros/libro_list.html', {'libros': libros})

def libro_detail(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'libros/libro_detail.html', {'libro': libro})

@login_required
def libro_create(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = LibroForm()
    return render(request, 'libros/libro_form.html', {'form': form})

@login_required
def libro_update(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libro_detail', pk=libro.pk)
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/libro_form.html', {'form': form})

@login_required
def libro_delete(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('libro_list')
    return render(request, 'libros/libro_confirm_delete.html', {'libro': libro})

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('libro_list')
    else:
        form = UserCreateForm()
    return render(request, 'libros/registration/signup.html', {'form': form})

@login_required
def user_profile(request):
    try:
        avatar = request.user.avatar
    except Avatar.DoesNotExist:
        avatar = None

    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=avatar)
        if form.is_valid():
            avatar = form.save(commit=False)
            avatar.user = request.user
            avatar.save()
            return redirect('user_profile')
    else:
        form = AvatarForm(instance=avatar)

    return render(request, 'libros/user_profile.html', {'form': form, 'avatar': avatar})