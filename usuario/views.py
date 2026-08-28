from django.shortcuts import render


def cadastro(request):
    return render(request, 'CadastroPerfil.html')


def login(request):
    return render(request, 'LoginPerfil.html')