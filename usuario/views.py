from django.shortcuts import render, redirect

def inicio(request):
    return redirect('cadastro')

def cadastro(request):
    return render(request, 'CadastroPerfil.html')

def login(request):
    return render(request, 'LoginPerfil.html')