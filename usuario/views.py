from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required

from .models import Aluno
from sistema.models import Curso, Serie, Disciplina


def cadastro(request):

    if request.method == 'POST':

        print("CHEGOU NO CADASTRO!")
        print(request.POST)

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        curso_id = request.POST.get('curso')

        disciplinas_ids = request.POST.getlist('disciplinas')

        # Verifica se o e-mail já está cadastrado
        if Aluno.objects.filter(email=email).exists():
            cursos = Curso.objects.all()

            return render(
                request,
                'CadastroPerfil.html',
                {
                    'erro': 'Este e-mail já está cadastrado.',
                    'cursos': cursos
                }
            )

        # Cria o aluno
        aluno = Aluno.objects.create_user(
            username=nome,
            email=email,
            password=senha
        )

        # Salva o curso escolhido
        aluno.curso_id = curso_id
        aluno.save()

        # Associa as disciplinas escolhidas ao aluno
        disciplinas = Disciplina.objects.filter(
            id__in=disciplinas_ids
        )

        for disciplina in disciplinas:
            disciplina.aluno = aluno
            disciplina.save()

        return redirect('login')

    # Busca os cursos cadastrados no banco
    cursos = Curso.objects.all()

    return render(
        request,
        'CadastroPerfil.html',
        {
            'cursos': cursos
        }
    )


def filtrar_disciplinas(request):

    curso_id = request.GET.get('curso')
    ano = request.GET.get('serie')

    if not curso_id or not ano:
        return JsonResponse([], safe=False)

    try:
        serie = Serie.objects.get(
            curso_id=curso_id,
            ano=ano
        )
    except Serie.DoesNotExist:
        return JsonResponse([], safe=False)

    disciplinas = Disciplina.objects.filter(
        serie=serie
    ).filter(
        cursos__id=curso_id
    ).distinct()

    dados = []

    for disciplina in disciplinas:
        dados.append({
            'id': disciplina.id,
            'nome': disciplina.nome
        })

    return JsonResponse(dados, safe=False)


def login(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        senha = request.POST.get('senha')

        usuario = authenticate(
            request,
            username=email,
            password=senha
        )

        if usuario is not None and usuario.is_active:

            auth_login(request, usuario)

            return redirect('home')

        return render(
            request,
            'LoginPerfil.html',
            {
                'erro': 'E-mail ou senha incorretos.'
            }
        )

    return render(request, 'LoginPerfil.html')


@login_required
def home(request):
    return render(request, 'PaginaHome.html')


@login_required
def perfil(request):
    return render(request, 'EdicaoPerfil.html')


@login_required
def tarefas(request):
    return render(request, 'PaginaTarefas.html')


@login_required
def duvidas(request):
    return render(request, 'Duvidas.html')


@login_required
def estatisticas(request):
    return render(request, 'PaginaEstatistica.html')

@login_required
def manual(request):
    return render(request, 'Manual.html')