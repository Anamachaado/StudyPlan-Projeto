from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),

    path(
        'cadastro/',
        views.cadastro,
        name='cadastro'
    ),

    path(
        'disciplinas/',
        views.filtrar_disciplinas,
        name='filtrar_disciplinas'
    ),

    path(
        'home/',
        views.home,
        name='home'
    ),

      path(
        'perfil/',
        views.perfil,
        name='perfil'
    ),

    path(
        'tarefas/',
        views.tarefas,
        name='tarefas'
    ),

    path(
        'duvidas/',
        views.duvidas,
        name='duvidas'
    ),

    path(
        'estatisticas/',
        views.estatisticas,
        name='estatisticas'
    ),

    path(
        'manual/',
        views.manual,
        name='manual'
    ),

]